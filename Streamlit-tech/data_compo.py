import streamlit as st
import pandas as pd

st.title("Streamlit Elements")

#dataframe section
st.subheader("Dataframe")
df=pd.DataFrame({
    'Name':['Alice',"Bob",'Charlie','David'],
    'Age':[24,45,66,34],
    'Occupation':['Engineer','Doctor','Artist','Chef']
})
st.dataframe(df)

#data editor section (editable dataframe)
st.subheader("Data Editor")
editable_df=st.data_editor(df)
print(editable_df)

#Static table-only table no features of df
st.subheader("static table")
st.table(df)

#Metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows",value=len(df))
st.metric(label="Average Age",value=round(df['Age'].mean(),1))

#Json and Dict Section

st.subheader("JSON and Dictionery")
sample_dict={
    "name":"Alice",
    "age":23,
    "skills":["Python","AI","LLM"]
}
st.json(sample_dict)#showcase as json object

st.write("Dictionary view",sample_dict)
