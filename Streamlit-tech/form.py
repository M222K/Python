#streamlit form is used with with keyword whenever we have a form and we want to run it , streamlit will take all the inputs of the form and then reruns the application in any of the event.

#this help in avoiding reruns in updating or creation of any click event isnside elements of form multiple times, it only reruns once submit altogether

import streamlit as st 
from datetime import datetime

st.title("User Information Form")

form_values={
    "name":None,
    "age":None,
    "gender":None,
    "dob":None
}
min_date=datetime(1990,1,1)
max_date=datetime.now()

#group the elements inside form , to handle each element state
with st.form(key="user_info_form"):
    
    form_values["name"]=st.text_input("Enter your name: ")
    form_values["age"]=st.number_input("Enter your age: ")
    
    form_values["gender"]=st.selectbox("Gender",["Male","Female"])
    
    form_values["dob"]=st.date_input("Enter your dob",max_value=max_date,min_value=min_date)
    
    submit_button=st.form_submit_button(label="Submit") #after this it will reruns and print
    print("after submit")
    if submit_button: #runs when the button state changes to true
        print("in if ")
        if not all(form_values.values()):
            st.warning("Please fill in all the inputs!")
        else:
            st.balloons()
            st.write("##info")
            for(key,values) in form_values.items():
                st.write(f"{key}:{values}")

print(form_values)