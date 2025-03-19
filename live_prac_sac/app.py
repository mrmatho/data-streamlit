import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Education and Economy", 
    page_icon="📊",
    layout="wide")
# Load the dataset
@st.cache_data
def load_data():
    prim = pd.read_csv('gdp_pop_primary.csv')
    sum = pd.read_csv('gdp_pop_summary.csv')
    time_df = pd.read_csv('primary_country_time.csv')
    return prim, sum, time_df

prim_df, sum_df, time_df = load_data()

# Title and subtitle
st.title("Education and Economy")
st.subheader("Population, GDP and Primary Education Completion")

# st.dataframe(sum_df, use_container_width=True)

col1, col2, col3 = st.columns(3)
with col1: 
    st.metric("Average GDP per Capita", 
              f"{sum_df['GDP Per Capita'][0]:.0f}",
              border=True)

with col2:
    st.metric("Minimum Primary Education Rate", 
              f"{sum_df['Primary Education Completion Rate'][2]:.1f}%",
              border=True)

with col3:
    st.metric("Maximum Primary Education Rate",
              f"{sum_df['Primary Education Completion Rate'][3]:.1f}%",
              border=True)

left_col, right_col = st.columns(2, border=True)
prim_df.sort_values(by="Country", inplace=True)
with left_col:
    st.subheader("Primary Education vs GDP Per Capita")
    fig = px.scatter(prim_df, x="GDP Per Capita",
               y="Primary Education Completion Rate",
               size="Population", color="Country")
    
    st.plotly_chart(fig)
    
with right_col:
    st.subheader("Primary Completion Rates in each Country")
    fig = px.bar(prim_df, x="Country",
                 y="Primary Education Completion Rate",
                 color="Population", text_auto='.2s')
    st.plotly_chart(fig)

countries = sorted(time_df['Country'].unique())
country_select = st.selectbox("Select a Country", countries)

small_c, large_c = st.columns(2)
filtered = time_df[time_df['Country'] == country_select]

with small_c:
    st.subheader(country_select)
    

with large_c:
    fig = px.line(filtered, 
                  x='Year',
                  y='Percent_completed',
                  markers=True,
                  labels="Percent_completed")
    st.plotly_chart(fig)