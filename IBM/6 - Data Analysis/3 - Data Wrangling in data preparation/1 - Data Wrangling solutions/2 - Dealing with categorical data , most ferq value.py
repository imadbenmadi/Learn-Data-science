common_screen_size = df['Screen_Size_cm'].value_counts().idxmax()  # Get the most frequent value
df["Screen_Size_cm"].replace(np.nan, common_screen_size, inplace=True)  # Replace NaNs
