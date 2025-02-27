Nice! Now let’s tackle **NTILE()**, which helps split data into equal-sized groups. After that, we’ll move on to **Pivot Tables & Dynamic Pivots**.

---

# **4. NTILE() – Splitting Data into Equal-Sized Groups**

## **What is NTILE()?**

-   **NTILE(N)** → Divides rows into **N equal-sized groups**.
-   Each group gets a **group number from 1 to N**.
-   Used for **percentiles, quartiles, and ranking distribution**.

✅ **Key Features**:

-   Helps **categorize data** (e.g., top 25%, middle 50%, bottom 25%).
-   Useful for **salary distribution, student grades, or customer segmentation**.

---

## **Real-World Example: Employee Performance Quartiles**

### **📊 Scenario**:

Your company wants to **divide employees into 4 performance levels** based on sales.

### **🛠️ Table: `sales`**

| employee_id | name    | sales_amount |
| ----------- | ------- | ------------ |
| 1           | Alice   | 9000         |
| 2           | Bob     | 8000         |
| 3           | Charlie | 7000         |
| 4           | David   | 6000         |
| 5           | Emma    | 5000         |
| 6           | Frank   | 4000         |
| 7           | Grace   | 3000         |
| 8           | Henry   | 2000         |

---

### **🎯 Goal**: Divide employees into **4 quartiles** based on sales.

```sql
SELECT
    employee_id,
    name,
    sales_amount,
    NTILE(4) OVER (ORDER BY sales_amount DESC) AS quartile
FROM sales;
```

### **🔍 Output**

| employee_id | name    | sales_amount | quartile |
| ----------- | ------- | ------------ | -------- |
| 1           | Alice   | 9000         | 1        |
| 2           | Bob     | 8000         | 1        |
| 3           | Charlie | 7000         | 2        |
| 4           | David   | 6000         | 2        |
| 5           | Emma    | 5000         | 3        |
| 6           | Frank   | 4000         | 3        |
| 7           | Grace   | 3000         | 4        |
| 8           | Henry   | 2000         | 4        |

---

## **Breaking Down the Output**

-   Employees are **divided into 4 quartiles**.
-   **Top performers (Q1)**: Alice & Bob.
-   **Lowest performers (Q4)**: Grace & Henry.

---

## **🔥 Practical Use Case: Targeting the Top 25% Performers**

Want to **select only the top quartile** (Q1)?

```sql
WITH RankedSales AS (
    SELECT
        employee_id,
        name,
        sales_amount,
        NTILE(4) OVER (ORDER BY sales_amount DESC) AS quartile
    FROM sales
)
SELECT * FROM RankedSales WHERE quartile = 1;
```

### **🛠️ Output**

| employee_id | name  | sales_amount | quartile |
| ----------- | ----- | ------------ | -------- |
| 1           | Alice | 9000         | 1        |
| 2           | Bob   | 8000         | 1        |

📌 Now you can **reward the top 25% employees**! 🚀

---

## **💡 Summary**

-   `NTILE(N)` splits rows into **N groups**.
-   Used for **percentiles, quartiles, and ranking-based analysis**.
-   Great for **salary ranges, performance groups, customer segmentation, etc.**.
