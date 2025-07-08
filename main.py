import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv("transfermarkt_players.csv")

# Clean the 'current_price' and 'difference' columns to extract numeric values
df["current_price_num"] = (
    df["current_price"]
    .str.replace("€", "")
    .str.replace("m", "")
    .str.replace(",", "")
    .astype(float)
)
df["difference_num"] = (
    df["difference"]
    .str.replace("€", "")
    .str.replace("m", "")
    .str.replace("+", "")
    .str.replace(",", "")
    .astype(float)
)

# # 1. Top 10 Most Valuable Players
# plt.figure(figsize=(12, 6))
# top_players = df.nlargest(10, "current_price_num")
# plt.bar(top_players["player_name"], top_players["current_price_num"], color="skyblue")
# plt.title("Top 10 Most Valuable Players")
# plt.ylabel("Current Price (Million €)")
# plt.xlabel("Player Name")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()

# # 2. Top 10 Clubs by Total Player Value
# plt.figure(figsize=(12, 6))
# club_value = (
#     df.groupby("club")["current_price_num"].sum().sort_values(ascending=False).head(10)
# )
# plt.bar(club_value.index, club_value.values, color="orange")
# plt.title("Top 10 Clubs by Total Player Value")
# plt.ylabel("Total Value (Million €)")
# plt.xlabel("Club")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()

# # 3. Distribution of Value Increase (difference)
# plt.figure(figsize=(10, 5))
# plt.hist(df["difference_num"], bins=20, color="green", edgecolor="black")
# plt.title("Distribution of Value Increase")
# plt.xlabel("Value Increase (Million €)")
# plt.ylabel("Number of Players")
# plt.tight_layout()
# plt.show()

# 4. Top 10 Players with Biggest Market Value Increase
plt.figure(figsize=(12, 6))
top_increase_players = df.nlargest(10, "difference_num")
plt.bar(top_increase_players["player_name"], top_increase_players["difference_num"], color="lightcoral")
plt.title("Top 10 Players with Biggest Market Value Increase")
plt.ylabel("Value Increase (Million €)")
plt.xlabel("Player Name")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
