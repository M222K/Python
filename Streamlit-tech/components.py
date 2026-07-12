import streamlit as st
import os

#Text based elements

st.title("Super simple title")
st.header("this is a header")
st.subheader("subheader")
st.markdown("this is **Markdown**")
st.caption("small text")
code_example='''
def greet(name):
print("hello",name)
'''

st.code(code_example)

st.divider()

# to import and add images --> create a static folder and add your media in same directory as of app

#use os library to crete path to image saved locally
st.image(os.path.join(os.getcwd(), "static","a man and woman 1 (1).png"))