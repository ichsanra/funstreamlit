import streamlit as st
import speedtest

# Title of the app
st.title("Internet Speed Test")

# Button to trigger speed test
if st.button('Run Speed Test', key='run_speed_test_button'):
    st.write("Running speed test... Please wait.")
    
    # Create a Speedtest object
    st_speedtest = speedtest.Speedtest()
    
    # Get best server based on ping
    st_speedtest.get_best_server()
    
    # Perform download and upload speed test
    download_speed = st_speedtest.download() / 1_000_000  # Convert to Mbps
    upload_speed = st_speedtest.upload() / 1_000_000  # Convert to Mbps
    
    # Perform ping test
    ping_result = st_speedtest.results.ping
    
    # Display the results
    st.write(f"Download Speed: {download_speed:.2f} Mbps")
    st.write(f"Upload Speed: {upload_speed:.2f} Mbps")
    st.write(f"Ping: {ping_result:.2f} ms")
else:
    st.write("Click the button above to run the speed test.")
