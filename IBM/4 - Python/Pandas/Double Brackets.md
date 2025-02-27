### **Why Use Double Brackets `df[['Column1', 'Column2']]`?**

When selecting multiple columns from a DataFrame, you must use **double square brackets (`[['col1', 'col2']]`)** because:

1. **Single Brackets (`df['Column']`) Returns a Series**

    ```python
    z = df['Department']
    print(type(z))  # <class 'pandas.core.series.Series'>
    ```

    - This returns a **pandas Series**, not a DataFrame.

2. **Double Brackets (`df[['Column1', 'Column2']]`) Returns a DataFrame**
    ```python
    z = df[['Department', 'Salary']]
    print(type(z))  # <class 'pandas.core.frame.DataFrame'>
    ```
    - This returns a **DataFrame**, which is useful when working with multiple columns.

### **Why is it Necessary?**

-   Pandas treats column selection differently based on **whether you select one or multiple columns**.
-   The **outer brackets** (`df[...]`) are used to access the column.
-   The **inner brackets** (`[['col1', 'col2']]`) indicate that you're selecting multiple columns, ensuring the result is still a **DataFrame**.

### **What Happens if You Select a Non-Existent Column?**

If `'ID'` doesn't exist in your DataFrame:

```python
z = df[['Department', 'Salary', 'ID']]
```

It will throw an error:

```plaintext
KeyError: "['ID'] not in index"
```

To **avoid this error**, you can check column existence before selecting:

```python
cols = ['Department', 'Salary', 'ID']
valid_cols = [col for col in cols if col in df.columns]
z = df[valid_cols]  # Only selects columns that exist
```
