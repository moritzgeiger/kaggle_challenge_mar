## DF AND VISUALIZATION
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

## DEPLOYMENT
import streamlit as st
import os

### FUNCTIONS AND CLASSES ###

from kaggle_challenge_mar.pipeline import Predictor

def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv()

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

### FRONTEND ###
st.set_page_config(
            page_title="Kaggle Challenge Predictor",
            layout="centered",
            initial_sidebar_state="auto")

st.header("""**Kaggle Challenge Predictor**""")
st.subheader("""Tabular Playground Series - Mar 2021""")
st.markdown("""This project is is a simple predictor frontend for the open Kaggle Playground Challenge of March 2021""")
with st.beta_expander('''How can I use this?'''):
        st.markdown("""
                    - Go to the Challenge on Kaggle: <a href="https://www.kaggle.com/c/tabular-playground-series-mar-2021" target=blank>Link</a>
                    - Download the test.csv file from there
                    - upload it here and click Predict & Download
                    - You will have the predictions ready for submission dowmloaded""", unsafe_allow_html=True)

with st.beta_expander('''The model'''):
        st.markdown('''
                    -  As a final estimator the RandomForestClassifier from ScikitLearn is chosen.
                    -  To balance the input data the oversampling techinque of SMOTE is used.
                    -  The current Kaggle score is 0.77836 and may be improved in the upcoming days.
                    ''')

### PREDICTOR ###
st.subheader("""The Predictor""")
X_test = st.file_uploader("Choose the csv of the Kaggle challenge to predict", type=['csv'])

if X_test:
    if st.button('Predict & Download as CSV'):
        print('predicting...')
        predictor = Predictor(X_test)
        y_pred = predictor.predict()
        # st.write(y_pred)
        tmp_download_link = download_link(y_pred, 'submission.csv', 'Click here to download your data!')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    else:
        st.write('Click "Predict & Download"')



with st.beta_expander('''Credits'''):
        st.markdown('''
                    Made by: Moritz Geiger <br>
                    Visit my GitHub Page: <a href="https://github.com/moritzgeiger/kaggle_challenge_mar" target=blank>here</a>
                    ''', unsafe_allow_html=True)


