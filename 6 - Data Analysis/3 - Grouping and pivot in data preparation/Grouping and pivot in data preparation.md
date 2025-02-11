
### **1️⃣ Grouping (`groupby()`)**  
It’s used to group data by one or more columns and then apply an aggregate function (like sum, mean, count, etc.).

#### **Example:**  
Imagine we have a dataset of **sales** by **city** and **category**.

```python
import pandas as pd

# Example DataFrame
data = {
    'city': ['NY', 'LA', 'NY', 'LA', 'NY', 'LA'],
    'category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'sales': [100, 150, 200, 250, 300, 350]
}
df = pd.DataFrame(data)

# Group by 'city' and sum the 'sales'
grouped = df.groupby('city')['sales'].sum()
print(grouped)
```

#### **Output:**
```
city
LA    750
NY    600
Name: sales, dtype: int64
```

In this case, we grouped the data by `city` and summed up the `sales` for each city.

#### **Another Example (Multiple Grouping):**

```python
# Group by both 'city' and 'category' and calculate the average 'sales'
grouped_multiple = df.groupby(['city', 'category'])['sales'].mean()
print(grouped_multiple)
```

#### **Output:**
```
city  category
LA    A            150
      B            300
NY    A            200
      B            200
Name: sales, dtype: int64
```

Here, the data is grouped by both `city` and `category`, and we calculate the average sales for each group.

---

### **2️⃣ Pivot Table (`pivot_table()`)**  
It’s used to reshape data by **reorganizing it** into a table format, often with rows as categories and columns as the aggregated values.

#### **Example:**

```python
# Pivot the data to see total sales by city and category
pivot = df.pivot_table(index='city', columns='category', values='sales', aggfunc='sum')
print(pivot)
```

#### **Output:**
```
category    A    B
city              
LA         150  350
NY         300  200
```

Here, we used `pivot_table()` to **restructure** the data:
- **Rows (`index`)**: `city`
- **Columns**: `category`
- **Values**: `sales`
- **Aggregation (`aggfunc`)**: We used `sum` to sum sales for each combination of city and category.

---

### **Key Differences:**
- **`groupby()`** is used when you want to **group data** and apply aggregation functions like `sum()`, `mean()`, `count()`, etc.
- **`pivot_table()`** reshapes the data, often providing a **summary table** with rows, columns, and aggregated values.
