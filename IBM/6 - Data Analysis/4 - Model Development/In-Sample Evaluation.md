### **In-Sample Evaluation Measures – Explained**

In-sample evaluation is when we assess how well our model is performing **on the same data** it was trained on. This gives us an idea of how well the model fits the training data, but it doesn’t necessarily tell us about its generalization ability (i.e., how well it will perform on unseen data). Despite this limitation, **in-sample evaluation** is important because it helps us **identify overfitting** and **fine-tune the model**.

Here are some **key measures** for evaluating in-sample performance:

---

### **1️⃣ Mean Absolute Error (MAE)**

-   **Definition:** MAE calculates the **average of the absolute differences** between predicted values and actual values.
-   **Formula:**  
    \[
    MAE = \frac{1}{n} \sum\_{i=1}^{n} |y_i - \hat{y}\_i|
    \]
    Where:

    -   \(y_i\) = Actual value
    -   \(\hat{y}\_i\) = Predicted value
    -   \(n\) = Number of data points

-   **Interpretation:**
    -   MAE is easy to understand.
    -   It gives us the **average error in the same units** as the original data.
    -   **Lower MAE** indicates a better fit.

---

### **2️⃣ Mean Squared Error (MSE)**

-   **Definition:** MSE is similar to MAE but squares the error before averaging. This means it penalizes **larger errors** more.
-   **Formula:**  
    \[
    MSE = \frac{1}{n} \sum\_{i=1}^{n} (y_i - \hat{y}\_i)^2
    \]
-   **Interpretation:**
    -   **Sensitive to large errors**. A few outliers will significantly increase the MSE.
    -   It **measures variance**, making it suitable for finding models that overfit or underfit the data.
    -   **Lower MSE** means a better fit, but it can be misleading if there are outliers.

---

### **3️⃣ Root Mean Squared Error (RMSE)**

-   **Definition:** RMSE is simply the **square root of MSE**. It brings the error measure back to the **original units** of the data (like MAE).
-   **Formula:**  
    \[
    RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum\_{i=1}^{n} (y_i - \hat{y}\_i)^2}
    \]
-   **Interpretation:**
    -   RMSE is **sensitive to large errors**, similar to MSE.
    -   **Lower RMSE** indicates a better model.
    -   Since RMSE is in the same units as the target variable, it's easier to interpret than MSE.

---

### **4️⃣ R-squared (R²)**

-   **Definition:** R² is a **proportion of the variance** in the dependent variable that is explained by the independent variables.
-   **Formula:**  
    \[
    R^2 = 1 - \frac{\sum (y_i - \hat{y}\_i)^2}{\sum (y_i - \bar{y})^2}
    \]
    Where:
    -   \(\bar{y}\) = Mean of actual values
    -   \(y_i\) = Actual value
    -   \(\hat{y}\_i\) = Predicted value
-   **Interpretation:**
    -   R² gives an idea of how much of the data variance is explained by the model.
    -   **Values between 0 and 1**.
    -   **Higher R²** means the model explains more of the variance.
    -   **R² = 1** means perfect fit.
    -   **R² = 0** means the model does no better than predicting the mean of the target variable.
    -   **Negative R²** can occur when the model performs worse than a simple mean-based model (i.e., a very poor fit).

---

### **5️⃣ Adjusted R-squared (Adjusted R²)**

-   **Definition:** Adjusted R² adjusts the R² value based on the number of features in the model. It accounts for **overfitting** by penalizing the inclusion of too many variables.
-   **Formula:**  
    \[
    \text{Adjusted } R^2 = 1 - \left(1 - R^2 \right) \times \frac{n - 1}{n - p - 1}
    \]
    Where:

    -   \(n\) = Number of data points
    -   \(p\) = Number of independent variables (features)

-   **Interpretation:**
    -   Adjusted R² is a more reliable measure when comparing models with different numbers of features.
    -   **Higher Adjusted R²** means a better model (compared to other models with more features).

---

### **6️⃣ Mean Absolute Percentage Error (MAPE)**

-   **Definition:** MAPE calculates the **average percentage error** between actual and predicted values.
-   **Formula:**  
    \[
    MAPE = \frac{1}{n} \sum\_{i=1}^{n} \left|\frac{y_i - \hat{y}\_i}{y_i}\right| \times 100
    \]
-   **Interpretation:**
    -   MAPE is good for understanding **how much error** is happening as a percentage of the actual value.
    -   However, it **cannot be used with zero values** in the data (it becomes undefined).
    -   **Lower MAPE** means a better model.

---

### **7️⃣ Explained Variance Score**

-   **Definition:** Measures the proportion of variance explained by the model, similar to \(R^2\), but it’s used when **the target values are continuous**.
-   **Formula:**  
    \[
    \text{Explained Variance} = 1 - \frac{\text{Var}(y - \hat{y})}{\text{Var}(y)}
    \]
-   **Interpretation:**
    -   **Higher Explained Variance** means the model has captured more of the target variable’s variance.

---

### **Summary of In-Sample Measures**

-   **MAE**: Simple, interpretable error measure.
-   **MSE & RMSE**: Penalize larger errors more.
-   **R² & Adjusted R²**: Measure how well the model fits and generalizes.
-   **MAPE**: Expresses error as a percentage.
-   **Explained Variance**: Measures how much of the target variance is explained.

---

### **When to Use These Measures?**

-   **MAE**: When you want a simple, intuitive measure of error.
-   **MSE/RMSE**: When you want to **penalize large errors**.
-   **R²**: To see the **proportion of variance** explained.
-   **Adjusted R²**: When comparing models with different numbers of features.
-   **MAPE**: When you want the error in percentage terms, especially for financial or business-related problems.

---

Bro, these measures will help you evaluate your model's **performance on the training data**. They give insights into **how well the model is fitting the data** and help decide if any adjustments are needed, like **tuning hyperparameters** or **preventing overfitting**. Let me know if you need more details on any of these! 😎
