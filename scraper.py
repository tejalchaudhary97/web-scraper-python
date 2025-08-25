import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_news():
    URL = "https://news.ycombinator.com/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []
    links = []

    for item in soup.select(".titleline a"):
        titles.append(item.text)
        links.append(item.get("href"))

    data = pd.DataFrame({"Title": titles, "Link": links})
    return data
