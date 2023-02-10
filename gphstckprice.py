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

header=st.container()
dataset=st.container()
graph=st.container()

with header:
    st.header('This is a quick demo of how to look up a stock price and graph it (courtesy: Yahoo Finance)')
    info='''First select a stock symbol, you will see a table of daily activities and also
select between 3 daily data series to plot!'''
    st.text(info)

with dataset:
    
    stkopt=[' ','AAPL','AMZN','GOOG','AMD']
    stkslct=st.selectbox('Which of these stocks would you like to retrieve info for?', stkopt)
 
    if stkslct==' ':
        pass
    else:
        df = yf.download(
            stkslct,
            start="2022-01-01",
            end="2023-01-31",
            progress=False,)
        df=df.sort_index(axis = 0,ascending=False)
        st.write(df)

    

with graph:
    
    if stkslct==' ':
        pass
    else:
        
        gph_options=['Open','High','Close']
        gph_col=st.selectbox('Which of these series would you like to see:', gph_options)
        ttle='Daily price for: ' + stkslct
        
        fig=px.line(df,x=df.index, y=gph_col, title=ttle, markers=True)
        
        st.write(fig)