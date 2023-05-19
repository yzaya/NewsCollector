from bs4 import BeautifulSoup
import urllib.request
import sys, json, csv, re


# Get the data from the website
GNews = "https://news.google.com/news/rss/headlines"
r = urllib.request\
    .urlopen(GNews)
xml = r.read() #the data on the website is alrady in an xml format
parser = "html.parser"
soup = BeautifulSoup(xml,parser)
soup # this is the parsed data


results = []
for item in soup.find_all("item"):
    title = item.find("title")
    link = item.find("link")
    pub_date = item.find("pubdate") or item.find("pubdate")
    if title is None:
        continue
    else:
        result = [title.text, link.text, pub_date.text]
        results.append(result)
results

# Clean the array to add quotes at the beginning and end of the first column

quoted_results = unquoted_data = [[re.sub(r'^"(.+)"$', r'\1', value) if col_index == 0 else value for col_index, value in enumerate(row)] for row in results]
quoted_results

with open('googleNews.csv', "a", newline='') as f:
    w = csv.writer(f,delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for row in quoted_results:
        w.writerow(row)