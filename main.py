import streamlit as st
import pandas as pd
import numpy as np


st.title('Just a test')

st.title('Simple Streamlit App')

st.text('Type a number in the box below')

n = st.number_input('Number', step=1)

st.write(f'{n} + 1 = {n+1}')

s = st.text_input('Type a your name in the box below')

st.write(f'Hello {s}')