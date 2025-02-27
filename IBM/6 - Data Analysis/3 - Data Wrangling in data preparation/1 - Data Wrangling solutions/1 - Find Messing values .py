
missing_data = df.isnull()
for column in missing_data.columns:
    missing_count = missing_data[column].sum()  # Count only True (missing values)
    
    if missing_count > 0:  # Only print if there are missing values
        print(f"{column}: {missing_count} missing values\n")