from bs4 import BeautifulSoup
import urllib.request
import sys, json, csv, re


# Get the data from the website
GNews = "https://news.google.com/news/rss/headlines"
r = urllib.request\
    .urlopen(GNews)
xml = r.read() #the data on the website is already in an xml format
parser = "html.parser"
soup = BeautifulSoup(xml,parser)

# View an xml layout of the data being held in the soup variable
# print(soup.prettify()) # 

# Save it to an xml file
# with open('Soup.xml', 'w') as f:
#   f.write(str(soup.prettify()))

# This works for getting the url, but is not needed:
# for link in soup.find_all('source'):
#    print(link.get('url'))

# Turn the soup into a list
results = []
for item in soup.find_all("item"):
    title = item.find("title")
    link_element = item.find("link")
    link = link_element.next_sibling.strip() if link_element and link_element.next_sibling else None
    pub_date = item.find("pubdate") or item.find("pubdate")
    if title is None:
        continue
    else:
        result = [title.text, link, pub_date.text]
        results.append(result)
results

# Clean the array to add quotes at the beginning and end of the first column

quoted_results = unquoted_data = [[re.sub(r'^"(.+)"$', r'\1', value) if col_index == 0 else value for col_index, value in enumerate(row)] for row in results]

with open('googleNewsTest.csv', "a", newline='') as f:
    w = csv.writer(f,delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for row in quoted_results:
        w.writerow(row)