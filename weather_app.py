import streamlit as st
import requests

# Function to get weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Your OpenWeatherMap API key
api_key = 'your API key'  # Replace with your actual API key

# Title of the app
st.title("Weather Information")

# Input for the city name
city = st.text_input("Enter city name:")

# Button to get weather data
if st.button("Get Weather"):
    if city:
        weather_data = get_weather(city, api_key)
        if weather_data.get("cod") == "404":
            st.error("City not found! Please enter a valid city name.")
        elif weather_data.get("cod") != 200:
            st.error(f"Error: {weather_data.get('message', 'Unable to fetch weather data')}")
        else:
            st.subheader(f"Weather in {city}")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        st.error("Please enter a city name.")
