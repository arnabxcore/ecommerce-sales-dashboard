import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Revenue
df["Revenue"] = df["Quantity"] * df["Price"]

print("========== E-COMMERCE SALES ANALYSIS ==========")

# Display data
print("\nSales Data:")
print(df)

# Total orders
print("\nTotal Orders:", len(df))

# Total products sold
print("Total Products Sold:", df["Quantity"].sum())

# Total revenue
print("Total Revenue:", df["Revenue"].sum())

# Average order revenue
print("Average Order Revenue:", df["Revenue"].mean())

# Highest revenue order
print("\nHighest Revenue Order:")
print(df.loc[df["Revenue"].idxmax()])

# Product-wise revenue
print("\nProduct-wise Revenue:")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

# Category-wise revenue
print("\nCategory-wise Revenue:")
print(df.groupby("Category")["Revenue"].sum())

# Region-wise revenue
print("\nRegion-wise Revenue:")
print(df.groupby("Region")["Revenue"].sum())

# Monthly revenue
print("\nMonthly Revenue:")
print(df.groupby(df["Date"].dt.month)["Revenue"].sum())

# Best-selling products
print("\nBest-Selling Products:")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False))

# Orders with revenue greater than 50,000
print("\nOrders Above 50,000:")
print(df[df["Revenue"] > 50000])

# Product revenue chart
product_revenue = df.groupby("Product")["Revenue"].sum()

product_revenue.plot(kind="bar")

plt.title("Revenue by Product", fontsize=14, fontweight='bold')
plt.xlabel("Product", fontsize=12, fontweight='bold')
plt.ylabel("Revenue", fontsize=12, fontweight='bold')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
