import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Questionnaire",
                   layout="wide",
                   page_icon=":question:")

st.title(":question: Questionnaire :question:")

@st.cache_data
def load_data():
    # Load the data from a CSV file
    df = pd.read_csv("Questionnaire.csv")
    return df

df = load_data()

st.dataframe(df)

# Create a bar chart of favorite colours
st.subheader("Favorite Colours and Foods")

fig = px.bar(df, x="Food", color="Colour") #, color_discrete_map={"blue": "blue", "white": "gray", "green": "green", "ultra-violet": "purple", "navy": "darkblue"},)
st.plotly_chart(fig, use_container_width=True)

# Create a scatterplot comparing People in house with Time away
st.subheader("People in House vs Time Away")
fig = px.scatter(df, x="DaysAway", y="PeopleInHouse", color="Food")
st.plotly_chart(fig, use_container_width=True)