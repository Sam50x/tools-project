import streamlit as st
import pandas as pd
import os

st.title('Data Exploring Page')

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(root_dir, 'data', 'books_clean.csv')

clean_df = pd.read_csv(file_path)

st.subheader('Clean data:')
st.write(clean_df)