# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:54:34 2024

@author: Tanishq Salkar
"""
import streamlit as st 
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Analysing impact of crime rate and public transport accessibility on rent of apartments in Los Angeles! 👋")
st.subheader("by Tanishq Salkar")
st.sidebar.success("Select a page above.")

st.write(
    """
    ### About Project Data
    **🏠 Housing dataset** contains the name of the apartment, rent, number of bedrooms, number of bathrooms, address, and zip code.
    \n **🚇 LA metro stops dataset** – contains stop name, stop code, coordinates (latitude, longitude)
    \n **👥 Population dataset** – Area name, zip code, population
    \n **🚨 Crime dataset** – date occurred, crime, type of crime, the severity of the crime, coordinates (latitude, longitude), etc (downloaded from the website)
"""
)

st.write("""
         
    ### Pages in the Web App
    **Page 2** 📊 Explore parameters like home rent, crime rate, and bus stops through Exploratory Data Analysis (EDA). \n
    **Page 3** 🗺️ Visualize the distribution of apartments, crime rates, and the number of stops in Los Angeles on an interactive map. \n
    **Page 4** 📚 Discover the key insights and learning outcomes from the project. \n
         """)
         
#st.subheader("")