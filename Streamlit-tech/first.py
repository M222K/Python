#Streamlit- Python based UI libraary to create frontend without using html, css , javascript.

import streamlit as st

#st.write()--> used to add anything to the frontend app. It can be text, images, dataframes, charts, etc.
st.write("hello world!")

#TO RUN THE STREALIT APP, USE THE COMMAND BELOW IN TERMINAL--> streamlit run file_name.py

# '''
# Streamlit gives you both a Local URL and a Network URL because it runs on a client-server architecture. This means the backend server runs on your machine, while the frontend renders in your browser.
# Local URL: Connects only to your specific machine (e.g., http://localhost:8501). It is private and used exclusively for your own development.
# Network URL: Uses your machine's local IP address (e.g., http://192.168.X.X:8501). It allows coworkers or devices on the same Wi-Fi or local network to view your app
# '''

#this also supports hot reloading, so if you make any changes to the code, it will automatically reflect in the browser without needing to restart the server.

st.write(
    {
    "age":34,
    "name":"Mahak"
}) #streamlit automatically determines how to write any object you put as parametre in the app


#We can also write any expression to the main line of python file and it will automatically displayed on streamlit app

3+7 #gives the sum on app
"this will give the answer 10"

#Streamlit Data Flow-->Anytime something must be updated on the screen,Streamlit reruns your entire script from top to bottom