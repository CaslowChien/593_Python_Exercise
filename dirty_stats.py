import pandas as pd

df = pd.read_csv('funny_epidemiological_events.csv')
print("Number of missing cells by column:", df.isnull().sum()[['Condition', 'Agent', 'Reporting Agency', 'City']])
print("Number of categories:", df.nunique()[['Condition', 'Agent', 'Reporting Agency', 'City']])