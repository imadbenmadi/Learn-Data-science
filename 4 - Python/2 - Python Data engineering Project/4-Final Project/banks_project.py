from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 
import os

url = 'https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
final_table_attr = ["Name", "MC_USD_Billion","MC_GBP_Billion", "MC_EUR_Billion" ,"MC_INR_Billions"]
output_csv_path = "Largest_banks_data.csv"
db_name = 'Banks.db'
table_name = 'Largest_banks'
code_log = "code_log.txt"








def my_extract(url, table_attribs):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find_all("tbody")[2]
    df = pd.DataFrame(columns=table_attribs)

    # The row should not be empty.
    table_rows = table.find_all("tr")
    table_rows = [row for row in table_rows if [td for td in row.find_all("td") if td.text.strip()]]

    # Keep only rows where the first column <td> contains an <a> tag (a link)
    rows_with_valid_links = [row for row in table_rows if row.find_all("td") and row.find_all("td")[0].find("a")]
    table_rows = [ row.find_all("td") for row in rows_with_valid_links]

    # the third column should not be —
    table_rows = [row for row in table_rows if row[2].text.strip() != "—"]

    # string the df in dictionary
    dict = {}
    dict[table_attribs[0]] = [row[1].text.strip() for row in table_rows]
    dict[table_attribs[1]] = [row[2].text.strip() for row in table_rows]

    # Append all these dictionaries one by one to the dfframe.
    df = pd.concat([df, pd.DataFrame(dict)], ignore_index=True)
    log_progress("Data extracted successfully")
    return df


def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Name": col[0].a.contents[0],
                             "MC_USD_Billion": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df

def my_transform(df):
    # Remove commas and dollar signs and convert to float
    df['MC_USD_Billion'] = df['MC_USD_Billion'].str.replace(',', '').str.replace(r'\$', '').astype(float) 
    # devide by 1000 and round to 2 decimal places
    df['MC_USD_Billion'] = round(df['MC_USD_Billion']/1000, 2)
    # Modify the name of the column from 'MC_USD_Billion' to 'GDP_USD_billions'
    df.rename(columns={'MC_USD_Billion': 'GDP_USD_billions'}, inplace=True)
    log_progress("Data transformed successfully")
    return df

def transform(df):
    GDP_list = df["MC_USD_Billion"].tolist()
    GDP_list = [float("".join(x.split(','))) for x in GDP_list]
    GDP_list = [np.round(x/1000,2) for x in GDP_list]
    df["MC_USD_Billion"] = GDP_list
    df=df.rename(columns = {"MC_USD_Billion":"GDP_USD_billions"})
    return df

def my_load(df, csv_path):
    df.to_csv(csv_path, index=False)
    df.to_sql(table_name, sqlite3.connect(db_name), if_exists='replace', index=False)
    log_progress("Data loaded successfully")

def run_query(query_statement, sql_connection):
    query = sql_connection.execute(query_statement)
    return query.fetchall()

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    if not os.path.exists(code_log):
        with open(code_log, 'w') as f:
            pass
    with open(code_log, 'a') as f:
        f.write(timestamp + ' : ' + message + '\n')


my_load(my_transform(my_extract(url, table_attribs)), csv_path)
conn = sqlite3.connect(db_name)
query = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
print(run_query(query, conn))