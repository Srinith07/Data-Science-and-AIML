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
sns.scatterplot(x=df['Age'], y=df['salary'], data=df)
plt.title("Age vs Salary")
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend(title="Department / Gender")
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Department'], y=df['Experience'], data=df)
plt.title("Experience by Department")
plt.xlabel('Department')
plt.ylabel('Experience')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Experience', data=df)
plt.title("Experience by Gender")
plt.xlabel('Gender')
plt.ylabel('Experience')
plt.show()
