# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:26:45 2024

@author: Tanishq Salkar
"""
import streamlit as st 
import pandas as pd
import folium
import pandas as pd
import json
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

areas = list(df.city.unique())
areas.insert(0,'Los Angeles')
area_filter = st.sidebar.selectbox("Area",areas )
rent_filter = st.sidebar.slider("Rent: ",min_value=0,max_value=20000)

if area_filter != "Los Angeles":
    locations = df[(df['city'].str.contains(area_filter,case=False)) & (df['rent']>=rent_filter)][['latitude','longitude','rent']]
else:
    locations = df[ (df['rent']>=rent_filter)][['latitude','longitude','rent']]
#locations = df[(df['city'].str.contains(area_filter,case=False)) & (df['rent']>=rent_filter)][['latitude','longitude','rent']]
st.write(" ## Apartments listed for rent in Los Angeles")
st.map(locations)

#bus stops in LA

bus_stops = load_data2("bus_stops.xlsx")
bus_locations = bus_stops[['latitude','longitude']]
st.write(" ## BUS Stops in Los Angeles")
st.map(bus_locations,latitude=34.0522,longitude= -118.2437,zoom=11)

#Metro stops in LA

metro_stops = load_data2("metro_stops.xlsx")
metro_locations = metro_stops[['latitude','longitude']]
st.write(" ## Metro Stops in Los Angeles")
st.map(metro_locations)

## Crime Rate in LA Areas
st.subheader("Crime rate in Los Angeles Area wise")
st.sidebar.title("Crime Rate Settings")
min_threshold = st.sidebar.slider("Minimum Threshold", min_value=0, max_value=2000, value=730)
max_threshold = st.sidebar.slider("Maximum Threshold", min_value=0, max_value=2000, value=1300)
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
