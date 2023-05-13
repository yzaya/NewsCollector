# This is the webscraper from the book intended to be made into a class.
# Not currently functional, but also contains the links to microsoft and apple feeds

from bs4 import BeautifulSoup
import urllib.request
import sys
import json

class Scraper:
    def __init__(self,site):
        self.site = site
        self.soup = None
    def scrapeSoup(self):
        r = urllib.request\
            .urlopen(self.site)
        xml = r.read()
        parser = "html.parser"
        self.soup = BeautifulSoup(xml,parser)
        return self.soup
    def soup2Dict(self):
        results = []
        for item in self.soup.find_all("item"):
            title = item.find("title")
            link = item.find("link")
            pub_date = item.find("pubdate") or item.find("pubdate")
            if title is None:
                continue
            else:
                result = {
                    "title": title.text,
                    "link": link.text,
                    "pub_date": pub_date.text
                }
                results.append(result)
        return results
    def soup2List(soup):
        results = []
        for item in soup.find_all("item"):
            title = item.find("title")
            link = item.find("link")
            pub_date = item.find("pubdate") or item.find("pubdate")
            if title is None:
                continue
            else:
                result = [
                    title.text,
                    link.text,
                    pub_date.text,
                    "\n"
                ]
                results.append(result)
        return results


# Google
Gnews = "https://news.google.com/news/rss/headlines"
GSoup = Scraper(Gnews)
print(dir(GSoup))
GSoupDict = Scraper.soup2Dict(GSoup)
Scraper.soup
print(GSoupDict)
Gresults
with open("googleNews.json", "a") as f:
    json.dump(Gresults,f)

with open("googleNews.csv", "a") as f:
    f.write(Gresults)


Gsize = sys.getsizeof(Gnews) #Gets the size of the var in bytes
Gsize = Gsize/1000  #Translates the size into kilobytes
Gsize

# Microsoft 
Mnews = "https://news.microsoft.com/feed/"
Mresults = Scraper(Mnews).scrape()
print(Mnews)

# Apple 
Anews = "https://www.apple.com/newsroom/rss-feed.rss"
Aresults = Scraper(Anews).scrape()
print(Aresults)