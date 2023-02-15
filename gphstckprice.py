#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:27:30 2023

@author: avi_patel
"""

import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu  

page_title="Stock Info & Chart - Select a stock symbol from the drop down menu"
page_icon=":chart_with_upwards_trend:"
layout="centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_icon + " " + page_title)

selected = option_menu(
    menu_title=None,
    options=["Table", "Visualization"],
    icons=["pencil-fill","bar-chart-fill"],
    orientation="horizontal"
    )

stkopt=[' ','AAPL','AMZN','GOOG','AMD']
stkslct=st.selectbox('Which of these stocks would you like to retrieve info for?', stkopt)
if stkslct==' ':
    pass
else:
    df = yf.download(stkslct,start="2022-01-01",end="2023-01-31",progress=False,)

if selected == "Table":

 
    if stkslct==' ':
        pass
    else:
        msg1="This is a data table for: " + stkslct
        st.text(msg1)
        st.write(df)

if selected == "Visualization":
    

    
    if stkslct==' ':
        pass
    else:
        msg2="This is a daily chart for: " + stkslct
        st.text(msg2)
        df=df.sort_index(axis = 0,ascending=False)
        gph_options=['Open','High','Close']
        gph_col=st.selectbox('Which of these series would you like to see:', gph_options)
        ttle='Daily price for: ' + stkslct
        
        fig=px.line(df,x=df.index, y=gph_col, title=ttle, markers=True)
        
        st.write(fig)