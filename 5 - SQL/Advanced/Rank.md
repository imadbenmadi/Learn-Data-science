# **RANK() & DENSE_RANK() – Ranking Within Partitions**

## **What Are RANK() & DENSE_RANK()?**

Both functions **assign a rank** to rows based on a specified order.

-   **`RANK()`**: If two rows have the same value, they get the **same rank**, but the next rank **skips numbers**.
-   **`DENSE_RANK()`**: Similar to `RANK()`, but it **does not skip numbers** after a tie.

✅ **Key Features**:

-   `RANK()` leaves gaps in rankings.
-   `DENSE_RANK()` keeps ranks consecutive.
-   Both are useful for leaderboards, competitions, and ranking scenarios.

---

## **Real-World Example: Employee Sales Ranking**

### **👨‍💼 Scenario**:

You run a company and want to rank employees based on their **monthly sales performance**.

### **🛠️ Table: `sales`**

| employee_id | name    | sales_amount |
| ----------- | ------- | ------------ |
| 1           | Alice   | 5000         |
| 2           | Bob     | 7000         |
| 3           | Charlie | 7000         |
| 4           | David   | 4000         |
| 5           | Emma    | 6000         |

---

### **🎯 Goal**: Rank employees based on `sales_amount`.

```sql
SELECT
    employee_id,
    name,
    sales_amount,
    RANK() OVER (ORDER BY sales_amount DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY sales_amount DESC) AS dense_rank
FROM sales;
```

### **🔍 Output**

| employee_id | name    | sales_amount | RANK | DENSE_RANK |
| ----------- | ------- | ------------ | ---- | ---------- |
| 2           | Bob     | 7000         | 1    | 1          |
| 3           | Charlie | 7000         | 1    | 1          |
| 5           | Emma    | 6000         | 3    | 2          |
| 1           | Alice   | 5000         | 4    | 3          |
| 4           | David   | 4000         | 5    | 4          |

---

## **Breaking Down the Output**

1. **Bob & Charlie have the same sales (7000)**:
    - `RANK() = 1`, but the next rank is **3** (it skips 2).
    - `DENSE_RANK() = 1`, and the next rank is **2** (no skip).
2. **Emma (6000 sales) gets rank 3 in `RANK()`, but 2 in `DENSE_RANK()`**.
3. **Alice (5000 sales) gets rank 4 in `RANK()`, but 3 in `DENSE_RANK()`**.

---

## **📌 When to Use RANK() vs. DENSE_RANK()**

-   **Use `RANK()`** when you want to show **real ranking positions with gaps** (e.g., in sports tournaments).
-   **Use `DENSE_RANK()`** when you want **continuous rankings without gaps** (e.g., grouping employees into salary grades).

---

## **🔥 Practical Use Case: Get the Top 3 Employees**

Want to **list the top 3 employees** based on sales?

```sql
WITH RankedSales AS (
    SELECT
        employee_id,
        name,
        sales_amount,
        RANK() OVER (ORDER BY sales_amount DESC) AS rank
    FROM sales
)
SELECT * FROM RankedSales WHERE rank <= 3;
```

### **🛠️ Output**

| employee_id | name    | sales_amount | rank |
| ----------- | ------- | ------------ | ---- |
| 2           | Bob     | 7000         | 1    |
| 3           | Charlie | 7000         | 1    |
| 5           | Emma    | 6000         | 3    |

👉 This ensures that **if two employees tie at rank 1, both are included**.

---

## **💡 Summary**

-   `RANK()` **skips numbers** after a tie.
-   `DENSE_RANK()` **keeps ranking consecutive**.
-   Use `RANK()` for **competitions**, `DENSE_RANK()` for **salary levels, leaderboards, etc.**.

---
