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


plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=5, kde=True)
plt.title("Age Distribution")
plt.show()

plt.figure()
sns.histplot(df['salary'], bins=5, kde=True)
plt.title("Salary Distribution")
plt.show()

plt.figure()
sns.boxplot(x=df['Department'], y=df['Experience'])
plt.title("Experience by Department")
plt.show()

print("\n Department Value Counts:")
print(df['Department'].value_counts())

print("\n Gender Value Counts:")
print(df['Gender'].value_counts())
