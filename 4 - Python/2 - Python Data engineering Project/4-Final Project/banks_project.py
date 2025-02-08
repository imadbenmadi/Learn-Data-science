from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 
import os

url = 'https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
final_table_attr = ["Name", "MC_USD_Billion","MC_GBP_Billion",
                     "MC_EUR_Billion" ,"MC_INR_Billions"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
code_log = "code_log.txt"
exchange_rates = "exchange_rate.csv"   
output_csv_path = "Largest_banks_data.csv"






def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    if not os.path.exists(code_log):
        with open(code_log, 'w') as f:
            pass
    with open(code_log, 'a') as f:
        f.write(timestamp + ' : ' + message + '\n')

def my_extract(url, table_attribs):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find_all("tbody")[1]
    df = pd.DataFrame(columns=table_attribs)

    table_rows = table.find_all("tr")
    table_rows = [row for row in table_rows if row.find_all("td")]

    data_dict = {"Name": [], "MC_USD_Billion": []}  # Dictionary to store lists of values

    for row in table_rows:
        cols = row.find_all("td")  
        if len(cols) < 3:
            continue
        
        name_tag = cols[1].find("a")
        bank_name = name_tag.text.strip() if name_tag else "Unknown"
        market_cap = cols[2].text.strip()

        # Append to dictionary lists
        data_dict["Name"].append(bank_name)
        data_dict["MC_USD_Billion"].append(market_cap)

    df = pd.DataFrame(data_dict)
    log_progress("Data extracted successfully")
    return df




def my_transform(df):
    # Remove commas and dollar signs and convert to float
    df['MC_USD_Billion'] = df['MC_USD_Billion'].str.replace(',', '').str.replace(r'\$', '').astype(float) 

    with open("exchange_rate.csv","r") as f:
        skip = f.readline()
        exchange_rates = f.readlines()
    exchange_rates = [x.strip() for x in exchange_rates]
    formated_exchange_rates = {}
    for rate in exchange_rates:
        currency, rate = rate.split(",")
        formated_exchange_rates[currency] = float(rate)
    exchange_rates = formated_exchange_rates
    df['MC_GBP_Billion'] = round(df['MC_USD_Billion'] * exchange_rates['GBP'], 2)
    df['MC_EUR_Billion'] = round(df['MC_USD_Billion'] * exchange_rates['EUR'], 2)
    df['MC_INR_Billions'] = round(df['MC_USD_Billion'] * exchange_rates['INR'], 2)
    return df


def my_load(df, output_csv_path):
    df.to_csv(output_csv_path, index=False)
    df.to_sql(table_name, sqlite3.connect(db_name), if_exists='replace', index=False)
    log_progress("Data loaded successfully")

def run_query(query_statement, sql_connection):
    query = sql_connection.execute(query_statement)
    return query.fetchall()



my_load(my_transform(my_extract(url, table_attribs)), output_csv_path)
conn = sqlite3.connect(db_name)
query1 = f"SELECT * FROM Largest_banks"
query2 = f"SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
query3 = f"SELECT * from Largest_banks LIMIT 5"
# print(run_query(query1, conn))
# print(run_query(query2, conn))
print(run_query(query3, conn))