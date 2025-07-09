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

# # 4. Top 10 Players with Biggest Market Value Increase
# plt.figure(figsize=(12, 6))
# top_increase_players = df.nlargest(10, "difference_num")
# plt.bar(
#     top_increase_players["player_name"],
#     top_increase_players["difference_num"],
#     color="lightcoral",
# )
# plt.title("Top 10 Players with Biggest Market Value Increase")
# plt.ylabel("Value Increase (Million €)")
# plt.xlabel("Player Name")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()

# 5. Age Group with Biggest Total Value Increase
plt.figure(figsize=(10, 6))
# Define age bins (customize as needed)
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

# Print the age group with the biggest increase
top_group = age_increase.idxmax()
top_value = age_increase.max()
print(
    f"Age group with biggest total value increase: {top_group} ({top_value:.2f} million €)"
)
