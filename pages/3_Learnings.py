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
I wanted to study the impact of crime rate and public transport accessibility on the rent of apartments listed for rent in Los Angeles County. 
For that, I scraped 1000 apartments listed on Trulia.com. From there, I gathered information like the name of the apartment, address, rent, number of bathrooms, number of bedrooms, etc.
\nFrom a public API, I fetched the number of bus stops and metro rail stops in Los Angeles.
\nAdditionally, I obtained crime statistics for Los Angeles for the past 5 years from a public domain.
\nUsing the above data, I aimed to determine if there was any correlation between rent and crime or between rent and the number of stops in the vicinity of the apartment. 🏢🚍🚇🔍
""")
st.subheader("What did you Discover/what were your conclusions ?")
st.write("""
         Based on the analysis that was done on the data I found out that there was a slight negative correlation between crime rate and the rent of the apartment. \n
The number of bus stops and metro stops did not impact the rent as the correlation between them was of very small magnitude. The reason might be that when I visualized the number of bus stops in LA, I found out that each corner of the city was connected via bus which indicated uniform availability of public transportation. Hence it did not impact the rent of the apartment. \n
The highest correlation I observed was between rent and the number of bedrooms/bathrooms which is kind of obvious as it indicates a larger area hence higher rent. \n
Since this dataset only consisted of 1000 apartments, it might be a small sample to cover the entire Los Angeles city to get an accurate regression line between rent and crime rate. \n
Also, other factors like amenities,  parking, furnished/ not furnished, security deposit, pet-friendly apartments, etc can play a role in determining the overall rent.

         """)
st.subheader("What difficulties did you have in completing the project ?")
st.write("""
          
The most difficult part of the project was mapping crime rate area-wise on the map and then integrating it with the Streamlit app. Specifically for this problem, I had to use another library called Folium which was completely new to me. \n
 
Also in certain filters that multi-select I faced issues, initially I was using np. random to select localities in the city. However, each time I tried to change the areas, it used to get reset and random five areas were used to get selected in the filter. \n
 
In this project I extensively used Plotly to create interactive charts, it was completely new to me, and had to refer to online resources to guide me in visualization.

         """)
st.subheader("What skills did you wish you had while you were doing the projecty?")
st.write("""
         I wish I had more experience in visualization, especially in Plotly charts and in Folium and Mapbox. Also, more experience in Streamlit would have helped. \n
But certainly, this project has allowed me to learn new skills. It has helped to improve my skills in handling and manipulating Pandas data frames. It has helped me to elevate my data visualization skills. \n
Learning to build a streamlit app will help me to create powerful, customizable web interfaces with minimal code in the future.

         
         """)