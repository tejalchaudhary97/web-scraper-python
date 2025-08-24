# Web Scraper Python

A simple Python project that scrapes news headlines from Hacker News and saves them into a CSV file. This project demonstrates basic web scraping techniques using Python.

## Features

- Scrapes news headlines and corresponding links from Hacker News
- Exports data to `news.csv`
- Built with Python using:
  - `requests` for HTTP requests
  - `BeautifulSoup` for parsing HTML
  - `pandas` for saving data in CSV

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tejalchaudhary97/web-scraper-python.git
cd web-scraper-python

Create and activate a virtual environment (optional but recommended):

python -m venv venv
# Windows
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Usage

Run the scraper:

python scraper.py
