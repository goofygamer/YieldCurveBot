import requests
import keys
import nasdaqdatalink
import quandl
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime, timedelta
import pandas as pd
import math
import data

def closest(data = data.data):
    dataREV = data.iloc[::-1]

    end_date = pd.to_datetime(date.today() - timedelta(days = 1825))

    dataREV = dataREV[(dataREV.index >= '1990-01-02') & (dataREV.index<= end_date)]

    #!!! FORMULA POSITIONING
    dataREV["Diff"] = abs((data['10 YR'].iloc[-1] - data['2 YR'].iloc[-1]) - (dataREV['10 YR'] - dataREV['2 YR']))
    
    return dataREV['Diff'].idxmin()