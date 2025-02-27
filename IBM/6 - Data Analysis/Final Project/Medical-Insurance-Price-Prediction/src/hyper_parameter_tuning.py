

# Define possible values for k (K-Folds) and alpha (regularization)
k_values = range(5,10)  # Different K values to test
alphas = alphas = np.linspace(0.01, 10, num=100)  # Different alpha values for Ridge Regression

# Set the best polynomial degree from previous testing
# we know it is 2 from the previos code 
best_degree = 2

# Store results for different k values
best_results = []

best_k = None
for k in k_values:
    print(f"\nTesting for k = {k} folds...\n")

    # Define Ridge regression model
    ridge = Ridge()

    # Define the pipeline (Polynomial Features + Ridge)
    pipeline = Pipeline([
        ('poly', PolynomialFeatures(degree=best_degree)),
        ('ridge', ridge)
    ])

    # Define the hyperparameter grid
    param_grid = {
        'ridge__alpha': alphas,
        'ridge__fit_intercept': [True, False]
    }

    # Perform GridSearchCV to find best alpha and fit_intercept
    grid_search = GridSearchCV(pipeline, param_grid, cv=k, scoring='r2')
    grid_search.fit(x_train, y_train)

    # Extract best parameters
    best_alpha = grid_search.best_params_['ridge__alpha']
    best_fit_intercept = grid_search.best_params_['ridge__fit_intercept']
    best_r2 = grid_search.best_score_

    # Store the results
    best_results.append((k, best_alpha, best_fit_intercept, best_r2))
    print(f"Best for k={k}: alpha={best_alpha}, fit_intercept={best_fit_intercept}, R²={best_r2:.4f}")
    best_k = k
    
    print("_____________________________")

# Find the overall best k and alpha
best_k, best_alpha, best_fit_intercept, best_r2 = max(best_results, key=lambda x: x[3])

print("\nFinal Best Selection:")
print(f"Best k: {best_k}")
print(f"Best alpha: {best_alpha}")
print(f"Best fit_intercept: {best_fit_intercept}")
print(f"Best R² score: {best_r2}")
print(f"Best k: {best_k:.4f}")

# Train the final Ridge model with the best parameters
ridge_final = Ridge(alpha=best_alpha, fit_intercept=best_fit_intercept)
pr = PolynomialFeatures(degree=best_degree)
x_train_poly = pr.fit_transform(x_train)
x_test_poly = pr.transform(x_test)

ridge_final.fit(x_train_poly, y_train)

# Predict and evaluate
yhat_ridge = ridge_final.predict(x_test_poly)
print('Final Model Evaluation:')
print(f'R2: {r2_score(y_test, yhat_ridge):.4f}')
print(f'MSE: {mean_squared_error(y_test, yhat_ridge):.4f}')

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
sns.distplot(y_test, hist=False, color="r", label="Actual Value")
sns.distplot(yhat_ridge, hist=False, color="b", label="Fitted Values")
plt.title('Actual vs Fitted Values for Charges (Ridge Regression)')
plt.xlabel('Charges')
plt.ylabel('Proportion of Charges')
plt.legend()
plt.show()