import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example: load dataset
df = pd.DataFrame({
    "Price": [250000, 300000, 350000, 400000, 450000],
    "SquareFootage": [1500, 2000, 2500, 3000, 3500],
    "Bedrooms": [3, 4, 4, 5, 5],
    "City": ["A", "B", "C", "D", "E"]
})

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='SquareFootage', y='Price')

plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='City', y='Price')

plt.title("Price Distribution by City")
plt.xticks(rotation=45)
plt.show()

correlation = df['SquareFootage'].corr(df['Price'])
print("Correlation:", correlation)
