Materialized views are like normal views but with stored, precomputed data, making queries much faster. Here’s a breakdown:

### **1. What are Materialized Views?**

A **Materialized View** is a database object that stores the result of a query physically, unlike a regular view which just represents a query dynamically. This improves **performance** for expensive queries.

### **2. Creating & Updating Views**

-   **Regular View**: Does not store data, just represents a query dynamically.
    ```sql
    CREATE VIEW my_view AS
    SELECT name, salary FROM employees WHERE salary > 5000;
    ```
-   **Materialized View**: Stores the result for faster access.
    ```sql
    CREATE MATERIALIZED VIEW my_mat_view AS
    SELECT name, salary FROM employees WHERE salary > 5000;
    ```
    -   Unlike regular views, **materialized views need to be refreshed** to get updated data.

### **3. Updatable Views vs. Read-Only Views**

-   **Updatable View**: You can perform `INSERT`, `UPDATE`, and `DELETE` if the view is based on a single table with a primary key.
    ```sql
    CREATE VIEW my_updatable_view AS
    SELECT id, name FROM employees;
    ```
    -   You can do:
        ```sql
        UPDATE my_updatable_view SET name = 'John' WHERE id = 1;
        ```
-   **Read-Only View**: If a view is based on **multiple tables or complex joins**, it is **not updatable**.
    ```sql
    CREATE VIEW my_read_only AS
    SELECT emp.name, dep.department_name
    FROM employees emp JOIN departments dep
    ON emp.dep_id = dep.id;
    ```
    -   You **CANNOT** do `UPDATE`, `INSERT`, or `DELETE` here.

### **4. Materialized Views: Precomputed Data for Performance**

-   Used for **fast reads** and reducing expensive computations.
-   Needs **manual or scheduled refresh**:
    ```sql
    REFRESH MATERIALIZED VIEW my_mat_view;
    ```
-   Can be **fully refreshed** (drop and recalculate) or **incrementally refreshed** (update only changed data).

### **Materialized Views in MySQL (Real Use Cases)**
Unlike PostgreSQL or Oracle, MySQL **does not natively support materialized views**, but you can simulate them using **tables + triggers/events**.

### **1. What is a Materialized View?**
A **Materialized View** stores precomputed query results in a table for **faster reads** instead of recalculating on every request.

### **2. Real Use Cases**
#### **🔹 Example 1: Speeding Up Complex Aggregations**  
If you frequently calculate **total sales per month**, instead of querying a large `orders` table each time:
```sql
CREATE TABLE materialized_sales AS 
SELECT MONTH(order_date) AS month, SUM(total_price) AS total_sales 
FROM orders 
GROUP BY month;
```
👉 Faster reporting without scanning millions of rows.

#### **🔹 Example 2: Precomputed Joins for Fast Analytics**  
Joining large tables repeatedly is slow. Instead:
```sql
CREATE TABLE materialized_employee_stats AS 
SELECT e.id, e.name, d.department_name, COUNT(p.project_id) AS project_count
FROM employees e 
JOIN departments d ON e.dep_id = d.id 
LEFT JOIN projects p ON e.id = p.emp_id
GROUP BY e.id;
```
👉 Quickly fetch pre-aggregated data.

### **3. Keeping It Updated**
Since MySQL lacks built-in refresh, use:
- **Triggers:** Update the materialized table when data changes.
- **Events:** Refresh periodically.

#### **Automatic Refresh Using Events (Every 1 Hour)**
```sql
CREATE EVENT refresh_materialized_sales
ON SCHEDULE EVERY 1 HOUR
DO 
REPLACE INTO materialized_sales 
SELECT MONTH(order_date) AS month, SUM(total_price) AS total_sales 
FROM orders 
GROUP BY month;
```
👉 Keeps data fresh without manual intervention.

### **Key Takeaways**
✔ **Boosts query performance** by avoiding expensive joins & aggregations.  
✔ **Requires manual updates** via triggers/events.  
✔ **Best for reporting & analytics** where real-time updates aren’t needed.

