# Medical Charges Prediction - Project Report

## 1. Introduction

This project aims to predict **medical insurance charges** based on demographic and health-related features. I explored the dataset, performed exploratory data analysis (EDA), and tested multiple models to achieve the best predictive performance.

---

## 2. Dataset Overview

### **Features:**

-   `age`: Age of the person
-   `bmi`: Body Mass Index
-   `no_of_children`: Number of children covered by insurance
-   `smoker`: 1 if the person is a smoker, 0 otherwise
-   `region`: Categorical feature indicating the person's region
-   `female`, `male`: One-hot encoded gender features
-   `charges`: The target variable (medical insurance cost)

---

## 3. Exploratory Data Analysis (EDA)

I conducted the following analyses:

-   **Data Cleaning:** No missing values Ire found.
-   **Feature Distribution:**
    -   Charges Ire **right-skeId** (many low values, feIr high ones).
    -   BMI had a **normal distribution**.
    -   Smokers had significantly higher charges than non-smokers.
-   **Correlations:**
    -   `smoker` had the highest positive correlation with `charges`.
    -   `bmi` and `age` also had moderate correlations with `charges`.
    -   `region` had almost no impact on charges.

**Key Insights:**

-   Smokers pay much higher medical insurance costs.
-   BMI and age influence costs but not as significantly as smoking.
-   The number of children doesn’t strongly affect charges.

---

## 4. Model Development

### **Baseline Model: Linear Regression**

-   I started with a simple **linear regression model**, which gave moderate performance but failed to capture non-linear relationships.

### **Polynomial Regression with Cross-Validation**

-   I applied **polynomial features** to improve the model.
-   I tested different **degrees (1 to 9)** with varying **k-fold cross-validation splits (5 to 10 folds)**.
-   The best model achieved **R² = 84.1%** with **degree 3 and 5-fold CV**.

### **Ridge Regression (Regularization)**

-   To improve generalization, I applied **Ridge Regression** with hyperparameter tuning.
-   I tested **different alpha values (0.1, 1, 10, 100, 1000)** using **GridSearchCV**.
-   The best model gave the **same performance (84.1%)**, confirming no significant overfitting.

---

## 5. Final Model Selection

I saved the best-performing **Ridge Regression model** with polynomial features as the final model using `joblib`:

```python
import joblib
joblib.dump(grid_search.best_estimator_, 'final_model.pkl')
```

To **load and use** the model for prediction on new data:

```python
model = joblib.load('final_model.pkl')
new_data = [[25, 30.5, 3, 0, 1, 1, 0]]  # Example input
prediction = model.predict(new_data)
print("Predicted Charges:", prediction[0])
```

---

## 6. Results & Insights

### **Model Performance:**

-   **Final Model:** Ridge Regression with Polynomial Features (Degree = 3)
-   **R² Score:** 84.1%
-   **Mean Squared Error (MSE):** Calculated and validated

### **Key Business Insights:**

1. **Smokers have significantly higher insurance costs**, making smoking status a key predictor.
2. **BMI and age influence charges**, meaning healthier lifestyle habits may reduce costs.
3. **The number of children has minimal impact on charges**, showing that insurance rates are not heavily dependent on dependents.
4. **Regularization (Ridge Regression) did not improve performance**, confirming that the polynomial model was already Ill-generalized.

---

## 7. Conclusion & Next Steps

-   I successfully built a **highly predictive model** for insurance charges (**84.1% accuracy**).
-   The model is now ready for deployment and can be used to **predict charges for new customers**.
-   Future improvements could include **feature engineering (e.g., interaction terms)** and **testing ensemble models** like Random Forest or Gradient Boosting for potentially better performance.

---

## 8. Portfolio & Deployment

-   The final model is saved as `final_model.pkl` and can be used for **real-time predictions**.
-   This report can be included in a **portfolio** to showcase **data analysis, model tuning, and deployment skills**.

🚀 **Project Complete!** 🎯
