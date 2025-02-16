### **What Does P-Value Mean in Data Science?**

The **p-value** is a statistical measure that tells you how significant a variable is in your model. It helps you decide whether a feature (independent variable) has a real impact on the target variable.

### **Key Concept:**

-   A **low p-value** (typically **< 0.05**) means the variable is **statistically significant** → It has a strong effect on the target variable.
-   A **high p-value** (typically **> 0.05**) means the variable is **not significant** → It might be just noise.

### **Example: CPU Frequency & Price Prediction**

If you're predicting **laptop prices** and see that **CPU_frequency** has the **lowest p-value**, it means:  
✅ **CPU frequency is the most important feature** affecting laptop prices.  
❌ If another feature (e.g., "Number of USB Ports") has a high p-value, it means it's **not useful** for price prediction.

### **TL;DR:**

-   **Low p-value** = The feature is important. ✅
-   **High p-value** = The feature is not useful. ❌
-   Always **remove features with high p-values** to improve your model! 🚀
