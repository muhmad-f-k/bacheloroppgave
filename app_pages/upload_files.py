import pandas as pd
import streamlit as st
# Need openpyxl to be installed to work properly - pip install openpyxl


def load_file_and_read_file():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write(df)
