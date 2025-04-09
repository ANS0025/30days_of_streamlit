import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

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