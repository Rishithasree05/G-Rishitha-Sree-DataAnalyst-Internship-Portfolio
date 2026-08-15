import pandas as pd

# Load dataset
df = pd.read_excel("../Dataset/Enhanced_Sales_Dataset.xlsx")

print("="*60)
print("DESCRIPTIVE STATISTICS")
print("="*60)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nSummary Statistics")
print(df.describe())

print("\nAverage Age")
print(df["Age"].mean())

print("\nAverage Sales")
print(df["Total_Sales"].mean())

print("\nMaximum Sales")
print(df["Total_Sales"].max())

print("\nMinimum Sales")
print(df["Total_Sales"].min())

print("\nCategory Distribution")
print(df["Category"].value_counts())

print("\nGender Distribution")
print(df["Gender"].value_counts())

print("\nCity Distribution")
print(df["City"].value_counts())