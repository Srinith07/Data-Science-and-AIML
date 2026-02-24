import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=1000)
incomes = np.random.exponential(scale=50000, size=1000)
scores = 100 - np.random.exponential(scale=10, size=1000)
scores = np.clip(scores, 0, 100)
df = pd.DataFrame({
    'Heights': heights,
    'Incomes': incomes,
    'Scores': scores
})

plt.figure(figsize=(15, 4))
for i, column in enumerate(df.columns, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[column], kde=True)
    mean_val = df[column].mean()
    median_val = df[column].median()
    plt.axvline(mean_val, color='red', linestyle='--',
                label=f"Mean: {mean_val:.1f}")
    plt.axvline(median_val, color='green', linestyle='-',
                label=f"Median: {median_val:.1f}")
    plt.title(column)
    plt.legend()
plt.tight_layout()
plt.show()

for column in df.columns:
    mean_val = df[column].mean()
    median_val = df[column].median()
    print(f"{column} -> Mean: {mean_val:.2f}, Median: {median_val:.2f}")
