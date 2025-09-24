import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\Data Science\Projects\VideoGamesProject-main\VideoGamesSales.csv")
# print(df.head())
# print(f"Columns is {df.shape[0]} ")
# print(f"Rows is {df.shape[1]} ")
# df = df[df.duplicated()]
# print(f"Duplicate Rows are {df.shape[0]} ")
# print(f"Duplicate Columns are {df.shape[1]} ")
df = df.drop_duplicates()
# print(f"After removing duplicates, Rows are {df.shape[0]} ")
# print(df.info())
# print(df.isnull().sum())
df["Region"] = df["Region"].fillna("North")
# print(df.shape[0])
# df = df[df["Region"].isnull()]
# print(df.shape[0])
# print(df.isnull().sum())
# df = df.head(100)
df["NA_Sales"] = df["NA_Sales"].replace('$' , " " , regex= True)
df["NA_Sales"] = pd.to_numeric(df["NA_Sales"], errors='coerce')
Average_NA_Sales = df["NA_Sales"].mean()
Average_NA_Sales = round(Average_NA_Sales, 2)
df["NA_Sales"] = df["NA_Sales"].fillna(Average_NA_Sales)
df["Country"] = df["Country"].replace("USA", "United States")
df["Country"] = df["Country"].str.title()
# df = df[df["Country"] == "Australia"]
df = df.rename(columns={"NA_Sales" : "National Sales", "Global_Sales" : "Global Sales" , "NA_Profit" : "National Profit","Global_Profit": "Global Profit"})
sales_cap = df["National Sales"].quantile(0.95)
print(f"Sales cap is {sales_cap}")
df["National Sales"] = np.where(df["National Sales"] > sales_cap, sales_cap, df["National Sales"])

# print(f"Average NA Sales is {Average_NA_Sales}")

# df = df[df["National Sales"] < sales_cap]
print(df)

#Chart bar 
National_sales = df.groupby(["Region" , "Country"])["National Sales"].sum().reset_index().sort_values("National Sales", ascending=False)
# plt.figure(figsize=(16, 8))
# sns.barplot(data = National_sales, x="Region", y="National Sales", hue="Country", palette="viridis")
# plt.title("National Sales by Country and Region" , fontweight='bold', fontsize=16 )
# plt.xlabel("Region")
# plt.ylabel("National Sales")    
# plt.xticks(rotation=45)
# plt.legend(title="Country")
# plt.tight_layout()
# plt.show()
# print(df)
# # print(National_sales)

# plt.figure(figsize=(10, 6))
# sns.boxplot(data = df , x = "Country" , y = "National Sales"   , hue= "Genre")
# plt.title("National Sales by Country and Genre", fontweight='bold', fontsize=16)
# plt.xlabel("Country" , fontweight='bold', fontsize=14)
# plt.ylabel("National Sales" , fontweight='bold', fontsize=14)
# plt.xticks(rotation=45) 
# plt.legend(title="Genre")
# plt.tight_layout()
# plt.show()

# create a pie chart

# Sales = df.groupby(["Country"])[["National Sales" , "Global Sales"]].sum().reset_index()
# Country = Sales["Country"]
# National_sales = Sales["National Sales"]
# Global_sales = Sales["Global Sales"]

# fig , axs = plt.subplots(1, 2, figsize=(10, 7))
# axs[0].pie(National_sales, labels=Country, autopct='%1.1f%%', startangle=90)
# axs[0].set_title("National Sales by Country", fontweight='bold', fontsize=16)

# axs[1].pie(Global_sales, labels=Country , autopct = "%1.1f%%" , startangle = 90)
# axs[1].set_title("Global Sale by Country" , fontweight='bold', fontsize=16)

# plt.show()

# Create a scatter plot
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x="National Sales", y="Global Sales", hue="Region", style="Genre", size="Global Sales", sizes=(20, 200), alpha=0.7)
# plt.title("National Sales vs Global Sales", fontweight='bold', fontsize=16)
# plt.xlabel("National Sales", fontweight='bold', fontsize=14)
# plt.ylabel("Global Sales", fontweight='bold', fontsize=14)
# plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.show()
# hello zaid here
# create a line chart
plt.plot(df["Year"], df["National Sales"], marker='o', linestyle='-', color='b' , label='National Sales')
plt.plot(df["Year"], df["Global Sales"], marker='x', linestyle='--', color='g', label='Global Sales')
plt.title("National Sales vs Global Sales Over Years", fontweight='bold', fontsize=16)
plt.xlabel("Year", fontweight='bold', fontsize=14)
plt.ylabel("Sales", fontweight='bold', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Sales Type")
# plt.tight_layout()
plt.grid(True)
plt.tight_layout()
plt.show()


