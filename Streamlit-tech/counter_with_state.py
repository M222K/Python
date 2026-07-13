import streamlit as st

#Session State---> something that we can use to store values within the same user session
#Each session is specific to that user and the instace of a web browser the user is working upon,even if we reload the page , we will have a new session altogether,it do not change on reruns of script but when the browser reloades or the user changer or browser

#Instead of storing value of counter as a variable we will store it in form of session state

if "counter" not in st.session_state: #basically session_state is like a python dict that stores the value over the key counter for it .
    st.session_state.counter=0

if st.button("Increment counter"):
    st.session_state.counter+=1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("reset"):
    st.session_state.counter=0
    st.write(f"Counter reset")
else:
    st.write("Counter is not reset")

st.write(f"Counter value is {st.session_state.counter}")