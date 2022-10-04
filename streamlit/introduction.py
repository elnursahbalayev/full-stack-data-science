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
# import plotly.figure_factory as ff

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200) 
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]
group_labes=['Group1', 'Group2', 'Group3']

df = pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76, -122.4], columns=['lat', 'lon'])

st.map()

# creating buttons
if st.button('Say hello'):
    st.write('hello is here')
else:
    st.write('wh are you here?')

genre = st.radio('What is a radio button?', options=['elnur', 'kamal', 'hesen', 'cemil'])

if genre=='elnur':
    st.write('oh you like elnur')
elif genre=='kamal':
    st.write('kamal maldi')

st.text('-'*83)

option = st.selectbox('how was your night', options=['fantastic', 'great', 'super'])
