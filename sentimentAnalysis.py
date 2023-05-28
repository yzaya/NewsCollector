# A file for doing sentiment analysis on the news titles 
# using HuggingFace's transformers library
from transformers import pipeline
import csv, pandas as pd

df = pd.read_csv('googleNews.csv')
df

# Create a pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Apply the pipeline to the titles
senti = []
for i in df['title']:
    senti.append(sentiment_pipeline(i))

# Turn the output into a dataframe
sentiDF = pd.DataFrame(senti)

# Separate the items into separate columns
sentiDF['label'] = sentiDF[0].apply(lambda x: x['label'])
sentiDF['score'] = sentiDF[0].apply(lambda x: x['score'])

df['label'] = sentiDF['label']
df['score'] = sentiDF['score']

df.to_csv('GNews-withSentiment.csv', mode='a')
