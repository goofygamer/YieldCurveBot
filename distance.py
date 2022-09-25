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

def days(listed = data.recessionList):
    dist = math.inf
    target = closest.closest().date()
    for rec in listed:
        if ((target - rec[0]).days >= 0) and ((target - rec[1]).days) <= 0:
            return f"In a recession on {date.date.index[-1].date()}!"
        dist = min(dist, abs((rec[0] - target).days))
    
    return f"Recession is {dist} days away on {data.data.index[-1].date()}"