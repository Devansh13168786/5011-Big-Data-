import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm

# Load datasets
df_full = pd.read_csv("C:/Users/HP/Desktop/1 pro/Trips_Full Data.csv")
df = pd.read_csv("C:/Users/HP/Downloads/Trips_by_Distance (3).csv")

# Convert 'Date' to datetime format and filter records for week 32 in both datasets
df_full['Date'] = pd.to_datetime(df_full['Date'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df_full_week32 = df_full[df_full['Week of Date'] == 32]
df_week32 = df[df['Week'] == 32]

# Select 'Trips 10-25 Miles' from df_full_week32 as 'x' and 'Number of Trips 10-25' from df_week32 as 'y'
n = min(len(df_full_week32), len(df_week32))
X = df_full_week32['Trips <1 Mile'].iloc[:n].values.reshape(-1, 1)
y = df_week32['Number of Trips >=500'].iloc[:n].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model Training
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred_lr_train = model_lr.predict(X_train)
y_pred_lr_test = model_lr.predict(X_test)

# Polynomial Regression Model Training
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test)  # Generating X_poly_test
model_poly = LinearRegression()
model_poly.fit(X_poly_train, y_train)
y_pred_poly_train = model_poly.predict(X_poly_train)
y_pred_poly_test = model_poly.predict(X_poly_test)

# Advanced Linear Regression With statsmodels
X_sm_train = sm.add_constant(X_train)
model_sm = sm.OLS(y_train, X_sm_train)
results_sm = model_sm.fit()
X_sm_test = sm.add_constant(X_test)  # Adding constant to X_test for prediction
y_pred_sm_train = results_sm.predict(X_sm_train)
y_pred_sm_test = results_sm.predict(X_sm_test)

# Print model details and predictions
print("Linear Regression:")
print(f"Training Coefficient of determination: {model_lr.score(X_train, y_train)}")
print(f"Predictions (Training):\n{y_pred_lr_train}")
print(f"Predictions (Testing):\n{y_pred_lr_test}")

print("\nPolynomial Regression:")
print(f"Training Coefficient of determination: {model_poly.score(X_poly_train, y_train)}")
print(f"Predictions (Training):\n{y_pred_poly_train}")
print(f"Predictions (Testing):\n{y_pred_poly_test}")

print("\nOLS Regression Results:")
print(results_sm.summary())
print("OLS Predictions (Training):")
print(y_pred_sm_train)
print("OLS Predictions (Testing):")
print(y_pred_sm_test)

# Visualizations
# Scatter Plot with Regression Line for Linear Regression
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Actual data')
plt.plot(X_train, y_pred_lr_train, color='red', label='Fitted line - Linear')
plt.title('Linear Regression: Actual vs Predicted')
plt.xlabel('Trips <1 Mile')
plt.ylabel('Number of Trips >=500')
plt.legend()
plt.show()

# Scatter Plot with Regression Line for Polynomial Regression
plt.figure(figsize=(10, 6))
X_range = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)
X_range_poly = poly_features.transform(X_range)
plt.scatter(X_train, y_train, color='blue', label='Actual data')
plt.plot(X_range, model_poly.predict(X_range_poly), color='green', label='Fitted line - Polynomial')
plt.title('Polynomial Regression: Actual vs Predicted')
plt.xlabel('Trips <1 Mile')
plt.ylabel('Number of Trips >=500')
plt.legend()
plt.show()
