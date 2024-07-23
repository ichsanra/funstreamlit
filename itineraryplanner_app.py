import streamlit as st
from datetime import datetime, timedelta

# Function to create a daily itinerary
def create_itinerary(start_date, days, activities):
    itinerary = []
    current_date = start_date
    for day in range(days):
        itinerary.append({"date": current_date, "activities": activities})
        current_date += timedelta(days=1)
    return itinerary

# Streamlit app
st.title("Travel Itinerary Planner")
st.write("Plan your trip by entering the details below:")

# User inputs
start_date = st.date_input("Start Date", datetime.now())
days = st.number_input("Number of Days", min_value=1, max_value=30, value=1)
activities = st.text_area("Activities (separate by commas)", "Visit museum, Go to the beach, Try local food")

if st.button("Generate Itinerary"):
    activities_list = [activity.strip() for activity in activities.split(",")]
    itinerary = create_itinerary(start_date, days, activities_list)
    st.write("### Your Itinerary")
    for day in itinerary:
        st.write(f"**{day['date'].strftime('%A, %B %d, %Y')}**")
        for activity in day['activities']:
            st.write(f"- {activity}")
