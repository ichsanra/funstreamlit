import streamlit as st
import requests
import pandas as pd
import time

# Function to get cryptocurrency prices
def get_crypto_prices(cryptos):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(cryptos),
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    return response.json()

# List of cryptocurrencies to track
cryptos = ['bitcoin', 'ethereum', 'dogecoin', 'litecoin', 'cardano']

# Title of the app
st.title("Cryptocurrency Prices Tracker")

# Display real-time prices
st.header("Real-Time Cryptocurrency Prices")

# Refresh interval (in seconds)
refresh_interval = st.slider("Select refresh interval (seconds)", 5, 60, 10)

while True:
    prices = get_crypto_prices(cryptos)
    df = pd.DataFrame(prices).T.reset_index()
    df.columns = ['Cryptocurrency', 'Price (USD)']
    st.write(df)

    time.sleep(refresh_interval)
    st.experimental_rerun()

