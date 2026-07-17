import streamlit as st 

#Fragments-way to rerun omly certain portions of the user interface and better organize or seperate out your code

st.title("My awesome app")


#massive effeciecy game -- if i  need to add any dynamic element that changes based on the value of another slider or button i can put it fragment so that on change it reruns that part rather than the whole screen

@st.fragment()
def toggle_and_text():
    cols=st.columns(2)
    cols[0].toggle("toggle")
    cols[1].text_area("Enter Text")

@st.fragment()
def filter_and_file():
    new_cols=st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload_image")
    new_cols[2].selectbox("choose option",["Option1","Option2","Option3"])
    new_cols[3].slider("Select value",0,100,50)
    new_cols[4].text_input("Enter text")


toggle_and_text()
cols=st.columns(2)
cols[0].selectbox("select from below",[1,2,3],None)
cols[1].button("update")
filter_and_file()