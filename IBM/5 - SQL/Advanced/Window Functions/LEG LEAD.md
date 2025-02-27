# **LEAD() & LAG() – Accessing Previous/Next Rows**

## **What Are LEAD() & LAG()?**

-   **`LAG(column, N)`** → Gets the **previous** row value (N steps back).
-   **`LEAD(column, N)`** → Gets the **next** row value (N steps forward).
-   Default `N = 1` (i.e., the **immediate** previous or next row).
-   Useful for **comparing consecutive rows** (e.g., price changes, sales trends).

✅ **Key Features**:

-   Helps analyze **trends** (e.g., if sales increased or decreased).
-   Useful in **time-series data** (e.g., comparing yesterday vs. today).
-   Works with **PARTITION BY** to reset calculations for each group.

---

## **Real-World Example: Stock Price Changes**

### **📈 Scenario**:

You have a table of stock prices for a company and want to compare each day’s price to the previous day’s and the next day’s price.

### **🛠️ Table: `stock_prices`**

| stock_id | stock_date | price |
| -------- | ---------- | ----- |
| 1        | 2024-02-01 | 100   |
| 2        | 2024-02-02 | 105   |
| 3        | 2024-02-03 | 102   |
| 4        | 2024-02-04 | 110   |
| 5        | 2024-02-05 | 108   |

---

### **🎯 Goal**: Compare each day’s price with the previous and next day.

```sql
SELECT
    stock_date,
    price,
    LAG(price) OVER (ORDER BY stock_date) AS previous_day_price,
    LEAD(price) OVER (ORDER BY stock_date) AS next_day_price
FROM stock_prices;
```

### **🔍 Output**

| stock_date | price | previous_day_price | next_day_price |
| ---------- | ----- | ------------------ | -------------- |
| 2024-02-01 | 100   | NULL               | 105            |
| 2024-02-02 | 105   | 100                | 102            |
| 2024-02-03 | 102   | 105                | 110            |
| 2024-02-04 | 110   | 102                | 108            |
| 2024-02-05 | 108   | 110                | NULL           |

---

## **Breaking Down the Output**

-   **First row**: No previous price (`NULL`).
-   **Last row**: No next price (`NULL`).
-   Each row **compares with the previous and next day**.

---

## **🔥 Practical Use Case: Identifying Stock Price Drops**

Want to find the days when the stock **dropped compared to the previous day**?

```sql
WITH PriceChanges AS (
    SELECT
        stock_date,
        price,
        LAG(price) OVER (ORDER BY stock_date) AS previous_day_price
    FROM stock_prices
)
SELECT * FROM PriceChanges WHERE price < previous_day_price;
```

### **🛠️ Output**

| stock_date | price | previous_day_price |
| ---------- | ----- | ------------------ |
| 2024-02-03 | 102   | 105                |
| 2024-02-05 | 108   | 110                |

📉 This shows that the price **dropped on Feb 3 and Feb 5**.

---

## **📌 When to Use LEAD() & LAG()**

-   **LAG()** → Compare with previous row (e.g., sales last month vs. this month).
-   **LEAD()** → Compare with next row (e.g., today’s sales vs. tomorrow’s expected sales).
-   Use in **trend analysis, financial data, and sequential comparisons**.

---

## **💡 Summary**

-   `LAG()` gets the **previous row** value.
-   `LEAD()` gets the **next row** value.
-   Both are **powerful for analyzing trends and comparisons**.
