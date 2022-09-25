import requests
import keys
import nasdaqdatalink
import quandl
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime, timedelta
import pandas as pd
import math
import closest
import data
import kaleido
import plotly.io as pio

def graphs(data = data.data):
    target = closest.closest()
    close = data.loc[[target]]

    #Figure for todays yield
    OneMO = data['1 MO'].iloc[-1]
    TwoMO = data['2 MO'].iloc[-1]
    ThreeMO = data['3 MO'].iloc[-1]
    SixMO = data['6 MO'].iloc[-1]
    OneYR = data['1 YR'].iloc[-1]
    TwoYR = data['2 YR'].iloc[-1]
    ThreeYR = data['3 YR'].iloc[-1]
    FiveYR = data['5 YR'].iloc[-1]
    SevenYR = data['7 YR'].iloc[-1]
    TenYR = data['10 YR'].iloc[-1]
    TwentyYR = data['20 YR'].iloc[-1]
    ThirtyYR = data['30 YR'].iloc[-1]

    fig1 = px.line(line_shape = "spline", 
    x = ['1M', '2M', '3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y'], 
    y = [OneMO, TwoMO, ThreeMO, SixMO, OneYR, TwoYR, ThreeYR, FiveYR, SevenYR, TenYR, TwentyYR, ThirtyYR], 
    template = "plotly_dark")

    
    #update the line
    fig1.update_traces(line_color = "#39FF14", line_width = 5)

    #SCATTER
    fig2 = px.scatter(x = ['1M', '2M', '3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y'], 
    y = [OneMO, TwoMO, ThreeMO, SixMO, OneYR, TwoYR, ThreeYR, FiveYR, SevenYR, TenYR, TwentyYR, ThirtyYR])

    #update the scatter
    fig2.update_traces(marker_size = 18, marker_color = "#39FF14")

    #Closest day
    fig3 = px.line(line_shape = "spline",
    x = ['1M', '2M', '3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y'],
    y = [close['1 MO'].iloc[-1], close['2 MO'].iloc[-1], close['3 MO'].iloc[-1],
    close['6 MO'].iloc[-1], close['1 YR'].iloc[-1], close['2 YR'].iloc[-1], close['3 YR'].iloc[-1],
    close['5 YR'].iloc[-1], close['7 YR'].iloc[-1], close['10 YR'].iloc[-1], close['20 YR'].iloc[-1],
    close['30 YR'].iloc[-1]], 
    template = "plotly_dark")


    fig3.update_traces(line_color = "#FF3131", line_width = 5)

    #SCATTER
    fig4 = px.scatter(x = ['1M', '2M', '3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y'], 
    y = [close['1 MO'].iloc[-1], close['2 MO'].iloc[-1], close['3 MO'].iloc[-1],
    close['6 MO'].iloc[-1], close['1 YR'].iloc[-1], close['2 YR'].iloc[-1], close['3 YR'].iloc[-1],
    close['5 YR'].iloc[-1], close['7 YR'].iloc[-1], close['10 YR'].iloc[-1], close['20 YR'].iloc[-1],
    close['30 YR'].iloc[-1]], template = "plotly_dark")

    fig4.update_traces(marker_size = 18, marker_color = "#FF3131")

    #COMBINING GRAPH
    fig5 = go.Figure(data = fig1.data + fig2.data + fig3.data + fig4.data, layout = fig1.layout)

    #update axes
    fig5.update_xaxes(title_text = "Bond Length",
    title_font = {"size": 40}, tickfont = {"size": 30})
    fig5.update_yaxes(title_text = "Yield",
    title_font = {"size": 40}, tickfont = {"size": 30})

    fig5.add_annotation(xref = "x domain",
    yref="y domain",
    x = 0.05,
    y = 0.95,
    font = {"color": "#FF3131", "size": 35},
    text = "--- " + str(target.date()), showarrow = False)

    fig5.add_annotation(xref = "x domain",
    yref="y domain",
    x = 0.05,
    y = 0.875,
    font = {"color": "#39FF14", "size": 35},
    text = "--- " + str(data.index[-1].date()), showarrow = False)

    pio.write_image(fig5, file=f"images/Graph{str(data.index[-1].date())}.png", width = 2544, height = 1185)
    fig5.show()