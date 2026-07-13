import streamlit as st 


#counter without session state
#as soon as the button is tapped the value gets 1 then again after it is tapped as the script reruns the value again set to 0 thus , we are not able to store the previous chnaged state

counter=0

st.write(f"Counter value :{counter}")

if st.button("increment counter"):
    counter+=1
    st.write(f"counter value is incremented to {counter}")
else:
    st.write(f"Counter stays at {counter}")
    
    