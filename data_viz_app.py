import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title('Simple Data Visualization App')

# Markdown
st.markdown("""
This app allows you to upload a CSV file and select the type of visualization you want to create.
""")

# File uploader allows user to add their own CSV
uploaded_file = st.file_uploader("Choose a file", type=['csv'])

if uploaded_file is not uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())  # Show uploaded data
    
    # Let the user select the column for visualization
    column_to_plot = st.selectbox('Which column do you want to visualize?', df.columns)

    # Let the user select the type of plot
    plot_type = st.selectbox("Select the type of plot", ['Line', 'Bar', 'Histogram'])

    # Generate the plot
    fig, ax = plt.subplots()
    if plot_type == 'Line':
        df[column_to_plot].plot(kind='line', ax=ax)
        st.pyplot(fig)
    elif plot_type == 'Bar':
        df[column_to_plot].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)
    elif plot_type == 'Histogram':
        df[column_to_plot].plot(kind='hist', bins=30, ax=ax)
        st.pyplot(fig)
