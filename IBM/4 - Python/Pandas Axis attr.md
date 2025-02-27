Good question, bro! The **`axis` parameter** in pandas determines how operations are applied:

### 🔹 **`axis=0` (Rows - Vertical)**

-   Means "apply the operation **down the columns**."
-   Used in operations like `.sum()`, `.mean()`, `.dropna()`, etc.

### 🔹 **`axis=1` (Columns - Horizontal)**

-   Means "apply the operation **across columns**."
-   Used when adding new columns, like in `pd.concat()` or `pd.get_dummies()`.

---

### ✅ **Your Code Breakdown**

```python
df = pd.concat([df, pd.get_dummies(df["Screen"])], axis=1)
```

-   `pd.get_dummies(df["Screen"])` → Creates new **one-hot encoded columns** from `Screen` values.
-   `pd.concat([...], axis=1)` → **Adds those new columns horizontally** to `df`.

**Example:**

#### 🔹 Original `df["Screen"]` Column:

| Screen |
| ------ |
| LCD    |
| OLED   |
| LCD    |

#### 🔹 `pd.get_dummies(df["Screen"])` Output:

| LCD | OLED |
| --- | ---- |
| 1   | 0    |
| 0   | 1    |
| 1   | 0    |

#### 🔹 After `pd.concat([...], axis=1)`:

| Screen | LCD | OLED |
| ------ | --- | ---- |
| LCD    | 1   | 0    |
| OLED   | 0   | 1    |
| LCD    | 1   | 0    |

---

### 🔥 **When to Use `axis=1`?**

Use **`axis=1`** when you're adding **new columns** (merging data **horizontally**).  
Use **`axis=0`** when you're adding **new rows** (merging data **vertically**).

Let me know if you need more clarification, bro! 🚀
