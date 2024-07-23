import streamlit as st
import requests

# Function to get a random quote
def get_random_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    return response.json()

# Title of the app
st.title("Random Quote Generator")

# Button to fetch a new quote
if st.button("Get Random Quote"):
    quote_data = get_random_quote()
    quote = quote_data['content']
    author = quote_data['author']
    
    st.write(f"**{quote}**")
    st.write(f"- {author}")
else:
    st.write("Click the button above to get a random quote.")
