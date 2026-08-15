import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Load the dataset
df = pd.read_excel("../Dataset/Enhanced_Sales_Dataset.xlsx")

# Select numeric columns
numeric_df = df[["Age", "Quantity", "Unit_Price", "Total_Sales"]]

# Create Pair Plot
scatter_matrix(
    numeric_df,
    figsize=(10, 10),
    diagonal="hist"
)

# Title
plt.suptitle("Pair Plot")

# Save the image
plt.savefig("../Reports/pair_plot.png")

# Display the plot
plt.show()

print("Pair Plot Created Successfully!")