import csv
import pandas as pd

file_path = 'googleNews.csv'
df = pd.read_csv(file_path)
df
# split a column
df[['title', 'source']] = df['title'].str.split(' - ', 1, expand=True)

# change the order of the columns
df = df.reindex(columns=['date','title','source', 'link'])

# export to csv
df.to_csv("pdtest.csv", index=False)