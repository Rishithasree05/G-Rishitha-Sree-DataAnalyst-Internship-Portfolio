import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
file_path = "../Dataset/Enhanced_Sales_Dataset.xlsx"
df = pd.read_excel(file_path)

# Separate sales by gender
male_sales = df[df["Gender"] == "Male"]["Total_Sales"].dropna()
female_sales = df[df["Gender"] == "Female"]["Total_Sales"].dropna()

# Calculate means
male_mean = male_sales.mean()
female_mean = female_sales.mean()

# Independent two-sample t-test
t_stat, p_value = ttest_ind(
    male_sales,
    female_sales,
    equal_var=False
)

# 95% confidence interval for difference in means
difference = male_mean - female_mean

print("=" * 60)
print("HYPOTHESIS TESTING - GENDER SALES")
print("=" * 60)

print(f"Male sample size: {len(male_sales)}")
print(f"Female sample size: {len(female_sales)}")

print(f"\nMale average sales: {male_mean:,.2f}")
print(f"Female average sales: {female_mean:,.2f}")

print(f"\nDifference in average sales: {difference:,.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.6f}")

print("\nSignificance level: 0.05")

if p_value < 0.05:
    print("\nRESULT: Reject the null hypothesis.")
    print("There is a statistically significant difference")
    print("in average sales between male and female customers.")
else:
    print("\nRESULT: Fail to reject the null hypothesis.")
    print("There is no statistically significant difference")
    print("in average sales between male and female customers.")

print("=" * 60)