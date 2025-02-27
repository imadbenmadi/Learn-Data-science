# Advanced Usage of DataFrame Attributes and Methods

## 1. Introduction

DataFrames in pandas provide a rich set of attributes and methods for efficient data manipulation and analysis. This document presents complex examples demonstrating the use of various DataFrame attributes and methods.

## 2. Example Dataset

We start by creating a DataFrame with diverse data types.

```python
import pandas as pd
import numpy as np

# Sample data creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, np.nan],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining Date': pd.to_datetime(['2015-06-23', '2016-09-17', '2017-11-05', '2018-02-20', '2019-12-25'])
}
df = pd.DataFrame(data)
```

## 3. DataFrame Attributes

### 3.1 Shape

```python
print(df.shape)
```

_Output: (5, 5) – 5 rows and 5 columns._

### 3.2 Info

```python
print(df.info())
```

_Displays column names, data types, and null values._

## 4. DataFrame Methods

### 4.1 Descriptive Statistics

```python
print(df.describe())
```

_Generates summary statistics for numerical columns._

### 4.2 Head and Tail

```python
print(df.head(3))  # First 3 rows
print(df.tail(2))  # Last 2 rows
```

_Displays the first and last rows of the DataFrame._

### 4.3 Aggregation Functions

```python
print(df['Salary'].mean())  # Average salary
print(df[['Age', 'Salary']].sum())
```

_Computes mean salary and sum of numerical columns._
### Explanation of `groupby` and Aggregation

#### **Understanding `groupby`**
The `groupby` function in pandas is used to split the DataFrame into groups based on a specific column. This allows us to perform aggregate functions, such as calculating the mean, sum, or count, for each group separately.

#### **Breaking Down the Code**
```python
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)
```
1. **`df.groupby('Department')`**: 
   - This groups the data based on unique values in the `Department` column.
   - All rows belonging to the same department are collected together.

2. **`['Salary']`**:
   - Specifies that we are interested in the `Salary` column.

3. **`.mean()`**:
   - Computes the mean (average) salary for each department.

#### **Example Breakdown**
Given the DataFrame:
| Name    | Age | Salary | Department |
|---------|-----|--------|------------|
| Alice   | 25  | 50000  | HR         |
| Bob     | 30  | 60000  | IT         |
| Charlie | 35  | 70000  | Finance    |
| David   | 40  | 80000  | IT         |
| Eva     | NaN | 90000  | HR         |

After applying `groupby`:
| Department | Average Salary |
|------------|---------------|
| Finance    | 70000         |
| HR         | 70000         | *(Average of 50000 and 90000)* |
| IT         | 70000         | *(Average of 60000 and 80000)* |

### 4.4 Sorting

```python
print(df.sort_values(by=['Salary'], ascending=False))
```

_Sorts employees by salary in descending order._

### 4.5 Grouping and Aggregation

```python
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)
```

_Computes average salary per department._

### 4.6 Handling Missing Values

```python
df['Age'].fillna(df['Age'].median(), inplace=True)
print(df)
```

_Fills missing age values with the median age._

### 4.7 Column and Row Manipulation

```python
df.drop(columns=['Joining Date'], inplace=True)
df.rename(columns={'Salary': 'Annual Salary'}, inplace=True)
print(df)
```

_Drops a column and renames another._

### 4.8 Applying Functions

```python
df['Salary Increment'] = df['Salary'].apply(lambda x: x * 1.10)
print(df)
```

_Applies a 10% salary increment._

## 5. Conclusion

This document demonstrated practical use cases of key DataFrame attributes and methods in pandas, showcasing efficient data manipulation techniques.
