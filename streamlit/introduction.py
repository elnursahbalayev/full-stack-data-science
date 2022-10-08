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

st.write('you said yoru night was ', option)

options = st.multiselect('how was your night multiselect?', options=['fantastic', 'great', 'super'])
st.write('you said your night was', options[0],' and ', options[1])

age = st.slider('How old are you?', min_value=1, max_value=100)
st.write(f'You are {age} years old')

values = st.slider('select a range of values',0, 100, (15,80))

st.write('you selected the range between:' ,values)

number = st.number_input('Please enter your birth year',)

st.write(f'You are {round(2022-number)} years old')

upload_file = st.file_uploader('Choose a csv file to upload',type='csv')

if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.write(data)
    st.success('successfully uploaded the csv file')
else:
    st.error('the file you uploaded is empty, please upload a valid file')
    
color = st.color_picker('Pick your preferred color:','#00f900')
st.write('This is the color you picked', color)

add_sidebar = st.sidebar.selectbox('What is your favorite course:', options=['A course from TDS on building web app', 'udemy course on full stack data science'])

import time
my_bar = st.progress(0)
for percent_complete in range(101):
    time.sleep(0.1)
    my_bar.progress(percent_complete)
    
with st.spinner('waiting for it'):
    time.sleep(5)
st.success('successfully done')
st.balloons()