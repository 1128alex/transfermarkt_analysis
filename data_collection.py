from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pyautogui
from pyautogui import ImageNotFoundException

options = Options()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
options.add_argument("user-agent=" + user_agent)

import pandas as pd

chrome_driver_path = "C:/chromedriver-win64/chromedriver.exe"
google_url = "https://www.google.com"
transfermarkt_url = (
    "https://www.transfermarkt.com/spieler-statistik/marktwertspruenge/marktwertetop"
)


def safe_locate_on_screen(confidence, *args, **kwargs):
    try:
        return pyautogui.locateOnScreen(*args, **kwargs, confidence=confidence)
    except ImageNotFoundException:
        return None


service = Service(executable_path=chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get(google_url)

pyautogui.sleep(2)

w = pyautogui.getWindowsWithTitle("Google - Chrome")[0]
print(w)
if w.isActive == False:
    w.activate()
w.maximize()

browser.get(transfermarkt_url)

accept_button = safe_locate_on_screen(0.9, "./images/accept.png")
pyautogui.click(accept_button)

pyautogui.sleep(13)

datas = []

for i in range(4):
    table = browser.find_element(By.XPATH, '//*[@id="yw1"]/table')
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        tds = row.find_elements(By.TAG_NAME, "td")

        if len(tds) < 11:
            continue

        """
        0: index        
        1: second column       
            2: image        
            3: name        
            4: position        
        5: team
        6: nationality 
        7: age 
        8: current market value 
        9: change rate 
        10: difference 
        """

        name = tds[3].find_element(By.TAG_NAME, "a").get_attribute("title")
        position = tds[4].text
        club = tds[5].find_element(By.TAG_NAME, "img").get_attribute("title")
        nationality = tds[6].find_element(By.TAG_NAME, "img").get_attribute("title")
        age = tds[7].text
        current_value = tds[8].text
        percentage = tds[9].text
        difference = tds[10].text

        # # test
        # print("name:", name, end=", ")
        # print("position:", position, end=", ")
        # print("club:", club, end=", ")
        # print("age:", age, end=", ")
        # print("nationality:", nationality, end=", ")
        # print("current_value:", current_value, end=", ")
        # print("percentage:", percentage, end=", ")
        # print("difference:", difference)

        datas.append(
            {
                "player_name": name,
                "position": position,
                "club": club,
                "nationality": nationality,
                "age": age,
                "current_value": current_value,
                "percentage": percentage,
                "difference": difference,
            }
        )
    pyautogui.sleep(1)

    # next page
    browser.execute_script("window.scrollTo(2000, 1500)")
    next_page_button = browser.find_element(
        By.XPATH, '//a[@title="Go to the next page"]'
    )
    next_page_button.click()

    pyautogui.sleep(2)

    # close ad
    close_button = safe_locate_on_screen(0.95, "./images/close.png")
    close_button2 = safe_locate_on_screen(0.95, "./images/close2.png")
    close_button3 = safe_locate_on_screen(0.95, "./images/close3.png")
    if close_button is not None:
        pyautogui.click(close_button)
    if close_button2 is not None:
        pyautogui.click(close_button2)
    if close_button3 is not None:
        pyautogui.click(close_button3)

    pyautogui.sleep(20)

df = pd.DataFrame(datas)
print(df)

df.to_csv("transfermarkt_players.csv")
print("Success!")

input("Press Enter to exit and close the browser...")
browser.quit()
