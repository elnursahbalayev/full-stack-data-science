from pkgutil import get_data
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from PIL import Image

st.title('Streamlit app')

st.write('## A simple Data App with Streamlit')

st.write("""
         ### Let's explore different classifiers and datasets
         """)

dataset_name = st.sidebar.selectbox('Select a dataset', options=['Breast Cancer','Iris', 'Wine'])

classifier_name = st.sidebar.selectbox('Select a classifier',options=['SVM','KNN'])

def get_dataset(name):
    """Gets the dataset name from sidebar and gives back the dataframe itself"""
    data = None
    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    x = data.data
    y = data.target
    
    return x, y

x, y = get_dataset(dataset_name)
st.dataframe(x)
st.write('Shape of the dataset: ', x.shape)
st.write('Unique target variables: ', len(np.unique(y)))

fig = plt.figure()
sns.boxplot(data=x, orient='h')
st.pyplot(fig)

fig = plt.figure()
plt.hist(x)
st.pyplot(fig)

def add_parameter(name_of_clf):
    params = dict()
    if name_of_clf == 'SVM':
        c = st.sidebar.slider('Choose penalty',0.01,15.0)
        params['c'] = c
    else:
        k = st.sidebar.slider('Choose k', 1, 15)
        params['k'] = k
    return params
params = add_parameter(classifier_name)

def get_classifier(name_of_clf, params):
    clf = None
    
    if name_of_clf == 'SVM':
        clf = SVC(C=params['c'])
    else:
        clf = KNeighborsClassifier(n_neighbors=params['k'])
        
    return clf

clf = get_classifier(classifier_name, params)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=123)


clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

df_results = pd.DataFrame([y_pred, y_test], index=['y_pred', 'y_test'])
st.dataframe(df_results)

accuracy = accuracy_score(y_test, y_pred)

st.write('Accuracy = ',accuracy)
