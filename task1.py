import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "Price": [250000, 300000, 350000, 400000, 450000],
    "Size": [1500, 2000, 2500, 3000, 3500],
    "Bedrooms": [3, 4, 4, 5, 5],
    "City": ["A", "B", "C", "D", "E"]
})

plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
plt.figure(figsize=(8, 5))
sns.countplot(x="City", data=df)
plt.title("Count of Houses by City")
plt.xticks(rotation=45)
plt.show()
