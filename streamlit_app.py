import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime

# ==========  st.write ========== 
st.header("st.write")

st.subheader("Display Plain Text")
st.write("Hello World!")

st.subheader("Display numbers")
st.write(1234)

st.subheader("Display Text with Markdown")
st.write('Hello, *World!* :sunglasses:')

st.subheader("Display DataFrames")
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

st.subheader("Accept Multiple Arguments")
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.subheader("Display Charts")
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


# ==========  st.slider ========== 
st.subheader('Range time slider')

appointment = st.slider(
  "Schedule your appointment:",
  value=(time(11,30), time(12, 45))
)
st.write("you're scheduled for:", appointment)

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
    #  value=(datetime(2019, 12, 31), datetime(2020, 1, 1)),
    min_value=datetime(2020, 1, 1, 8, 0),
    # max_value=datetime(2020, 1, 7, 17, 0),
    value=datetime(2020, 1, 3, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

# ========== st.line_chart ========== 
st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)
