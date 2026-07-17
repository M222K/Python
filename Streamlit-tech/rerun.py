import streamlit as st 

st.title("Counter example with rerun")

if "count" not in st.session_state:
    st.session_state.count=0

def increment_rerun():
    st.session_state.count+=1
    st.rerun() #to update the state instantly after call as the fun is called after display so it lags, solution is this

st.write(f"Current Count:{st.session_state.count}")

if st.button("increment and update immediatley"):
    increment_rerun()