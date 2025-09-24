
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

st.title("Simple Linear Regression")

# Sidebar for user inputs
st.sidebar.header("Parameters")
a_true = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.5, 0.1)
variance = st.sidebar.slider("Noise Variance", 0, 1000, 100)
num_points = st.sidebar.slider("Number of points", 100, 1000, 100, 10)
b_true = 10 # Fixed intercept for simplicity

# Generate data
np.random.seed(0)
X = np.linspace(0, 10, num_points).reshape(-1, 1)
std_dev = np.sqrt(variance)
y = a_true * X.ravel() + b_true + np.random.normal(0, std_dev, num_points)

# Perform linear regression
model = LinearRegression()
model.fit(X, y)
a_pred = model.coef_[0]
b_pred = model.intercept_

# Calculate residuals and identify top 5 outliers
residuals = y - model.predict(X)
abs_residuals = np.abs(residuals)
outlier_indices = np.argsort(abs_residuals)[-5:]
outlier_x = X[outlier_indices]
outlier_y = y[outlier_indices]
outlier_residuals = residuals[outlier_indices]

# Display results
st.write(f"Original parameters: a = {a_true}, b = {b_true}")
st.write(f"Predicted parameters: a = {a_pred:.2f}, b = {b_pred:.2f}")

# Plotting
fig, ax = plt.subplots()
ax.scatter(X, y, label='Data points')
ax.plot(X, a_true * X + b_true, color='r', linestyle='--', label='Original line')
ax.plot(X, model.predict(X), color='g', label='Fitted line')
ax.scatter(outlier_x, outlier_y, color='red', label='Top 5 Outliers')
for i, index in enumerate(outlier_indices):
    ax.text(outlier_x[i], outlier_y[i], str(index), fontsize=9)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# Display outlier table
st.subheader("Top 5 Outliers")
outlier_df = pd.DataFrame({
    "Index": outlier_indices,
    "X Value": outlier_x.flatten(),
    "Y Value": outlier_y,
    "Residual": outlier_residuals
})
st.table(outlier_df)
