import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set(style='whitegrid')
data = {
    "Age": [25, 30, 35, 40, 45],
    "salary": [50000, 60000, 70000, 80000, 90000],
    "Experience": [2, 5, 7, 10, 12],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "Gender": ["Male", "Female", "Male", "Female", "Male"]
}

df = pd.DataFrame(data)
corr_matrix = df.corr(numeric_only=True)
print("Correlation Matrix:")
print(corr_matrix)

plt
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()


# outlier detection
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Department'])
plt.title("Department Boxplot")
plt.show()
