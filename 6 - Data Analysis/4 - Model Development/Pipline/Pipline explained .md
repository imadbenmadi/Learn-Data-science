### **What Does This Pipeline Do?**

This pipeline **automates** the process of transforming the data and training a regression model in one step.

---

### **Step-by-Step Breakdown**

#### **1. Define Features (`X`) and Target (`y`)**

-   `X` contains 4 features: `'horsepower'`, `'curb-weight'`, `'engine-size'`, `'highway-mpg'`.
-   `y` is the `'price'` column (target variable).

```python
x = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
y = df['price']
```

---

#### **2. Create a Pipeline with Three Steps**

Each step performs a specific task:

```python
Input = [
    ('scale', StandardScaler()),            # Step 1: Standardize the features
    ('polynomial', PolynomialFeatures(include_bias=False)),  # Step 2: Generate polynomial features
    ('model', LinearRegression())           # Step 3: Train a linear regression model
]
```

✅ **Step 1: `StandardScaler()`**

-   Standardizes features to **zero mean** and **unit variance**.
-   Helps models handle different scales effectively.

✅ **Step 2: `PolynomialFeatures()`**

-   Expands the features to include **polynomial terms** (e.g., `x1^2`, `x1*x2`, etc.).
-   `include_bias=False` removes the constant term (bias).

✅ **Step 3: `LinearRegression()`**

-   Fits a **linear model** on the transformed polynomial features.

---

#### **3. Fit the Pipeline on the Data**

```python
pipe = Pipeline(Input)
pipe.fit(x, y)
```

-   `fit()` applies **all three steps sequentially**:
    1. Standardizes `X`.
    2. Generates polynomial features.
    3. Trains the linear regression model.

---

#### **4. Make Predictions**

```python
ypipe = pipe.predict(x)
```

-   The pipeline **automatically applies transformations** before making predictions.
-   The predicted `price` values are stored in `ypipe`.

---

### **Why Use a Pipeline?**

✅ Avoids **manual feature transformations** (scaling, polynomial expansion).  
✅ Ensures **consistent transformations** during training and prediction.  
✅ **Easy to reuse** and apply to new data.

---

### **TL;DR**

-   **Pipeline automates preprocessing + model training.**
-   **First, data is standardized** (`StandardScaler`).
-   **Then, polynomial features are generated** (`PolynomialFeatures`).
-   **Finally, a linear regression model is trained** (`LinearRegression`).
-   **Everything is done in one step** (`fit()`, `predict()`).
