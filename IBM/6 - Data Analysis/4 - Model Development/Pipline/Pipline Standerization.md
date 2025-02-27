### **What Does "Zero Mean and Unit Variance" Mean?**

When you **standardize** data using `StandardScaler()`, it transforms each feature to have:

✅ **Mean (Average) = 0**  
✅ **Variance (Spread) = 1**

---

### **Mathematical Formula:**

For each feature \( X \), the standardized value \( X\_{\text{scaled}} \) is calculated as:

\[
X\_{\text{scaled}} = \frac{X - \mu}{\sigma}
\]

Where:

-   \( X \) = Original value
-   \( \mu \) = Mean of the feature
-   \( \sigma \) = Standard deviation of the feature

---

### **Why Do This?**

🔹 Some models (like **linear regression** and **polynomial regression**) perform **better when features are on the same scale**.  
🔹 Prevents **dominant influence** from large-scale features (e.g., weight in kg vs. price in dollars).  
🔹 Helps **faster and stable training** of machine learning models.

---

### **Example Before and After Standardization**

| Feature (Horsepower) | Before Standardization | After Standardization |
| -------------------- | ---------------------- | --------------------- |
| 100                  | 100                    | -0.85                 |
| 200                  | 200                    | 1.65                  |
| 150                  | 150                    | 0.40                  |

Here, `StandardScaler()` shifts all values to have a **mean of 0** and **variance of 1**.
