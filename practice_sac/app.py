import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Education and Economics", page_icon=":books:")

st.title("Education and Economics")
st.subheader("Population, GDP and Primary Education Completion")



# Load GDP Summary Stats data

summary_stats = pd.read_csv("gdp_pop_summary.csv")

# st.write(summary_stats)

c1, c2, c3 = st.columns(3)
c1.metric("Mean GDP", summary_stats["GDP"][0])
c2.metric("Primary Education Rate (Minimum)", f"{summary_stats["Primary Education Completion Rate"][2]}%")
c3.metric("Primary Education Rate (Maximum)", f"{summary_stats["Primary Education Completion Rate"][3]}%")

st.divider()

# Load GDP  data
df = pd.read_csv("gdp_pop_primary.csv")
col1, col2 = st.columns(2)

col1.subheader("GDP per Capita to Primary Education")

fig = px.scatter(df, x="GDP Per Capita", y="Primary Education Completion Rate", color="Country", size="Population", hover_name="Country", log_x=True, size_max=60)
col1.plotly_chart(fig)
col1.caption("Bubble size represents the population of the country. ")

col2.subheader("Primary Education")

fig = px.bar(df, x="Country", y="Primary Education Completion Rate", color="Country", title="Primary Education Completion Rate by Country")
col2.plotly_chart(fig)

st.divider()

# Load primary country data over time
df = pd.read_csv("primary_country_time.csv")
st.subheader("Primary Education Completion Rates")
st.markdown("**Select a country** to view the completion rate over time.")
# Select country
countries = df["Country"].unique()
countries = sorted(list(countries))
selected_country = st.selectbox("Country", countries, index=None)
if selected_country:
    col4, col5 = st.columns([0.3, 0.7])
    filtered_df = df[df["Country"] == selected_country].sort_values("Year", ascending=False)
    
    col4.header(selected_country)
    col4.metric("Mean Completion Rate", filtered_df["Percent_completed"].mean())
    year = str(filtered_df["Year"].iloc[0]) + " Completion Rate"
    col4.metric(year, filtered_df["Percent_completed"].iloc[0])

    fig = px.line(filtered_df, x="Year", y="Percent_completed", title=f"Primary Education Completion Rate in {selected_country}")
    col5.plotly_chart(fig)
