# **Pivot Tables & Dynamic Pivots**

## **What is a Pivot Table?**

-   **Transforms rows into columns**.
-   Summarizes data **in a structured format**.
-   Commonly used for **reporting & analytics**.

✅ **Key Features**:

-   Aggregates data **dynamically**.
-   Used for **sales reports, inventory, finance, etc.**.
-   Works well with **SUM, COUNT, AVG**.

---

## **Real-World Example: Monthly Sales Report**

### **📊 Scenario**:

Your company tracks **monthly sales per department**. You want to **display data in a pivot table format**.

### **🛠️ Table: `sales`**

| department  | month    | total_sales |
| ----------- | -------- | ----------- |
| Electronics | January  | 50000       |
| Clothing    | January  | 30000       |
| Grocery     | January  | 20000       |
| Electronics | February | 55000       |
| Clothing    | February | 28000       |
| Grocery     | February | 22000       |

---

### **🎯 Goal**: Convert rows into **a pivot table with months as columns**.

```sql
SELECT
    department,
    SUM(CASE WHEN month = 'January' THEN total_sales ELSE 0 END) AS January,
    SUM(CASE WHEN month = 'February' THEN total_sales ELSE 0 END) AS February
FROM sales
GROUP BY department;
```

### **🔍 Output**

| department  | January | February |
| ----------- | ------- | -------- |
| Electronics | 50000   | 55000    |
| Clothing    | 30000   | 28000    |
| Grocery     | 20000   | 22000    |

📌 Now you have a **clean monthly sales report**!

---

## **🔥 Dynamic Pivot Tables (When You Don't Know the Months in Advance)**

If months **change dynamically**, you need a **Dynamic Pivot**.

### **Dynamic Pivot Example**

```sql
SET @sql = NULL;
SELECT
    GROUP_CONCAT(DISTINCT
        CONCAT('SUM(CASE WHEN month = ''', month, ''' THEN total_sales ELSE 0 END) AS `', month, '`')
    ) INTO @sql
FROM sales;

SET @sql = CONCAT('SELECT department, ', @sql, ' FROM sales GROUP BY department;');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

✅ **What This Does**:

1. **Dynamically fetches all months** from the table.
2. **Generates a SQL query** to pivot based on available months.
3. **Executes the pivot query**.

📌 Now your query **automatically adjusts to new months!** 🚀

---

## **💡 Summary**

-   **Pivot Tables** turn **rows into columns**.
-   **Static Pivot** → Use `CASE WHEN` for known values.
-   **Dynamic Pivot** → Uses `GROUP_CONCAT()` to handle **unknown values**.
-   Commonly used in **reporting, dashboards, financial summaries**.
