import streamlit as st
from app_pages.home_page import home_page
from app_pages.contact_page import contact_page
from app_pages.about_page import about_page

def main():
  st.sidebar.title("Navigation")
  page = st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

  if page == "Home":
    home_page()
  elif page == "About":
    about_page()
  elif page == "Contact":
    contact_page()

if __name__ == "__main__":
  main()
