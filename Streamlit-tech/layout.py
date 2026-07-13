import streamlit as st

#Sidebar
st.sidebar.title("THis is sidebar")
st.sidebar.write("we can place elements like text , images , buttons here")
sidebar_input=st.sidebar.text_input("Enter your name")


#tabs layout - multiple tabs with context management of each

tab1, tab2,tab3=st.tabs(["Tab1","Tab2","Tab3"])

with tab1:
    st.write("This is tab1")

with tab2:
    st.write("this is tab2")
    
with tab3:
    st.write("This is tab3")

#Columns layout - this will give us rows laid out like flexbox xolumns where we can group diffrenet elements

col1,col2=st.columns(2)

with col1:
    st.header("Column1")
    st.write("this is column1")

with col2:
    st.header("Column2")
    st.write("this is column2")
    
#Container

with st.container(border=True):
    st.write("this is inside of container")
    st.write("we can think of containers as fgrouping of elements")
    st.write("helps manage sections of the page")
    
#Empty Placeholder
placeholder=st.empty()
placeholder.write("This is placeholder usefull for dynamic content, that needs to be changed after some event")

if st.button("Update Placeholder"):
    placeholder.write("the placeholder has been updated!")
    
#Expander
with st.expander("Expander for more details"):
    st.write("This is additonal inforamtion that is hidden by default")
    st.write("You can use exapnders to keep your interface cleaner")
    
#Popover (Tooltip)
st.write("Hover over this for tooltip")
st.button("Button with tooltip",help="this is popup on hover")

#Sidebar input handeling
if sidebar_input:
    st.write(f"You entered in the sidebar:{sidebar_input}")