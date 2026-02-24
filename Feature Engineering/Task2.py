from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    'Age': [22, 25, 30, 35, 40, 45, 50],
    'Salary': [20000, 30000, 40000, 60000, 80000, 100000, 120000]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)

standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data:\n", df_standardized)

minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data:\n", df_normalized)

# Before Scaling
plt.figure()
plt.hist(df['Salary'])
plt.title("Salary - Original")
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# After Standardization
plt.figure()
plt.hist(df_standardized['Salary'])
plt.title("Salary - Standardized")
plt.xlabel("Scaled Salary")
plt.ylabel('Frequency')
plt.show()

# After Normalization
plt.figure()
plt.hist(df_normalized['Salary'])
plt.title("Salary - Normalized")
plt.xlabel("Scaled Salary")
plt.ylabel('Frequency')
plt.show()
