import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("../Dataset/Enhanced_Sales_Dataset.xlsx")

# Scatter Plot
plt.figure(figsize=(8,6))
plt.scatter(df["Age"], df["Total_Sales"])

plt.title("Age vs Total Sales")
plt.xlabel("Age")
plt.ylabel("Total Sales")

plt.savefig("../Reports/age_vs_sales_scatter.png")
plt.show()

print("Scatter Plot Created Successfully!")