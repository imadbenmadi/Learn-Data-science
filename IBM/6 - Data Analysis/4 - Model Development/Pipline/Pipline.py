from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import clean data
df = pd.DataFrame({
    "price": [13495, 16500, 16500, 13950, 17450, 15250, 17710, 18920, 23875, 17859],
    "horsepower": [111, 154, 102, 115, 110, 110, 110, 140, 160, 101],
    "curb-weight": [2548, 2823, 2337, 2824, 2507, 2844, 2954, 3086, 3053, 2395],
    "engine-size": [130, 152, 109, 136, 136, 136, 136, 131, 131, 108],
    "highway-mpg": [27, 22, 24, 25, 20, 29, 27, 25, 20, 29]
})

# Features (X) and target (y)
X = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
y = df['price']

# Split into training and testing data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the pipeline
pipe = Pipeline([
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(degree=2, include_bias=False)),  # Degree=2 for quadratic terms
    ('model', LinearRegression())
])

# Train the model
pipe.fit(X_train, y_train)

# Predict on the test data
y_pred = pipe.predict(X_test)

# Print actual vs predicted values
print("Predicted values:", y_pred)
print("Actual values:", y_test.values)

# Plot predictions vs actual values
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='dashed', label="Perfect Fit")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Polynomial Regression Predictions vs Actual")
plt.legend()
plt.show()
