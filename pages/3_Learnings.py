# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:43:08 2024

@author: Tanishq Salkar
"""
import streamlit as st

st.set_page_config(page_title="Learnings", page_icon="📚")
st.write("# Learnings")

st.subheader("What did you set out to study?")
st.write("""

I aimed to study the impact of crime rate and public transport accessibility on the rent of apartments listed for rent in Los Angeles County. To achieve this, I scraped information from 1000 apartments listed on Trulia.com, gathering details such as the apartment name, address, rent, number of bathrooms, number of bedrooms, etc. 🏠

Furthermore, I retrieved data on the number of bus stops and metro rail stops in Los Angeles from a public API. 🚌🚇

Additionally, I collected crime statistics for Los Angeles for the past 5 years from a public domain. 🚨

With the gathered data, my objective was to determine if there was any correlation between rent and crime, or between rent and the number of stops in the vicinity of the apartment. 📊""")
st.subheader("What did you Discover/what were your conclusions ?")
st.write("""
    Based on the data analysis conducted, it was observed that there exists a slight negative correlation between the crime rate and the rent of apartments. 📉

Furthermore, the number of bus stops and metro stops showed minimal impact on rent, as their correlation with rent was of very small magnitude. This could be attributed to the extensive bus network observed across Los Angeles, connecting every corner of the city, thus ensuring uniform availability of public transportation, which consequently did not significantly affect apartment rent. 🚌🚇

The most prominent correlation observed was between rent and the number of bedrooms/bathrooms, which aligns with expectations, indicating that larger living spaces tend to command higher rents. 🛏️🚿

However, it's important to note that the dataset analyzed consisted of only 1000 apartments, which might not be sufficient to accurately represent the entire Los Angeles rental market and establish a robust regression line between rent and crime rate.

Moreover, factors such as amenities, parking availability, furnished or unfurnished status, security deposit requirements, and pet-friendliness of apartments can also influence overall rental prices, suggesting a more comprehensive analysis may be necessary to fully understand rent determinants. 🏠🔍
         """)
st.subheader("What difficulties did you have in completing the project ?")
st.write("""
          

The most challenging aspect of the project was mapping the crime rate area-wise on the map and then integrating it with the Streamlit app. Specifically for this task, I had to utilize another library called Folium, which was entirely unfamiliar to me.

Additionally, I encountered difficulties with certain multi-select filters. Initially, I attempted to utilize np.random to select localities in the city. However, whenever I attempted to modify the areas, the selections would reset, and five random areas would consistently be chosen in the filter.

Throughout this project, I extensively utilized Plotly to create interactive charts. Despite being a newcomer to this tool, I successfully navigated its usage by referencing online resources for guidance on data visualization.
         """)
st.subheader("What skills did you wish you had while you were doing the projecty?")
st.write("""
     
I wish I had more experience in visualization, particularly in creating Plotly charts and utilizing Folium and Mapbox. Additionally, more experience in Streamlit would have been beneficial. 📊🗺️

However, this project has provided me with the opportunity to acquire new skills. It has enhanced my proficiency in handling and manipulating Pandas data frames, as well as elevated my data visualization abilities. 📈📊

Mastering the creation of Streamlit apps will enable me to develop powerful, customizable web interfaces with minimal code in the future. 💻🚀
         """)