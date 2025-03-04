import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Meteorites",
    page_icon=":rock:",
    layout="wide",
)

# Load the meteorites dataset
meteorites = pd.read_csv("meteorites.csv")

# Put a title and description on the page
st.title("Meteorites")
st.write(
    "This is a simple Streamlit app that shows the landing position of meteorites. The data is loaded from a CSV file and plotted as a scatterplot (using latitude) and a map."
)

# Remove rows with missing values
meteorites.dropna(inplace=True)

# Plot the Scatterplot
st.header("Meteorites Scatterplot")
st.scatter_chart(meteorites, x="reclong", y="reclat", size="year", height=700)

# Plot the Map
st.header("Meteorites Map")
st.map(meteorites, latitude="reclat", longitude="reclong")

# Show the data
st.header("Meteorites Data")
st.dataframe(meteorites, use_container_width=True)

