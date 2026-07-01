import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("real Estate.csv",)
print(df)
print(df.info)
print(df.info())
print(df.shape)

print(df.isnull().sum())

print(df.head(10))

print(df.duplicated().sum())
print(df.drop_duplicates())

df.columns = (df.columns.str.strip().str.lower().str.replace(" ","_"))
print(df.columns)

df["price"] = df["price"].astype(str).str.replace(",", "").astype(int)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

df.info()
df["status"] = (df["status"].str.strip().str.lower())

df["rera_approval"] = (df["rera_approval"].str.strip().str.lower())

df["flat_type"] = (df["flat_type"].str.strip().str.lower())

print(df["status"].unique())

print(df["rera_approval"].unique())

print(df["flat_type"].unique())

df = df.drop_duplicates()
print(df)

#which is the costliest property 
costliest_flat = df.loc[df["price"].idxmax()]
print(costliest_flat)

#Which locality has the highest average price?
highest_avg_price = (df.groupby("locality")["price"].mean().sort_values(ascending = False))
print(highest_avg_price)

#Which locality has the highest rate per square foot?
highest_rate = (df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending = False))
print(highest_rate.head())

#Do ready-to-move properties cost more than under-construction properties?
status_price = (df.groupby ("status")["price"].median())
print(status_price)

#Do RERA-approved properties command a price premium?
print(df.groupby("rera_approval")["price"].median())

#How does area (sqft) impact property price?
sns.scatterplot(data = df, x="area",y= "price")
plt.title("Area vs Price")
plt.savefig("Area_vs_Price.png")
plt.show()

#Which BHK configuration is the most expensive on average?
bhk_price = df.groupby("bhk_count")["price"].mean().sort_values(ascending=False)
print(bhk_price)
#visualization
bhk_price.plot(figsize=(10,5))
plt.title("Average Price by BHK")
plt.xlabel("BHK Count")
plt.ylabel("Average Price")
plt.savefig("BHK price.png")
plt.show()

#Which property type (Apartment, Floor, Plot) is the costliest?
property_price = (df.groupby("flat_type")["price"].mean().sort_values(ascending = False ))
print(property_price)

#Do certain builders or companies consistently price higher?
builder_price =  (df.groupby("company_name")["price"].mean().sort_values(ascending = False))
builder_price_cr = builder_price / 10000000
print(builder_price_cr.head(10))

#visualization
# Top 10 premium builders

top_builders = (
    df.groupby("company_name")["price"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

# Convert into Crores for better readability
top_builders = top_builders / 10000000

# Plot
plt.figure(figsize=(10,6))

top_builders.plot(kind="bar")

plt.title("Top 10 Premium Builders in Gurgaon")
plt.xlabel("Builder / Company")
plt.ylabel("Average Price (Crores)")

plt.xticks(rotation=45)
plt.savefig("top builder.png")
plt.show()

#Are larger homes always more expensive per square foot?
#visualization
plt.figure(figsize=(10,6))

sns.regplot(
    data=df,
    x="area",
    y="rate_per_sqft",
    scatter_kws={"alpha":0.3}
)

plt.title("Area vs Rate Per Sqft")
plt.xlabel("Area (Sqft)")
plt.ylabel("Rate Per Sqft")
plt.savefig("Area square.png")
plt.show()
