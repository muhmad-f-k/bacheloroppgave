import streamlit as st
import random

# Generate random data
data = [[random.randint(0, 100) for _ in range(10)] for _ in range(3)]

def home_page():
  st.title("Bachelor thesis for group 14")
  st.write("Welcome!")
  st.markdown("Random chart to test the performance")
  # Create the line chart
  st.line_chart(data)
  
  