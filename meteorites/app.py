import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page title, icon and layout
st.set_page_config(
    page_title="Meteorites",
    page_icon=":rock:",
    layout="wide"
)

# Load the meteorites dataset
meteorites = pd.read_csv("meteorites.csv")

# Remove rows with missing values
meteorites.dropna(inplace=True)

# Remove rows with mass <= 0
meteorites = meteorites[meteorites["mass"] > 0]

# Remove rows with reclat == 0 reclong == 0 (these are being used as defaults when the data is missing)
meteorites = meteorites[(meteorites["reclat"] != 0) & (meteorites["reclong"] != 0)]

# Put a title and description on the page
st.title("Meteorites")
st.write(
    "This is a simple Streamlit app that shows the landing position of meteorites. The data is loaded from a CSV file and plotted as a scatterplot (using latitude) and a map."
)
st.write("**Source:** King, E. & NASA. (2014). *Meteorite landings* [Dataset]. Kaggle. https://www.kaggle.com/datasets/nasa/meteorite-landings")

left_col, right_col = st.columns(2)

with left_col:
    # Have the user select a year range
    st.subheader("Filter by Year")
    min_year = st.number_input(
        "Minimum Year", min_value=int(meteorites["year"].min()),
        max_value=int(meteorites["year"].max()), value=int(meteorites["year"].min())
    )
    max_year = st.number_input(
        "Maximum Year", min_value=int(meteorites["year"].min()),
        max_value=int(meteorites["year"].max()), value=int(meteorites["year"].max())
    )
    # This is just for you 
    st.write(min_year, max_year)
    # Filter the dataframe based on the year range
    meteorites = meteorites[
        (meteorites["year"] >= min_year) & (meteorites["year"] <= max_year)
    ]

    # Plot the Scatterplot
    st.header("Meteorites Scatterplot")
    st.scatter_chart(meteorites, x="reclong", y="reclat", color="year", height=700)

with right_col:
    # Plot the Map
    st.header("Meteorites Map")
    st.map(meteorites, latitude="reclat", longitude="reclong")

    # Show the data
    st.header("Meteorites Data")
    st.dataframe(meteorites, use_container_width=True)

# Histograms
st.header("Distribution Shapes")

# Set number of bins. Range from 1 to 200, with a default of 20
bins = st.slider("Number of Bins", 1, 200, 20)

# Histograms into two columns
col1, col2 = st.columns(2)
with col1:
    st.subheader("Mass Histogram")
    # Each histogram needs the dataframe (meteorites), x for the column name and 
    # nbins for the number of bins. In this case we are also coloring by another column 
    fig = px.histogram(meteorites, x="mass", color="fall", nbins=bins)
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Latitude Histogram")
    fig = px.histogram(meteorites, x="reclat", nbins=bins)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Year Histogram")
    fig = px.histogram(meteorites, x="year", nbins=bins)
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Longitude Histogram")
    fig = px.histogram(meteorites, x="reclong", nbins=bins)
    st.plotly_chart(fig, use_container_width=True)
    
# Categorical Variables
col1, col2 = st.columns(2)

with col1:
    
    st.header("Categorical Variables")
    st.subheader("Fall")
    fig = px.bar(meteorites, x="fall")
    st.plotly_chart(fig, use_container_width=True)
    st.write("Bar chart using Plotly")
    # And using Streamlit default bar chart
    st.bar_chart(meteorites["fall"].value_counts())
    st.write("Bar chart using Streamlit default bar chart")
    
with col2:
    st.subheader("Class")
    fig = px.bar(meteorites, x="recclass", color="fall")
    st.plotly_chart(fig, use_container_width=True)
    st.write("Bar chart using Plotly")
    st.bar_chart(meteorites["recclass"].value_counts())
    st.write("Bar chart using Streamlit default bar chart")


