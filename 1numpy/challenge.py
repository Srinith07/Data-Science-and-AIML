import numpy as np

pm_values = np.array([85, 90, 78, 120, 95, 100, 130])
avg_pm2 = np.mean(pm_values)
print("Average PM2 value:", avg_pm2)
identifyed_pollution = pm_values > 100
print("Identified pollution levels (True for > 100):", identifyed_pollution)
percentage_polluted = np.sum(identifyed_pollution) / len(pm_values) * 100
print("Percentage of polluted days:", percentage_polluted, '%')
