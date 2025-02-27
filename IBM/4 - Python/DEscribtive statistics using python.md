# Descriptive Analysis in Pandas

## Introduction

Descriptive analysis in Pandas provides various methods to summarize and explore datasets. It helps in understanding the central tendency, dispersion, and distribution of data.

## 1. Basic Summary Statistics

### `df.describe()`

-   Returns summary statistics of numerical columns.
-   Includes count, mean, standard deviation, min, 25th percentile, median (50th percentile), 75th percentile, and max.

```python
import pandas as pd

# Sample DataFrame
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [40000, 50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)

# Summary statistics
df.describe()
```

### `df.describe(include='all')`

-   Provides summary statistics for all columns, including categorical data.

```python
df.describe(include='all')
```

## 2. Measures of Central Tendency

### Mean (`df.mean()`)

```python
df['Age'].mean()
```

### Median (`df.median()`)

```python
df['Age'].median()
```

### Mode (`df.mode()`)

```python
df['Age'].mode()
```

## 3. Measures of Dispersion

### Standard Deviation (`df.std()`)

```python
df['Age'].std()
```

### Variance (`df.var()`)

```python
df['Age'].var()
```

### Range (Max - Min)

```python
df['Age'].max() - df['Age'].min()
```

### IQR (Interquartile Range)

```python
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
IQR
```

## 4. Frequency and Count Analysis

### Value Counts (`df['column'].value_counts()`)

```python
df['Age'].value_counts()
```

### Count (`df.count()`)

```python
df.count()
```

## 5. Correlation and Covariance

### Correlation Matrix (`df.corr()`)

```python
df.corr()
```

### Covariance (`df.cov()`)

```python
df.cov()
```

## 6. Skewness and Kurtosis

### Skewness (`df.skew()`)

```python
df.skew()
```

### Kurtosis (`df.kurt()`)

```python
df.kurt()
```

## 7. Percentiles and Quantiles

### Specific Percentile (`df.quantile(q)`, where `q` is between 0 and 1)

```python
df['Age'].quantile(0.75)
```

## 8. Summary of Missing Values

### Check for Missing Values (`df.isnull().sum()`)

```python
df.isnull().sum()
```

### Drop Missing Values (`df.dropna()`)

```python
df.dropna()
```

### Fill Missing Values (`df.fillna(value) `)

```python
df.fillna(df['Age'].mean())
```

## Conclusion

Descriptive analysis in Pandas provides a comprehensive summary of the dataset. These methods help in data cleaning, understanding patterns, and making informed decisions for further analysis.
