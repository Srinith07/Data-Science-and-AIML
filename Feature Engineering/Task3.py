import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Feature (Experience)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

# Target (Salary) with curved relationship
y = np.array([30, 35, 45, 60, 80, 105, 135, 170, 210, 255])

model_linear = LinearRegression()
model_linear.fit(X, y)

y_pred_linear = model_linear.predict(X)
r2_linear = r2_score(y, y_pred_linear)

print("R² (Linear):", r2_linear)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression()
model_poly.fit(X_poly, y)

y_pred_poly = model_poly.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

print("R² (Polynomial):", r2_poly)

plt.scatter(X, y, label="Actual")

plt.plot(X, y_pred_linear, label="Linear Model")
plt.plot(X, y_pred_poly, label="Polynomial Model")

plt.legend()
plt.title("Linear vs Polynomial Fit")
plt.show()
