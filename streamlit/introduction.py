import streamlit as st


st.title('My first streamlit app')

from PIL import Image

st.subheader('This is a subheader')

st.write('Hello this is a text')

st.markdown("**this is a markdown text**")

st.success('this is a success function')

st.info('this is the info function')

st.warning('this is the warning function')

st.error('this is the error message')

st.help(print)

import numpy as np
import pandas as pd

df = np.random.rand(10, 20)

st.dataframe(df)


chart_data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.area_chart(chart_data)

st.bar_chart(chart_data)


import matplotlib.pyplot as plt


arr = np.random.normal(1, 1, size=100)

fig = plt.figure()
plt.hist(arr, bins=20)
st.pyplot(fig)

import plotly
import plotly.figure_factory as ff