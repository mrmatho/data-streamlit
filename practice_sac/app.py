import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Education and Economics")
st.subheader("Population, GDP and Primary Education Completion")

# Load GDP Summary Stats data

summary_stats = pd.read_csv("gdp_pop_summary.csv")
st.write(summary_stats)