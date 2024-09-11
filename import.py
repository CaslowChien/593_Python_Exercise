import csv
import sqlite3
import pandas as pd

conn = sqlite3.connect('health_events_data.db')
df = pd.read_csv('funny_epidemiological_events.csv')
df.to_sql('events', conn, if_exists='replace')