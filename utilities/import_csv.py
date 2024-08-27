import os
import pandas as pd
import sqlite3

# READ DATABASE TO PANDAS DF
csv_path = '../data/ousd_expenditures.csv'
df = pd.read_csv(csv_path)

# WRITE DF TO SQL
conn = sqlite3.connect('../data/database.db')
df.to_sql('ousd_expenditures', conn, if_exists='replace', index=False)
conn.close()
