import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("../Dataset/Enhanced_Sales_Dataset.xlsx")

print("=" * 60)
print("UNIVARIATE ANALYSIS")
print("=" * 60)

# -----------------------------
# Histogram - Customer Age
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10, edgecolor="black")
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../Reports/age_histogram.png")
plt.show()

print("Age Histogram Created")

# -----------------------------
# Bar Chart - Product Category
# -----------------------------
category = df["Category"].value_counts()

plt.figure(figsize=(8,5))
category.plot(kind="bar")
plt.title("Product Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("../Reports/category_bar_chart.png")
plt.show()

print("Category Bar Chart Created")

# -----------------------------
# Bar Chart - Gender
# -----------------------------
gender = df["Gender"].value_counts()

plt.figure(figsize=(6,5))
gender.plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("../Reports/gender_bar_chart.png")
plt.show()

print("Gender Bar Chart Created")

print("\nAll Univariate Analysis Charts Created Successfully!")