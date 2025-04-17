import streamlit as st

main_page = st.Page("pages/main_page.py", title="Main Page")
data_page = st.Page("pages/data_page.py", title="Data Page")

pg = st.navigation([main_page, data_page])

pg.run()