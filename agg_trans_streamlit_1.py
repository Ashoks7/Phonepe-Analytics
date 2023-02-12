# Import packages

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu


# Read file

agg_trans = pd.read_csv("df3.csv")

# Add back ground image

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.treebo.com%2Fblog%2Ftc-for-phonepe-app-sale%2F&psig=AOvVaw2bJZiIqYEhmnoOlYPnmyWy&ust=1676269097233000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCPDf8ueqj_0CFQAAAAAdAAAAABAR.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# Title of the page

st.title("Phonepe Analytics")

# Add option menu

selected = option_menu(menu_title=None, options=["map","statewise","yearwise","quaterwise"], icons=["clipboard-data","award","capslock-fill","coin"], orientation="horizontal")

# Code for map page
if selected=="map":
    df=pd.read_csv("df3.csv")

    


    fig = px.choropleth(
       df,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color='count',
       color_continuous_scale='Redor'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    
    st.write("Indian State wise Total Transaction Count 2018-2022")
    st.write(fig)
