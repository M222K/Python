import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("Charts Demo")

# Sample data
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# in streamlit we can add all the charts and plots as a image and embedd them easily

# Area chart section
st.subheader("Area Chart")
st.area_chart(df)

# Bar chart Section
st.subheader("Bar Chart")
st.bar_chart(df)

# Line CHart Section
st.subheader("Line Chart")
st.line_chart(df)

# Scatter chart section
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame(
    {'x': np.random.randn(100),
    'y': np.random.randn(100)}
)
st.scatter_chart(scatter_data)

#Map section (displaying random points on a map)
st.subheader("Map")
map_data=pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[37.36,-122.4], #coordiantes
    columns=['lat','lon']
)
st.map(map_data)

#pyplot section
st.subheader("pyplot charts")
fig, ax=plt.subplots()
ax.plot(df['A'],label='A')
ax.plot(df['B'],label='B')
ax.plot(df['C'],label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)
