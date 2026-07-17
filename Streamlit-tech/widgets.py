import streamlit as st

#All of our widgets or elements be it button or anyhting have a auto generated ID , which depends on what type of element it is and what your parametre is .

#DUplicate ID issue--> when we create the element with same parametres
st.button("Ok")
st.button("Ok",key="btn2") #eevery btn kind of store its state or session using the unique id it generates

#at the time of rerun the button changes its state to true and return the value if there is duplicate btns , we can issue to idetify the state to which btn element

if "slider" not in st.session_state:
    st.session_state.slider=25
    
min_value=st.slider("set min value",0,50,25)

st.session_state.slider=st.slider("Slider",min_value,100,st.session_state.slider)

#when a component is no longer rendered on the screen we actually remove its state
#on rerun it will consider it as a brand new component rendered not hidden so it deosnt hold previosly filled value

if "user_input" not in st.session_state:
    st.session_state.user_input = ""
    
if "checkbox" not in st.session_state:
    st.session_state.checkbox=False

def toggle_btn():
    st.session_state.checkbox=not st.session_state.checkbox

st.checkbox("Show input field",value="st.session_state.checkbox", on_change=toggle_btn)

if st.session_state.checkbox:
    input=st.text_input("Enter Something",value=st.session_state.user_input)
    st.session_state.user_input=input
else:
    user_input=st.session_state.get("user_input","")
    
st.write(f"the user input is :{input}")