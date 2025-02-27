import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('STAFF.db')

# Define table name and attributes
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Fix the file path
file_path = r"C:\Users\imadb\OneDrive\Bureau\Python Data engineering Project\2 - working with sql\INSTRUCTOR.csv"

# Read CSV file into DataFrame
df = pd.read_csv(file_path, names=attribute_list)

# Store DataFrame into SQLite table
df.to_sql(table_name, conn, if_exists='append', index=False)
print('Table is ready')

# Execute and print queries
for query_statement in [
    f"SELECT * FROM {table_name}",
    f"SELECT COUNT(*) FROM {table_name}"
]:
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)

# Append new data
data_dict = {
    'ID': [100],
    'FNAME': ['John'],
    'LNAME': ['Doe'],
    'CITY': ['Paris'],
    'CCODE': ['FR']
}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')

# Close connection
conn.close()
