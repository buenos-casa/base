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

barrio = pd.read_csv('data/communes.csv')
barrio.to_sql('BARRIOS', conn, if_exists='replace', index=True)

census = pd.read_csv('data/census/cleaned_data.csv')
census.to_sql('CENSUS', conn, if_exists='replace', index=False)

prop = pd.read_csv('data/prop_data/cleaned_data.csv')
prop.to_sql('PROPERTY', conn, if_exists='replace', index=True)

proper_barrios_month = pd.read_json('data/properati_data/properati_barrios_month.json')
proper_barrios_month.to_sql('BARRIOS_MONTHLY', conn, if_exists='replace', index=True)

proper_barrios = pd.read_json('data/properati_data/properati_barrios.json')
proper_barrios.to_sql('BARRIOS_RENT_STATS', conn, if_exists='replace', index=True)

proper_sell_month = pd.read_json('data/properati_data/properati_sell_month.json')
proper_sell_month.to_sql('SELL_MONTH', conn, if_exists='replace', index=True)

proper_sell = pd.read_json('data/properati_data/properati_sell.json')
proper_sell.to_sql('SELL', conn, if_exists='replace', index=True)
