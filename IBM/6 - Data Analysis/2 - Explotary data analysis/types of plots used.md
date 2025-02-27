### **Plots for Descriptive Analytics**

#### **1️⃣ Categorical Data (Discrete)**

Used for **count-based analysis** (e.g., gender, product categories, etc.).

-   **Bar Plot** → `sns.countplot(x=df["category"])` (Counts per category)
-   **Pie Chart** → `df["category"].value_counts().plot.pie()` (Proportions of categories)
-   **Box Plot** → `sns.boxplot(x="category", y="value", data=df)` (Distribution across categories)

#### **2️⃣ Numerical Data (Continuous)**

Used to show **distributions and trends** (e.g., age, salary, sales).

-   **Histogram** → `df["column"].hist(bins=20)` (Distribution of values)
-   **Box Plot** → `sns.boxplot(y=df["column"])` (Outliers & spread)
-   **Violin Plot** → `sns.violinplot(y=df["column"])` (Density + Box Plot)
-   **Scatter Plot** → `sns.scatterplot(x="num1", y="num2", data=df)` (Relationship between two numerical variables)

💡 **Summary:**

-   **Categorical → Bar, Pie, Box Plot**
-   **Numerical → Histogram, Box, Violin, Scatter**
