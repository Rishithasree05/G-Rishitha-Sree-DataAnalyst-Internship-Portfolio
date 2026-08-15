import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: Load Enhanced Dataset
# ==========================================
df = pd.read_excel("../Dataset/Enhanced_Sales_Dataset.xlsx")

print("=" * 60)
print("DATA VISUALIZATION")
print("=" * 60)

# ==========================================
# CHART 1: Sales by Category
# ==========================================
category_sales = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("../Reports/category_sales.png")
plt.show()

# ==========================================
# CHART 2: Monthly Sales
# ==========================================
monthly_sales = df.groupby("Month_Name")["Total_Sales"].sum()

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("../Reports/monthly_sales.png")
plt.show()

# ==========================================
# CHART 3: Gender Distribution
# ==========================================
gender = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
gender.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("../Reports/gender_distribution.png")
plt.show()

# ==========================================
# CHART 4: Age Distribution
# ==========================================
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../Reports/age_distribution.png")
plt.show()

# ==========================================
# CHART 5: Top Products
# ==========================================
top_products = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("../Reports/top_products.png")
plt.show()

# ==========================================
# CHART 6: Top Cities
# ==========================================
top_cities = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
top_cities.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("../Reports/city_sales.png")
plt.show()

print("\n" + "=" * 60)
print("ALL CHARTS CREATED SUCCESSFULLY")
print("Charts saved inside Reports folder.")
print("=" * 60)
