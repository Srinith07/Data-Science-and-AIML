import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
population = np.random.exponential(scale=50000, size=100000)
plt.figure(figsize=(6, 4))
sns.histplot(population, kde=True)
plt.title("Original Population (Right-Skewed)")
plt.show()
sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())

sample_means = np.array(sample_means)
plt.figure(figsize=(6, 4))
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (n = 30, 1000 samples)")
plt.show()
print("Population Mean:", population.mean())
print("Mean of Sample Means:", sample_means.mean())
print("Population Std:", population.std())
print("Std of Sample Means (Standard Error):", sample_means.std())
