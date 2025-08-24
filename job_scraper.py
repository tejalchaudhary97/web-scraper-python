import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example: RemoteOK job listings
URL = "https://remoteok.com/remote-dev-jobs"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
companies = []
links = []

for job in soup.select('tr.job'):
    title_tag = job.select_one('h2')
    company_tag = job.select_one('.companyLink')
    link_tag = job.get('data-href')
    
    if title_tag and company_tag and link_tag:
        titles.append(title_tag.text.strip())
        companies.append(company_tag.text.strip())
        links.append("https://remoteok.com" + link_tag)

# Save to CSV
data = pd.DataFrame({"Title": titles, "Company": companies, "Link": links})
data.to_csv("jobs.csv", index=False)

print("Job scraping completed. Check jobs.csv")
