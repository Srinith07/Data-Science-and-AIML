import numpy as np
import pandas as pd
np.random.seed(42)
data = np.random.normal(loc=170, scale=10, size=1000)
data = np.append(data, [210, 220, 130, 120])
df = pd.DataFrame({'Height': data})
mean_val = df['Height'].mean()
std_val = df['Height'].std()
print("Mean (μ):", round(mean_val, 2))
print("Standard Deviation (σ):", round(std_val, 2))

df['z_score'] = (df['Height'] - mean_val) / std_val
outliers = df[np.abs(df['z_score']) > 3]

print("Number of outliers:", len(outliers))
print(outliers)
