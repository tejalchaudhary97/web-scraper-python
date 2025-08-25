import streamlit as st
from scraper import scrape_news

st.title("Hacker News Scraper")

if st.button("Scrape News"):
    data = scrape_news()
    st.dataframe(data)

