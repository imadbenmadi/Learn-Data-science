import pandas as pd
import numpy as np

# Sample data creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'
             , 'Edward'],
    'Age': [25, 30, 35, 40, np.nan],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining Date': pd.to_datetime(['2015-06-23', '2016-09-17', '2017-11-05', '2018-02-20', '2019-12-25'])
}
df = pd.DataFrame(data)
# print(df)
# print("_________________________")
grouped = list(df.groupby('Department'))[1]
print(grouped)
# hr_group = df.groupby('Department').get_group('HR')
# print(hr_group)
