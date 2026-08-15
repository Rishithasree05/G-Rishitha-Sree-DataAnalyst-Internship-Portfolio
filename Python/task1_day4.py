import pandas as pd

# ==========================================
# STEP 1: Load Enhanced Dataset
# ==========================================
df = pd.read_excel("../Dataset/Enhanced_Sales_Dataset.xlsx")

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# ==========================================
# STEP 2: Total Sales
# ==========================================
print("\n1. Total Sales")
print("-" * 40)
print(f"₹ {df['Total_Sales'].sum():,.2f}")

# ==========================================
# STEP 3: Average Sales
# ==========================================
print("\n2. Average Sales")
print("-" * 40)
print(f"₹ {df['Total_Sales'].mean():,.2f}")

# ==========================================
# STEP 4: Total Orders
# ==========================================
print("\n3. Total Orders")
print("-" * 40)
print(df["Order_ID"].count())

# ==========================================
# STEP 5: Sales by Category
# ==========================================
print("\n4. Sales by Category")
print("-" * 40)
print(df.groupby("Category")["Total_Sales"].sum())

# ==========================================
# STEP 6: Sales by City
# ==========================================
print("\n5. Top 10 Cities by Sales")
print("-" * 40)
print(
    df.groupby("City")["Total_Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# ==========================================
# STEP 7: Sales by Month
# ==========================================
print("\n6. Sales by Month")
print("-" * 40)
print(df.groupby("Month_Name")["Total_Sales"].sum())

# ==========================================
# STEP 8: Top Products
# ==========================================
print("\n7. Top 10 Products by Sales")
print("-" * 40)
print(
    df.groupby("Product")["Total_Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# ==========================================
# STEP 9: Average Customer Age
# ==========================================
print("\n8. Average Customer Age")
print("-" * 40)
print(round(df["Age"].mean(), 2))

# ==========================================
# STEP 10: Gender Distribution
# ==========================================
print("\n9. Gender Distribution")
print("-" * 40)
print(df["Gender"].value_counts())

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)