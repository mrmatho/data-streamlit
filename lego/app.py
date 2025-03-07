# import streamlit, pandas and ipyvizzu

import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget

st.set_page_config(
    page_title="Lego",
    page_icon=":bar_chart:",
    layout="wide")

st.title("Lego")

def create_chart():
    # initialize Chart
    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )
    # create and add data to Chart
    data = Data()
    df = pd.read_csv("./sets.csv")
    df = df[df["num_parts"] > 100]
    df = df[df['year'] > 2000]
    data.add_df(df)
    st.dataframe(df)
 
    chart.animate(data)
 
    # add config to Chart
 
    chart.animate(
        Config.stackedBubble(
            {
                "size": "num_parts",
                "title": "Lego Sets",
                "stackedBy": "year"
            }
        )
    )
    chart.animate(Style({"title": {"fontSize": 35}}))

 
    # return generated html code
 
    return chart._repr_html_()
 
 
# generate Chart's html code
 
CHART = create_chart()
 
 
# display Chart
 
html(CHART, width=650, height=570)