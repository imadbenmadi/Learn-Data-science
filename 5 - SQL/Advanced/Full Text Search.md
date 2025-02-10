# Full-Text Search (FTS) – Efficient Text Searching in SQL

## **What is Full-Text Search?**

-   A technique for **fast text searching** inside a database.
-   Helps find **words, phrases, or similar text** efficiently.
-   Used in **search engines, blogs, e-commerce sites, and document indexing**.

✅ **Why Use Full-Text Search Instead of `LIKE`?**

-   `LIKE '%keyword%'` is **slow** for large datasets.
-   FTS uses **indexes** for **fast & efficient** searches.
-   Supports **ranking results, relevance, and multiple search options**.

---

## **🛠️ Setting Up Full-Text Search in MySQL**

### **1️⃣ Create a Sample Table**

Imagine a blog where users search for articles.

```sql
CREATE TABLE articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    FULLTEXT(title, content) -- Enabling Full-Text Search
);
```

### **2️⃣ Insert Sample Data**

```sql
INSERT INTO articles (title, content) VALUES
('SQL Performance Tips', 'Learn how to optimize queries for speed.'),
('Advanced MySQL', 'Understanding indexing and query optimization.'),
('Full-Text Search in MySQL', 'This tutorial explains how to use full-text search.'),
('SQL vs NoSQL', 'A detailed comparison between SQL and NoSQL databases.');
```

---

## **🔍 Searching with Full-Text Search**

### **Basic Search with `MATCH() AGAINST()`**

Find articles that mention **"SQL"**:

```sql
SELECT * FROM articles
WHERE MATCH(title, content) AGAINST('SQL');
```

### **🛠️ Output**

| id  | title                     | content                                                |
| --- | ------------------------- | ------------------------------------------------------ |
| 1   | SQL Performance Tips      | Learn how to optimize queries for speed.               |
| 2   | Advanced MySQL            | Understanding indexing and query optimization.         |
| 3   | Full-Text Search in MySQL | This tutorial explains how to use full-text search.    |
| 4   | SQL vs NoSQL              | A detailed comparison between SQL and NoSQL databases. |

✅ **Finds all articles containing "SQL"!** 🚀

---

## **🔥 Advanced Search Features**

### **1️⃣ Searching for Exact Phrases**

Find articles with **"Full-Text Search"** as an exact phrase:

```sql
SELECT * FROM articles
WHERE MATCH(title, content) AGAINST('"Full-Text Search"' IN BOOLEAN MODE);
```

📌 **Boolean Mode** allows advanced search options.

---

### **2️⃣ Excluding Words**

Find articles **about SQL** but **NOT about NoSQL**:

```sql
SELECT * FROM articles
WHERE MATCH(title, content) AGAINST('SQL -NoSQL' IN BOOLEAN MODE);
```

✅ **Excludes results containing "NoSQL"!**

---

### **3️⃣ Ranking Search Results (Relevance)**

Order results **by relevance score**:

```sql
SELECT
    title,
    MATCH(title, content) AGAINST('SQL') AS relevance
FROM articles
ORDER BY relevance DESC;
```

✅ **More relevant results appear first!** 🔥

---

## **💡 Summary**

-   **Full-Text Search is much faster than `LIKE` searches**.
-   Supports **boolean operators (`+`, `-`, `"..."`) for advanced search**.
-   Allows **ranking results by relevance**.
-   Commonly used in **search engines, blogs, and document-based applications**.
