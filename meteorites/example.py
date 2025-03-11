import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the app
st.set_page_config(page_title="Meteorite Landings", layout="wide")
st.title("Meteorite Landings")

# Load the data
df = pd.read_csv("meteorites.csv")
# Remove rows with missing values
df.dropna(inplace=True)

# We could do some filtering here, but we aren't right now

# Create a scatter plot
fig = px.scatter(df, x="year", y="mass", color="fall", hover_name="name")
fig.update_layout(title="Meteorite Landings", xaxis_title="Year", yaxis_title="Mass (g)")

# Display the plot
st.plotly_chart(fig, height=800)

# Display the data
st.write("Data:")
st.dataframe(df)