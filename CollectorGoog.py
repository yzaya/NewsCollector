from bs4 import BeautifulSoup
import urllib.request
import sys, json, csv, re


# Get the data from the website
GNews = "https://news.google.com/news/rss/headlines"
r = urllib.request\
    .urlopen(GNews)
xml = r.read() #the data on the website is already in an xml format
parser = "xml.parser"
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
    title_item = item.find("title")
    title_text = title_item.text
    title_list = title_text.split(" - ")
    title = title_list[0]
    source = title_list[1]
    link_element = item.find("link")
    link = link_element.next_sibling.strip() if link_element and link_element.next_sibling else None
    pub_date = item.find("pubdate") or item.find("pubdate")
    if title is None:
        continue
    else:
        result = [pub_date.text, title, source, link]
        results.append(result)
results


with open('googleNews.csv', "a", newline='') as f:
    w = csv.writer(f,delimiter=",", quotechar='"')
    for row in results:
        w.writerow(row)