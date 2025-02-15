import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression

file_name="usedcars.csv"
df = pd.read_csv(file_name)

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
y = df['price']

pipeline_steps = [
    ('scale', StandardScaler()), 
    ('polynomial', PolynomialFeatures(include_bias=False)), 
    ('model', LinearRegression())
]
pipe = Pipeline(pipeline_steps)

# Fit the pipeline
pipe.fit(Z, y)

# Predict
ypipe = pipe.predict(Z)
y = df[['price']]

ypipe_df = pd.DataFrame(ypipe , columns=['price'])
# Print first 4 predicted and actual values correctly
print("The first 4 predicted values are:", 
      {tuple(Z.iloc[i]): ypipe_df.iloc[i]['price'] for i in range(4)})

print("The first 4 actual values are:", 
      {tuple(Z.iloc[i]): y.iloc[i]['price'] for i in range(4)})

# Plot actual vs. predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y, ypipe, color='blue', label='Predicted vs Actual')  # Scatter plot for predictions
plt.plot(y, y, color='red', linestyle='--', label='Perfect Prediction')  # 45-degree reference line

# Labels and title
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Predicted vs Actual Prices")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
