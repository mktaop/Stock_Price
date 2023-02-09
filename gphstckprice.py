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


st.text('This is a quick demo of how to look up a stock price and graph it')
st.text('User can select between 3 daily data series to plot!')

stkopt=['AAPL','AMZN','GOOG','AMD']
stkslct=st.selectbox('which of these stocks would you like to retrieve info for?', stkopt)

df = yf.download(
    stkslct,
    start="2022-01-01",
    end="2023-01-31",
    progress=False,
)

st.write(df)

gph_options=['Open','High','Close']

#fig = px.line(df,x=df.index, y=gph_col, title='Daily AAPL Price', markers=True)
#fig.write_html('first_figurez.html', auto_open=True)


gph_col=st.selectbox('Which of these series would you like to see:', gph_options)
ttle='Daily price for: ' + stkslct

fig=px.line(df,x=df.index, y=gph_col, title=ttle, markers=True)

st.write(fig)