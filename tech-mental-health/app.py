import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Technology and Mental Health",
    page_icon=":brain:",
    layout="wide"
)

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("mental_health_and_technology_usage_2024.csv")
    return df

# Load the data
df = load_data()

# Title and reference
st.title("Technology and Mental Health")
st.write(
    "**Source:** *Ali, W.* Mental Health and Technology Usage 2024 [Dataset]. Kaggle. https://www.kaggle.com/datasets/mentalhealth/technology-and-mental-health"
)

st.dataframe(df)

# Histogram of numerical columns
st.header("Distribution of Numerical Columns")
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numerical_cols:
    st.subheader(f"Distribution of {col}")
    fig = px.histogram(df, x=col, title=f"Distribution of {col}")
    st.plotly_chart(fig, use_container_width=True)

# Correlation heatmap
st.header("Correlation Heatmap")
correlation_matrix = df.corr()
fig = px.imshow(correlation_matrix, text_auto=True, title="Correlation Heatmap")
st.plotly_chart(fig, use_container_width=True)