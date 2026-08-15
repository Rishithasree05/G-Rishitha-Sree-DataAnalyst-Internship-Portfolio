import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("../Dataset/Enhanced_Sales_Dataset.xlsx")

# Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# Create correlation matrix
corr = numeric_df.corr()

# Plot heatmap
plt.figure(figsize=(10,8))
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")
plt.tight_layout()

# Save chart
plt.savefig("../Reports/correlation_heatmap.png")

plt.show()

print("Correlation Heatmap Created Successfully!")