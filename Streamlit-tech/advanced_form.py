import streamlit as st
from datetime import datetime

min_date = datetime(1990, 1, 1)
max_date = datetime.now()

st.title("User Information Form ")

with st.form(key="User collection form"):

    name1 = st.text_input("Enter your name: ")
    birthdate = st.date_input(
        "Enter your dob: ", max_value=max_date, min_value=min_date)

    if birthdate:
        age = max_date.year-birthdate.year
        print(age)
        if birthdate.month > max_date.month or (birthdate.month == max_date.month and birthdate.day > max_date.day):
            age -= 1

        st.write(f"Your calcultaed age is {age} years.")

    submit_button1 = st.form_submit_button(label="submit")

    if submit_button1:
        if not name1 or not birthdate:
            st.warning("Please fill all the input fields!")
        else:
            st.balloons()
            st.success(f"Thank You! {name1}, your age is {age} years ")

#here the string of age display after the dob doesnt update dynamically after the dob is set because the element inside the form will not rerun its state before submission

#in order to do such dynamic update we need to use session state