# Import Python packages
import os, sqlite3
import pandas as pd
from pandas import DataFrame

# Define DB file
db_file = 'webapp/data.db'

conn = sqlite3.connect(db_file)
c = conn.cursor()

census = pd.read_csv('data/census/cleaned_data2.csv')
census.to_sql('CENSUS', conn, if_exists='replace', index=False)

prop = pd.read_csv('data/prop_data/cleaned_data.csv')
prop.to_sql('PROPERTY', conn, if_exists='replace', index=False)
