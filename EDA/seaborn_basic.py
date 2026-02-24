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
print(df)

print("\n First 2 rows of the dataset:")
print(df.head(2))
print("\n Last 2 rows of the dataset:")
print(df.tail(2))
print("\n Summary statistics for numeric columns:")
print(df.describe())
