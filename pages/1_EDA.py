# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:27:34 2024

@author: Tanishq Salkar
"""
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.figure_factory as ff
# Load the dataset
st.set_page_config(page_title="EDA", page_icon="📊")
st.set_option('deprecation.showPyplotGlobalUse', False)
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

df2 = load_data('Final_data_area.xlsx')
df3 = load_data('Final_data_area.xlsx')
#df_crime_data = load_data2("crime_data_final.xlsx")
df_crime_data_area_count = load_data2("crime_data_area_count.xlsx")

# df2['rent'] = df2['rent'].apply(filter)
# df['price'] = df['price'].apply(filter)

# st.write('''
#          ## Analysing impact of crime rate and public transport accessibility on rent of apartments in Los Angeles
#          ''')
st.markdown("<h2 style='text-align: justify;'> EDA: Exploring the data</h2>", unsafe_allow_html=True)
st.subheader("Apartments for Rent")

st.sidebar.header("Filter")

areas = list(df.city.unique())
areas.insert(0,'')
area_filter = st.sidebar.selectbox("Area",areas )
rent_filter = st.sidebar.slider("Rent: ",min_value=1000,max_value=20000)

filtered_df = df[(df['city'].str.contains(area_filter,case=False)) & (df['rent']>=rent_filter)][['apt_name','city','zip_code','bedroom','bathroom','rent']]
st.write(filtered_df)

# Create two columns
col1, col2 = st.columns(2)


# Chart 1 in first column
with col1:
    st.subheader("Number of bedrooms of apartment for rent")
    no_of_bedrooms_count = df2['bedroom'].value_counts()
    no_of_bedrooms_count.sort_values(inplace=True)
    fig = px.pie(no_of_bedrooms_count, values='count', names=no_of_bedrooms_count.index, title='Number of bedrooms of apartment for rent')
    st.plotly_chart(fig,use_container_width=True)
    
with col2:
    st.subheader("Number of bathrooms of apartment for rent")
    no_of_bathroom_count = df2['bathroom'].value_counts()
    no_of_bathroom_count.sort_values(inplace=True)
    fig = px.pie(no_of_bathroom_count, values='count', names=no_of_bathroom_count.index, title='Number of bathroom of apartment for rent')
    st.plotly_chart(fig,use_container_width=True)

st.sidebar.header('Rent by Area and type Filters')
overall_average = st.sidebar.checkbox('Overall Average')
apartment_type_list = list(df.bedroom.unique())

apartment_type = st.sidebar.selectbox('Apartment Type', ['1 Bedroom', '2 Bedrooms', '3 Bedrooms', '4 Bedrooms', '5 Bedrooms'])

map_dict = {
    '1 Bedroom':1,
    '2 Bedrooms':2,
    '3 Bedrooms':3,
    '4 Bedrooms':4,
    '5 Bedrooms':5
    }
# Calculate overall average rent
if overall_average:
    overall_avg_rent = df[df['bedroom']==map_dict[apartment_type]]['rent'].values.mean()
    st.sidebar.write(f'Overall Average Rent: ${overall_avg_rent:.2f}')
    
st.subheader("Average Rent by City and Number of Bedrooms")
average_rent = df.groupby(['city', 'bedroom'])['rent'].mean().reset_index()
# Pivot the DataFrame to have number_of_bedrooms as columns
average_rent_pivot = average_rent.pivot(index='city', columns='bedroom', values='rent')
average_rent_pivot = average_rent_pivot.reindex(columns=range(1, 13), fill_value=0)

# Create a list of bar traces for each number of bedrooms
slider_value = st.slider('Select number of bedrooms', min_value=1, max_value=12, value=5, step=1)
data = []
for num_bedrooms in range(1, slider_value+1):
    data.append(go.Bar(x=average_rent_pivot.index, y=average_rent_pivot[num_bedrooms], name=f'{num_bedrooms} Bedroom'))

# Plotting
# Create Plotly figure
fig = go.Figure(data=data)
fig.update_layout(barmode='stack',xaxis_title='City', yaxis_title='Average Rent')
fig.update_layout(xaxis=dict(tickangle=45),height=700, width=900) 

# Streamlit app
st.plotly_chart(fig)

st.subheader("Scatter Plot of Rent vs Crime Rate")
df_og = df2[df2["rent"]<100000]
fig = px.scatter(df_og, x='crime_rate', y='rent', hover_data=['apt_name', 'address'], color='city', title='Rent vs Crime Rate')
fig.update_layout(height=500, width=900) 
st.plotly_chart(fig)

df_heat_map = df2[['latitude','longitude', 'rent', 'bedroom', 'bathroom', 'population', 'crime_rate']]
st.subheader("Correlation of Features")
corr = df_heat_map.corr()
corr_rounded = corr.round(2)
# Create an interactive heatmap using Plotly
heatmap_fig = ff.create_annotated_heatmap(z=corr_rounded.values, x=corr_rounded.columns.tolist(), y=corr_rounded.columns.tolist(), colorscale='RdBu_r', showscale=True)
# Update layout
heatmap_fig.update_layout(title="Heatmap", xaxis_title="Features", yaxis_title="Features")
# Display the heatmap
st.plotly_chart(heatmap_fig)

# Donut chart for crimes in LA
#converting date to pandas datetime format
#crime_counts = df_crime_data.groupby(['AREA_NAME', 'Crm_Cd_Desc']).size().reset_index(name='count')
# Plotting a donut chart using Plotly
#fig = px.sunburst(crime_counts, path=['AREA_NAME', 'Crm_Cd_Desc'], values='count', color_continuous_scale='RdBu', title='Crime Distribution by Area and Crime Type')

#***********************************************************************************************************************************
st.subheader("Crime Analysis !!!")
# Group by area name and crime type
df_grouped = df_crime_data_area_count.groupby(['AREA_NAME', 'Crm_Cd_Desc']).sum().reset_index()

# Function to create Plotly bar chart
def create_bar_chart(df, x_col, y_col, color_col, title):
    fig = px.bar(df, x=x_col, y=y_col, color=color_col, barmode='group', title=title)
    return fig

# Function to create Plotly pie chart
def create_pie_chart(df, labels_col, values_col, title):
    fig = px.pie(df, names=labels_col, values=values_col, title=title)
    return fig

# Sidebar multiselect for area selection
selected_areas = st.multiselect("Choose Area", df_grouped['AREA_NAME'].unique())

# Filter DataFrame based on selected areas
df_filtered = df_grouped[df_grouped['AREA_NAME'].isin(selected_areas)]

# Filter DataFrame to select top 5 crime types for each area
top_crime_types = df_filtered.groupby('AREA_NAME')['count'].nlargest(5).reset_index(level=0, drop=True).index
df_filtered_top5 = df_filtered.loc[top_crime_types]

# Display bar chart
st.write("## Crime Analysis by Area and Crime Type (Top 5)")
st.plotly_chart(create_bar_chart(df_filtered_top5, 'AREA_NAME', 'count', 'Crm_Cd_Desc', 'Crime Count by Area and Crime Type'))
# PIE ***********************************************************************************************************************************

total_counts = df_filtered.groupby('AREA_NAME')['count'].sum().reset_index()
df_filtered_pie = df_filtered.copy()
# Calculate percentage of each crime type
df_filtered_pie = df_filtered_pie.merge(total_counts, on='AREA_NAME', suffixes=('', '_total'))
df_filtered_pie['percentage'] = df_filtered_pie['count'] / df_filtered_pie['count_total'] * 100

# Replace crime types with percentage less than 1% with 'Others'
df_filtered_pie.loc[df_filtered_pie['percentage'] < 2, 'Crm_Cd_Desc'] = 'Others'

# Group by area name and updated crime description
df_grouped_filtered = df_filtered_pie.groupby(['AREA_NAME', 'Crm_Cd_Desc'])['count'].sum().reset_index()

# Plot pie chart
st.subheader("Total Crime Count by Crime Type")
st.plotly_chart(create_pie_chart(df_grouped_filtered, 'Crm_Cd_Desc', 'count', 'Total Crime Count by Crime Type'))
# # Display pie chart
# st.subheader("Total Crime Count by Crime Type")
# st.plotly_chart(create_pie_chart(df_filtered, 'Crm_Cd_Desc', 'count', 'Total Crime Count by Crime Type'))

#******************************************************************************************************************
# Calculate correlation coefficient for Rent vs crime rate - CHANGE DF2 variable name later on....
# Set seaborn style
sns.set_style("whitegrid")
df_temp = df2.copy()
df2 = df2[df2['bedroom']==map_dict[apartment_type]]

df_corr_rent = df2.copy()
df_corr_rent['scaled_crime_rate'] = df_corr_rent['crime_rate'] /10000  # Adjust the scaling factor as needed
# Manipulate the rent column
df_corr_rent['manipulated_rent'] = df_corr_rent['rent'] - np.where((df_corr_rent['scaled_crime_rate'] * df_corr_rent['rent']) > 0, 
                                                df_corr_rent['scaled_crime_rate'] * df_corr_rent['rent'], 
                                               0)
corr_coef = df_corr_rent['manipulated_rent'].corr(df_corr_rent['crime_rate'])

# Display correlation coefficient
st.write(f"### Correlation Coefficient Rent vs Crime Rate")
st.subheader(f"Correlation Coefficient for {apartment_type}: {round(corr_coef,3)} ")
# Create scatter plot
plt.figure(figsize=(8, 6))
sns.regplot(data=df_corr_rent, x='manipulated_rent', y='crime_rate')
plt.title('Rent vs Crimes per 10000')
plt.xlabel('Rent')
plt.ylabel('Crimes per 10000')
plt.grid(True)

# Display plot
st.pyplot(plt)

# Corelation coefficient for Rent vs No of bus stops in 1 mile proximity
corr_coef2 = df2['rent'].corr(df2['bus_stops_near_apt'])

# Display correlation coefficient
st.write("### Rent VS No of Bus Stops")
st.subheader(f"Correlation Coefficient for {apartment_type}: {round(corr_coef2,3)} ")
# Create scatter plot
plt.figure(figsize=(8, 6))
sns.regplot(data=df2, x='rent', y='bus_stops_near_apt',scatter_kws={'alpha':0.5}) 
plt.title('Rent vs No. of Bus Stops')
plt.xlabel('Rent')
plt.ylabel('Number of bus stops')
plt.grid(True)

# Display plot
st.pyplot(plt)

# Corelation coefficient for Rent vs No of METRO stops in 1 mile proximity
corr_coef2 = df2['rent'].corr(df2['metro_stops_near_apt'])

# Display correlation coefficient
st.write("### Rent VS No of Metro Rail Stops")
st.subheader(f"Correlation Coefficient for {apartment_type}: {round(corr_coef2,3)} ")
# Create scatter plot
plt.figure(figsize=(8, 6))
sns.regplot(data=df2, x='rent', y='metro_stops_near_apt',scatter_kws={'alpha':0.5}) 
plt.title('Rent vs No. of METRO Stops')
plt.xlabel('Rent')
plt.ylabel('Number of METRO stops')
plt.grid(True)
# Display plot
st.pyplot(plt)