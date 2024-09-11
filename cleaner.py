import sqlite3
import pandas as pd

sqlite_db = sqlite3.connect('health_events_data.db')
df = pd.read_sql_query("SELECT * FROM events", sqlite_db, index_col='index')

# Event ID should be object
df['Event ID'] = df['Event ID'].astype('object')

# impute missing values
numeric_columns = df.select_dtypes(include=['number']).columns
category_columns = df.select_dtypes(include=['object']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
df[category_columns] = df[category_columns].fillna(df[category_columns].mode().iloc[0])

# remove duplicates
df = df.drop_duplicates()

# save the new table
conn = sqlite3.connect('health_events_data.db')
df.to_sql('cleaned_data', conn, if_exists='replace') # table name = 'cleaned_data'