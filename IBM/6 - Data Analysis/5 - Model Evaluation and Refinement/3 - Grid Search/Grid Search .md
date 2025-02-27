Grid search is a technique used for **hyperparameter tuning**, where you try out a **range of hyperparameters** to find the best combination that results in the most effective model.

### Here's the breakdown:

1. **Hyperparameters** are values you set before training the model, like:

    - The learning rate in gradient descent.
    - The value of \( \alpha \) in Ridge or Lasso regression.
    - The number of trees in a random forest.
    - The kernel type in SVM, etc.

2. **Grid Search** involves creating a grid of possible values for each hyperparameter, then training and evaluating the model on each combination of hyperparameters.

### How it works:

1. **Define a list of values** to test for each hyperparameter.
   For example:

    - For \( \alpha \) in Ridge regression, you might try [0.1, 1, 10, 100].
    - For `max_depth` in a decision tree, you might try [5, 10, 20].

2. **Train your model** with each combination of hyperparameters.

3. **Evaluate performance** using a metric like accuracy, MSE, R-squared, etc.

4. **Choose the best combination** that gives the best performance based on your evaluation metric.

### Example:

```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression

# Create a dataset
X, y = make_regression(n_samples=100, n_features=2, noise=0.1)

# Define a Ridge model
model = Ridge()

# Define the parameter grid
param_grid = {
    'alpha': [0.1, 1, 10, 100]
}

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)

# Fit the grid search to data
grid_search.fit(X, y)

# Print the best parameters and score
print("Best parameters found: ", grid_search.best_params_)
print("Best score found: ", grid_search.best_score_)
```

### What's happening here:

-   `param_grid` defines the possible values for hyperparameters (`alpha` in this case).
-   `GridSearchCV` will train and evaluate the model using **5-fold cross-validation** for each combination of `alpha` values.
-   After running, the `best_params_` will give the combination of hyperparameters that worked best.

### Pros of Grid Search:

-   Exhaustive search over all possible combinations.
-   Can be combined with cross-validation to give a more accurate evaluation.

### Cons of Grid Search:

-   **Computationally expensive**: As you test more combinations, it increases exponentially. (called **curse of dimensionality**).
-   Not efficient when the parameter grid is large.

If you're looking for a faster approach, you can use **RandomizedSearchCV**, which samples random combinations of hyperparameters instead of trying all possible values.

Let me know if you need more examples or details!
