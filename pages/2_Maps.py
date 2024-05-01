# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:26:45 2024

@author: Tanishq Salkar
"""
import streamlit as st 
import pandas as pd
import folium
import pandas as pd
from folium import plugins
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium


st.set_page_config(page_title="Maps", page_icon="🗺️")
def filter(string):
    string = string.replace(",","")
    return int(string)

@st.cache_data()
def load_data(path):
    df = pd.read_excel(path)
    df['rent'] = df['rent'].apply(filter)
    return df
@st.cache_data()
def load_data2(path):
    df = pd.read_excel(path)
    return df

df = load_data('Final_data_area.xlsx')
#Los Angeles Rental Insights: Maps of Apartments, Transit, and Crime Rates
st.markdown("<h2 style='text-align: justify;'>🗺️Los Angeles Rental Insights: Maps of Apartments, Transit 🚌, and Crime Rates 🚨</h2>", unsafe_allow_html=True)
areas = list(df.city.unique())
areas.insert(0,'Los Angeles')
area_filter = st.sidebar.selectbox("Area",areas )
rent_filter = st.sidebar.slider("Rent: ",min_value=0,max_value=20000)

if area_filter != "Los Angeles":
    locations = df[(df['city'].str.contains(area_filter,case=False)) & (df['rent']>=rent_filter)][['latitude','longitude','rent']]
else:
    locations = df[ (df['rent']>=rent_filter)][['latitude','longitude','rent']]
#locations = df[(df['city'].str.contains(area_filter,case=False)) & (df['rent']>=rent_filter)][['latitude','longitude','rent']]
st.write(" ### 🏢 Apartments listed for rent in Los Angeles")
st.map(locations)
st.write("The above maps showcase apartments available for rent in Los Angeles, offering the flexibility to filter based on rent range and locality.")
#bus stops in LA

bus_stops = load_data2("bus_stops.xlsx")
bus_locations = bus_stops[['latitude','longitude']]
st.write(" ## 🚍 Bus Stops in Los Angeles")
st.map(bus_locations,latitude=34.03,longitude= -118.15,zoom=11)
st.write("The map above displays all the bus stops across Los Angeles. It's clear from the map that the bus services cover the entire city, offering robust connectivity and easy public transport accessibility throughout Los Angeles.")
#Metro stops in LA

metro_stops = load_data2("metro_stops.xlsx")
metro_locations = metro_stops[['latitude','longitude']]
st.write(" ## 🚇 Metro Stops in Los Angeles")
st.map(metro_locations)
st.write("The Los Angeles Metro Rail is made up of 6 lines and 93 stations. Although it doesn't cover the entire city, its tracks are 169 kilometres long and run from north to south and from east to west.")
## Crime Rate in LA Areas
st.subheader("Crime rate in Los Angeles Area wise 🚨🚓")
st.sidebar.header("Crime Rate per 10000 people Settings")
min_threshold = st.sidebar.slider("Minimum Crime Rate", min_value=0, max_value=2000, value=730)
max_threshold = st.sidebar.slider("Maximum Crime Rate", min_value=0, max_value=2000, value=1300)
radius = st.sidebar.slider("Marker Radius", min_value=50, max_value=200, value=67)
threshold = (min_threshold, max_threshold)
df2 = df[["city","latitude","longitude","crime_rate"]]
grouped_df = df2.groupby("city", as_index=False).mean()
# Define a color function
def getColor(crime_rate):
    if crime_rate < 730:
        return 'green'
    elif threshold[0] <= crime_rate < threshold[1]:
        return 'yellow'
    else:
        return 'red'
map = folium.Map(location=[34.0522, -118.2437], zoom_start=12)

# Add markers with crime rates
marker_cluster = MarkerCluster().add_to(map)
for index, row in grouped_df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=radius,  # Adjust the radius as needed
        color=None,
        fill=True,
        fill_opacity=0.6,
        fill_color=getColor(row['crime_rate']),
        tooltip=f"City: {row['city']} \n Crime Rate: {round(row['crime_rate'])}"
    ).add_to(marker_cluster)
#Zip Code: {row['zip_code']},
# Display the map in Streamlit
#map.save('laHeatmap.html')

st_folium(map,width=1000,)
st.write("In the map above, we can observe the crime rate for each locality within the city of Los Angeles🔍. Red circles 🟥 indicate areas with a high crime rate, signifying an unsafe locality. 🚨 Yellow circles 🟡 denote moderate yet unsafe crime rates, while green circles 🟢 indicate relatively low crime rates in the area. Please note that the colors and crime rate indications are relative to the city of Los Angeles and are plotted based on observed crime rates in Los Angeles in the year 2023.")


st.write("The sidebar features filters allowing control over thresholds to identify safe, unsafe, and very unsafe zones in Los Angeles. Additionally, users can manipulate the radius of the locality to obtain an overall crime rate for the region. 🛡️")