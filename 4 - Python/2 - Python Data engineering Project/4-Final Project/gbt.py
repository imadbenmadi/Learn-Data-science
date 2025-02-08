
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
code_log = "code_log.txt"

def log_progress(message):
    timestamp_format = '%Y-%b-%d-%H:%M:%S'  # Year-Month-Day-Hour-Minute-Second 
    now = datetime.now()  
    timestamp = now.strftime(timestamp_format)  
    with open(code_log, 'a') as f:
        f.write(f"{timestamp} : {message}\n")

def my_extract(url, table_attribs):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find_all("tbody")[1]
    df = pd.DataFrame(columns=table_attribs)

    table_rows = table.find_all("tr")
    table_rows = [row for row in table_rows if row.find_all("td")]

    data = []
    for row in table_rows:
        cols = row.find_all("td")  
        if len(cols) < 3:  # Ensure there are enough columns
            continue
        
        name_tag = cols[1].find("a")
        bank_name = name_tag.text.strip() if name_tag else "Unknown"
        market_cap = cols[2].text.strip()
        
        data.append({"Name": bank_name, "MC_USD_Billion": market_cap})
    
    df = pd.DataFrame(data)
    log_progress("Data extracted successfully")
    return df

df = my_extract(url, table_attribs)
print(df.head())  # Print first few rows
