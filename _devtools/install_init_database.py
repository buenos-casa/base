# Import Python packages
import os, sqlite3
import pandas as pd
from pandas import DataFrame

# Define DB file
db_file = 'webapp/data.db'

conn = sqlite3.connect(db_file)
c = conn.cursor()

communes = pd.read_csv('data/communes.csv')
communes.drop(['count'], axis=1).to_sql('COMMUNES', conn, if_exists='replace', index=True)

barrio = pd.read_csv('data/barrio_table.csv')
barrio.to_sql('BARRIOS', conn, if_exists='replace', index=False)

census = pd.read_csv('data/census/cleaned_data.csv')
census.to_sql('CENSUS', conn, if_exists='replace', index=False)

prop = pd.read_csv('data/prop_data/cleaned_data.csv')
prop.to_sql('PROPERTY', conn, if_exists='replace', index=True)

proper_barrios_rent = pd.read_json('data/properati_data/rent/barrios_rent.json')
proper_barrios_rent.to_sql('RENT', conn, if_exists='replace', index=False)

proper_barrios_rent = pd.read_json('data/properati_data/rent/barrios_month.json')
proper_barrios_rent.to_sql('RENT_MO', conn, if_exists='replace', index=True)

proper_barrios_sell = pd.read_json('data/properati_data/sell/all_time.json')
proper_barrios_sell.to_sql('SELL', conn, if_exists='replace', index=False)

proper_barrios_sell = pd.read_json('data/properati_data/sell/month.json')
proper_barrios_sell.to_sql('SELL_MO', conn, if_exists='replace', index=True)
