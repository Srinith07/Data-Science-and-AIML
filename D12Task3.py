import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Price": [250000, 300000, 350000, 400000, 450000],
    "SquareFootage": [1500, 2000, 2500, 3000, 3500],
    "Bedrooms": [3, 4, 4, 5, 5],
    "City": ["A", "B", "C", "D", "E"]
})

# Correlation Matrix
corr_matrix = df.corr(numeric_only=True)

print(corr_matrix)

# Heatmap Visualization
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Price"])   # Replace with your main numerical column
plt.title("Boxplot of Price")
plt.show()
