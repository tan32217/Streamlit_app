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

st.write("# Analyzing the impact of crime rate and public transport accessibility on apartment rent in Los Angeles! 🌴  🌇 🌉 🎢 🌞 🌊 🎥")
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

st.subheader("Explanation of web app !!")
st.write("""
         In this project, I have conducted visualizations 📊 of apartments listed for rent in Los Angeles, as well as the number of bus 🚌 and metro 🚇 rail stops, and crime rates 🚨 for each locality displayed on maps. Utilizing Plotly charts, I have depicted the distribution of the number of bedrooms and bathrooms for the apartments.

Furthermore, I employed a heatmap 🔥 to comprehend the correlations between several features that were extracted. Additionally, through Seaborn's regplot function, I drew regression lines for various features such as rent vs. crime rate, rent vs. number of bus stops, and rent vs. number of metro stops.

To enhance user experience and analytical capabilities, I incorporated filters in the sidebar. These filters allow users to specify minimum and maximum rent values, select specific areas for crime analysis, and choose the number of bedrooms for correlation analysis of rent with other factors. 🛏️🔍
         
         """)
         
st.subheader("Major “gotchas” ")

st.write("""In this project, I encountered challenges while working with mapbox and folium. While visualizing crime rates on a map, I initially intended to utilize mapbox but had to resort to folium instead. Additionally, I aimed to create multiple regression lines on a Plotly chart for different bedroom types of apartments. \n However, I found that achieving this task became too cluttered visually. Despite attempting to address this using seaborn and the hue attribute, the visual clarity remained compromised. These were some of the significant challenges I encountered during this project.""")