import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://news.ycombinator.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
links = []

for item in soup.select(".titleline a"):
    titles.append(item.text)
    links.append(item.get("href"))

data = pd.DataFrame({"Title": titles, "Link": links})
data.to_csv("news.csv", index=False)
print("Scraping completed. Check news.csv")
