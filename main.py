import requests
import keys
import nasdaqdatalink
import quandl
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime, timedelta
import pandas as pd
import math

#URL for the JSON
# url = f"https://data.nasdaq.com/api/v3/datasets/USTREASURY/YIELD.json?api_key={keys.NASDAQ_API_KEY}"

# data = requests.get(url)

# print(type(data.json()))

#QUANDL
data = quandl.get("USTREASURY/YIELD", authtoken = keys.NASDAQ_API_KEY)

recessionList = [[datetime.strptime("1990-07-01", "%Y-%m-%d").date(), datetime.strptime("1991-03-31", "%Y-%M-%d").date()],
[datetime.strptime("2001-03-01", "%Y-%m-%d").date(), datetime.strptime("2001-11-31", "%Y-%M-%d").date()],
[datetime.strptime("2007-12-01", "%Y-%m-%d").date(), datetime.strptime("2009-06-30", "%Y-%M-%d").date()],
[datetime.strptime("2020-02-01", "%Y-%m-%d").date(), datetime.strptime("2020-04-30", "%Y-%M-%d").date()]]



def draw(data = data):
    #TODO: implement daily check mechanism
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


    #LINE
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

    #combining the graphs
    fig3 = go.Figure(data = fig1.data + fig2.data, layout = fig1.layout)

    #update axes
    fig3.update_xaxes(title_text = "Bond Length",
    title_font = {"size": 40}, tickfont = {"size": 30})
    fig3.update_yaxes(title_text = "Yield",
    title_font = {"size": 40}, tickfont = {"size": 30})

    # fig.update_layout(paper_bgcolor = "black")
    fig3.show()

def closest(data = data):
    dataREV = data.iloc[::-1]

    end_date = pd.to_datetime(date.today() - timedelta(days = 1825))

    dataREV = dataREV[(dataREV.index >= '1990-01-02') & (dataREV.index<= end_date)]

    #!!! FORMULA POSITIONING
    dataREV["Diff"] = abs((data['10 YR'].iloc[-1] - data['2 YR'].iloc[-1]) - (dataREV['10 YR'] - dataREV['2 YR']))
    
    return dataREV['Diff'].idxmin()

def graphs(data = data):
    target = closest()
    close = data.loc[[target]]
    print(close)

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
    text = "--- " + str(date.today()), showarrow = False)


    fig5.show()

def days(listed = recessionList):
    dist = math.inf
    target = closest().date()
    for rec in listed:
        if ((target - rec[0]).days >= 0) and ((target - rec[1]).days) <= 0:
            return "In a recession!"
        dist = min(dist, abs((rec[0] - target).days))
    
    return f"{dist} days away"


print(days())