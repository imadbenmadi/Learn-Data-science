### **🚀 Pagination in SQL: How to Efficiently Handle Large Datasets**

Pagination is used to **split large datasets into smaller chunks (pages)** so that users can navigate through them efficiently. It is commonly used in **web applications** for displaying **search results, product listings, chat messages**, etc.

---

## **1️⃣ Basic Pagination with `LIMIT` & `OFFSET`**

Most databases like MySQL, PostgreSQL, and SQLite use **`LIMIT` and `OFFSET`** for pagination.

### **📌 Syntax:**

```sql
SELECT columns
FROM table
ORDER BY column
LIMIT page_size OFFSET (page_number - 1) * page_size;
```

### **Example Table: `employees`**

| id  | name    | department | salary |
| --- | ------- | ---------- | ------ |
| 1   | Alice   | HR         | 50000  |
| 2   | Bob     | IT         | 60000  |
| 3   | Charlie | IT         | 55000  |
| 4   | David   | Sales      | 48000  |
| 5   | Eve     | HR         | 52000  |
| 6   | Frank   | IT         | 58000  |

### **📌 Example: Page 2 (Showing 2 Employees per Page)**

```sql
SELECT * FROM employees
ORDER BY id ASC
LIMIT 2 OFFSET (2 - 1) * 2;
```

### **💡 Query Breakdown:**

-   `LIMIT 2` → Show **2 records per page**.
-   `OFFSET (2 - 1) * 2 = 2` → Skip **first 2 rows** (Page 1).
-   **Page 1** → `LIMIT 2 OFFSET 0`
-   **Page 2** → `LIMIT 2 OFFSET 2`
-   **Page 3** → `LIMIT 2 OFFSET 4`

### **📝 Output (Page 2)**

| id  | name    | department | salary |
| --- | ------- | ---------- | ------ |
| 3   | Charlie | IT         | 55000  |
| 4   | David   | Sales      | 48000  |

---

## **2️⃣ Pagination in SQL Server (`OFFSET FETCH`)**

SQL Server doesn’t support `LIMIT`, so use `OFFSET` and `FETCH NEXT` instead:

```sql
SELECT * FROM employees
ORDER BY id
OFFSET 2 ROWS FETCH NEXT 2 ROWS ONLY;
```

-   **Skips 2 rows** and **fetches the next 2**.
-   Works the same way as `LIMIT OFFSET`.

---

## **3️⃣ Efficient Pagination with `WHERE` Instead of `OFFSET`**

⚠️ `OFFSET` becomes slow on **large datasets** because it still scans all previous rows. Instead, use **key-based pagination** with `WHERE` for better performance.

### **📌 Optimized Query Using `WHERE`**

```sql
SELECT * FROM employees
WHERE id > 2  -- Fetch only rows after ID 2
ORDER BY id ASC
LIMIT 2;
```

✅ Faster because it **uses an index** on `id` instead of skipping rows.  
✅ Ideal for **infinite scrolling** (like Twitter, Facebook feeds).

---

## **4️⃣ Counting Total Pages for Frontend Pagination**

To show **total pages**, count all rows first:

```sql
SELECT COUNT(*) AS total_records FROM employees;
```

### **📝 Example Result:**

| total_records |
| ------------- |
| 6             |

👉 **Total Pages Calculation (Frontend)**

```js
const totalPages = Math.ceil(total_records / page_size);
```

For `page_size = 2`:  
`total_pages = Math.ceil(6 / 2) = 3`

---

## **5️⃣ Example: Implementing Pagination in a Web App**

### **Backend API (Node.js + MySQL)**

```js
app.get("/employees", async (req, res) => {
    const page = parseInt(req.query.page) || 1; // Default page 1
    const pageSize = 2; // Show 2 records per page
    const offset = (page - 1) * pageSize;

    const [results] = await db.execute(
        `
        SELECT * FROM employees
        ORDER BY id ASC
        LIMIT ? OFFSET ?
    `,
        [pageSize, offset]
    );

    res.json({ page, pageSize, data: results });
});
```

### **Frontend API Call (React)**

```js
const fetchEmployees = async (page) => {
    const res = await fetch(`/employees?page=${page}`);
    const data = await res.json();
    setEmployees(data.data);
};
```

---

## **🚀 Best Practices for Pagination**

✅ **Use `LIMIT OFFSET` for small datasets** (<100k rows).  
✅ **Use `WHERE id > last_seen_id` for large datasets** (infinite scroll).  
✅ **Count total records (`COUNT(*)`) for total pages.**  
✅ **Always use `ORDER BY` to ensure consistent results.**
---
---
---

# **📌 Pagination in MySQL**
In MySQL, use `LIMIT` and `OFFSET` to paginate results efficiently.

#### **Basic Syntax**
```sql
SELECT * FROM table_name
ORDER BY column_name
LIMIT page_size OFFSET (page_number - 1) * page_size;
```

---

### **Example Table: `employees`**
| id | name  | department | salary |
|----|-------|-----------|--------|
| 1  | Alice | HR        | 50000  |
| 2  | Bob   | IT        | 60000  |
| 3  | Charlie | IT     | 55000  |
| 4  | David | Sales     | 48000  |
| 5  | Eve   | HR        | 52000  |
| 6  | Frank | IT       | 58000  |

---

### **📌 Page 2 (Showing 2 Employees per Page)**
```sql
SELECT * FROM employees
ORDER BY id ASC
LIMIT 2 OFFSET (2 - 1) * 2;
```
### **Output (Page 2)**
| id | name    | department | salary |
|----|--------|-----------|--------|
| 3  | Charlie | IT        | 55000  |
| 4  | David   | Sales     | 48000  |

---

### **🔥 Optimized Pagination (Key-Based)**
Avoid slow `OFFSET` by filtering with `WHERE`:
```sql
SELECT * FROM employees
WHERE id > 2  -- Fetch only rows after ID 2
ORDER BY id ASC
LIMIT 2;
```
✅ Faster on large datasets 🚀

---

### **📝 Count Total Records**
To calculate total pages:
```sql
SELECT COUNT(*) AS total_records FROM employees;
```
Use this in the frontend:
```js
const totalPages = Math.ceil(total_records / page_size);
```

Let me know if you need a **MySQL pagination query** for your **backend API**! 🚀