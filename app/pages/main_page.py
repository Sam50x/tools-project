import streamlit as st

st.title('Main Page')

st.text_input("Your name", key="name")

name = st.session_state.name

if name:
    f'Hello, {st.session_state.name}. This is our Data Science Tools web scraping project.'
    'Enjoy, bitch! 😉'

url = 'https://books.toscrape.com'