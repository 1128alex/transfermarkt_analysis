import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transfermarkt_players.csv")

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

plt.figure(figsize=(10, 6))
age_bins = [16, 18, 20, 22, 24, 26, 28, 30]
age_labels = ["17-18", "19-20", "21-22", "23-24", "25-26", "27-28", "29-30"]
df["age_group"] = pd.cut(
    df["age"].astype(int), bins=age_bins, labels=age_labels, right=True
)
age_increase = (
    df.groupby("age_group")["difference_num"].sum().sort_values(ascending=False)
)
plt.bar(age_increase.index, age_increase.values, color="purple")
plt.title("Total Market Value Increase by Age Group")
plt.ylabel("Total Value Increase (Million €)")
plt.xlabel("Age Group")
plt.tight_layout()
plt.show()

top_group = age_increase.idxmax()
top_value = age_increase.max()
print(
    f"Age group with biggest total value increase: {top_group} ({top_value:.2f} million €)"
)
