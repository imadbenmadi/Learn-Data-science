## **📌 Subqueries & CTEs (Common Table Expressions) in MySQL**  
Both **subqueries** and **CTEs** help break down complex queries by using temporary results inside a larger query.  

---

# **1️⃣ Subqueries in MySQL**
A **subquery** is a query inside another query, enclosed in parentheses `()`.  
Subqueries can be used in **`SELECT`**, **`FROM`**, or **`WHERE`** clauses.

---

### **📌 1.1 Scalar Subquery (Returns a Single Value)**
A **scalar subquery** returns **only one value (one row, one column)**.  

```sql
SELECT name, salary 
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```
✅ **Finds the employee with the highest salary.**  
✅ The subquery `(SELECT MAX(salary) FROM employees)` **returns one value**.

### **📝 Example Result:**
| name | salary |
|------|--------|
| Bob  | 60000 |

---

### **📌 1.2 Multi-Row Subquery (Returns Multiple Rows)**
A **multi-row subquery** returns **multiple rows**, usually inside `IN`, `ANY`, or `ALL` operators.  

```sql
SELECT name, department, salary
FROM employees
WHERE department IN (SELECT department FROM departments WHERE location = 'New York');
```
✅ **Finds employees in New York-based departments**.

---

### **📌 1.3 Correlated Subquery (Depends on Outer Query)**
A **correlated subquery** runs **once for each row in the outer query**.  

```sql
SELECT name, salary
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e1.department = e2.department);
```
✅ **Finds employees earning above their department’s average salary**.  
🚀 **Slower** than normal subqueries because it runs for each row.

---

# **2️⃣ CTEs (Common Table Expressions)**
A **CTE** (`WITH` clause) is a **temporary query result** that can be referenced multiple times in the main query.  
✅ **More readable** than subqueries.  
✅ **Can be recursive** for hierarchical data (e.g., categories, org charts).  

### **📌 2.1 Simple CTE (Reusable Temporary Query)**
```sql
WITH HighEarners AS (
    SELECT name, salary FROM employees WHERE salary > 50000
)
SELECT * FROM HighEarners;
```
✅ **Filters high earners and reuses the result in the main query**.  
✅ **Easier to read & maintain** than a subquery.

---

### **📌 2.2 Recursive CTE (For Hierarchical Data)**
Used for **self-referencing tables** (e.g., employee-manager relationships).

```sql
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT id, name, manager_id
    FROM employees
    WHERE manager_id IS NULL  -- Get top-level boss

    UNION ALL

    SELECT e.id, e.name, e.manager_id
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM EmployeeHierarchy;
```
✅ **Finds all employees reporting to the top-level boss.**  
✅ **Each recursive step finds employees under the previous level**.

---

## **🚀 Subqueries vs CTEs: When to Use?**
| Feature | Subqueries | CTEs |
|---------|-----------|------|
| Use in `SELECT`, `FROM`, `WHERE` | ✅ Yes | ✅ Yes |
| Readability | ❌ Harder | ✅ Easier |
| Performance | 🚀 Faster for simple cases | ✅ Better for complex queries |
| Recursive Queries | ❌ No | ✅ Yes |

---

### **🔥 Best Practice:**
- Use **subqueries** for **one-time calculations**.
- Use **CTEs** for **reusable & complex queries**.
- Use **recursive CTEs** for **hierarchical relationships**.

Do you want an example for **optimizing a query with CTEs**? 🚀