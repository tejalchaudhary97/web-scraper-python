import streamlit as st
import pandas as pd
from scraper import scrape_news  # if you made a function
from job_scraper import scrape_jobs  # if you made a function

st.title("Web Scraper Dashboard 📰💼")

option = st.sidebar.selectbox("Choose scraper", ["Hacker News", "Jobs"])

if option == "Hacker News":
    st.header("Hacker News Articles")
    try:
        data = pd.read_csv("news.csv")
        st.dataframe(data)
    except FileNotFoundError:
        st.warning("Run scraper.py locally first to generate news.csv")

elif option == "Jobs":
    st.header("Job Listings")
    try:
        data = pd.read_csv("jobs.csv")
        st.dataframe(data)
    except FileNotFoundError:
        st.warning("Run job_scraper.py locally first to generate jobs.csv")
