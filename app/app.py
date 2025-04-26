import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

st.title('Welcome to our Project')

st.divider()

st.text_input("Your name", key="name")
name = st.session_state.name
if name:
    f'Hello, {st.session_state.name}. This is our Data Science Tools web scraping project.'
    'Enjoy, bitch! 😉'

st.divider()

url = 'https://books.toscrape.com'
st.markdown(f'We are scraping data from: [Books to Scrape Website]({url})')

dir_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(dir_path, 'books_clean.csv')
df = pd.read_csv(csv_path)
st.write(df)

st.divider()

data = df.groupby('genre')['stars'].mean().round()
st.markdown("### Unique Genres:")
st.write(df.genre.unique())

st.divider()

data_df = pd.DataFrame({
    'Genre': data.index,
    'Average Rating': data.values
})

st.markdown("### Book categories and average ratings:")

data_df = data_df.set_index('Genre')

st.bar_chart(data_df)

st.divider()

df2 = df.groupby('genre')['price'].mean().reset_index()

data_df = pd.DataFrame({
    'Genre': df2['genre'],
    'Average Price': df2['price'],
})

st.markdown("### Comparison between genre of books and avg price for it:")

data_df = data_df.set_index('Genre')

st.line_chart(data_df)

st.divider()

data_df = pd.DataFrame({
    'Price': df['price'],
    'Stars': df['stars'],
})

st.markdown("### Relationship between Price and Star Ratings:")

data_df = data_df.set_index('Price')

st.scatter_chart(data_df)

st.subheader('That shows that price of a book and its star rating doesn\'t change each other by any means')

st.divider()

genre_counts = df['genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Count']

categories = genre_counts.sort_values(by='Count', ascending=False).head(10)

st.markdown("### Distribution of Top Book Categories:")

fig = px.pie(
    categories,
    names='Genre',
    values='Count',
    color_discrete_sequence=px.colors.sequential.Viridis
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

data_df = pd.DataFrame({
    'Genre': df['genre'],
    'Price': df['price'],
})

st.markdown("### Boxplot of Price by Genre:")

fig = px.box(
    data_df,
    x='Genre',
    y='Price',
    color='Genre',
    color_discrete_sequence=px.colors.qualitative.Vivid,
    points="outliers"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

art_description=df[df['genre']=='Sequential Art']
art_description_text=' '.join(art_description['description'])

st.markdown("### Wordcloud for Sequential Art Descriptions:")

wordcloud = WordCloud(
    width=1200,
    height=1000,
    background_color='white',
    colormap='viridis'
).generate(art_description_text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')

st.pyplot(fig, use_container_width=True)

st.divider()