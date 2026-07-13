import streamlit as st

# CALLBACK --> function THAT we trigger When a button is pressed or a onchange event occur to do something or process somthing at the backend

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

if st.session_state.step == 1:
    st.header("Form pt 1: Info")

    name = st.text_input(
        "Enter your name", value=st.session_state.info.get("name", ""))

    if st.button("NEXT"):
        st.session_state.info["name"] = name
        st.session_state.step = 2
        #we can use callback to call a function rather than changing step here

elif st.session_state.step == 2:
    st.header("Form pt 2: Review")

    st.subheader("Please review this info")

    st.write(f"Name: {st.session_state.info.get("name", "")}")

    if st.button("submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}

    if st.button("back"):
        st.session_state.step = 1

# herre when we click the next the value in state changes but the script is not reruns as it is still 1 as step when it reruns and get into if condition , when its pressed again , this time script runs with value as 2 and get into part 2 .
