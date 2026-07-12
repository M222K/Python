import streamlit as st

pressed=st.button("Press me!") #this is a button (every event occured on app has a state with it) (initially the state of button is false as soon as the event on click happens the state turns to true)

print("first",pressed)

pressed2=st.button("second button")
print("second",pressed2) #this will return the boolean state value of button every time the screen event aoccurs entire script reruns
