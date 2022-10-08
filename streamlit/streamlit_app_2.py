import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import model_selection

matplotlib.use('Agg')

from PIL import Image


st.title('Data Science app')

def main():
    activities = ['EDA', 'Visualization', 'Modelling and prediction', 'About us']
    option = st.sidebar.selectbox('Select one: ',activities)
    
    if option == 'EDA':
        st.subheader('Exploratory Data Analysis')
        
        data = st.file_uploader('Upload a dataset please',type=['csv', 'xlsx', 'txt', 'json'])
        
        if data is not None:
            st.success('File uploaded successfully')
            df = pd.read_csv(data)
            st.dataframe(df.head(20))
            
            if st.checkbox('Display shape'):
                st.write(df.shape)
                
            if st.checkbox('Display column names'):
                st.write(df.columns)
            
            if st.checkbox('Select multiple columns'):
                selected_columns = st.multiselect('Select preferred columns:', df.columns)
                df_1 = df[selected_columns]
                st.dataframe(df_1)
                
            if st.checkbox('Display summary'):
                st.write(df.describe().T)
            
            if st.checkbox('Display number of null values'):
                st.write(df.isnull().sum())
                
            if st.checkbox('Display data types'):
                st.write(df.dtypes.astype(str))
                
            if st.checkbox('Display correlation of data columns'):
                st.write(df.corr())
        
    elif option == 'Visualization':
        st.subheader('Visualization')
        
    elif option == 'Modelling and prediction':
        st.subheader('Modelling and prediction')
        
    elif option == 'About us':
        st.subheader('About us')
    
if __name__ == '__main__':
    main()