### 1. **Linear Regression (LR)**
Linear Regression is a supervised learning algorithm used for predicting a continuous value based on an independent variable. It assumes a linear relationship between the dependent variable (Y) and the independent variable (X).

#### **Equation:**
\[
Y = b_0 + b_1X + \epsilon
\]
Where:
- \( Y \) = Target variable  
- \( X \) = Independent variable  
- \( b_0 \) = Intercept  
- \( b_1 \) = Slope (coefficient of \( X \))  
- \( \epsilon \) = Error term  

#### **Use Case:**
- Predicting house prices based on square footage.
- Estimating sales revenue based on advertising expenses.

---

### 2. **Multiple Linear Regression (MLR)**
When there are multiple independent variables, it becomes **Multiple Linear Regression**.

#### **Equation:**
\[
Y = b_0 + b_1X_1 + b_2X_2 + ... + b_nX_n + \epsilon
\]

Where:
- \( X_1, X_2, ..., X_n \) are multiple independent variables.

#### **Use Case:**
- Predicting car price based on engine size, mileage, and brand.
- Forecasting student grades based on study hours, past scores, and sleep hours.

---

### 3. **Residual Plot**
A **residual plot** is used to check if Linear Regression is a good fit for the data.

#### **Residuals:**
\[
Residual = Actual\ Value - Predicted\ Value
\]

A **good residual plot** should show random scatter around zero.  

**Key Points:**
- **Randomly scattered residuals** → Linear regression is a good fit.
- **Pattern in residuals (U-shape or increasing variance)** → LR might not be the best choice.

---

### 4. **When NOT to Use Linear Regression**
- **Non-linear relationships**: If the data shows curves or complex patterns.
- **High multicollinearity**: When independent variables are highly correlated.
- **Heteroscedasticity**: If residual variance increases/decreases over time.
- **Outliers**: If there are extreme outliers that affect the regression line significantly.

Would you like a code example for any of these? 🚀