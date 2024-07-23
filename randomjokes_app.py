import streamlit as st
import requests

# Function to get a random joke
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    return joke

# Streamlit app
st.title("Random Joke Generator")
st.write("Click the button below to get a random joke!")

if st.button("Get a Joke"):
    joke = get_joke()
    st.write(f"**{joke['setup']}**")
    st.write(f"*{joke['punchline']}*")
