import requests
import keys
import nasdaqdatalink
import quandl
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime, timedelta
import pandas as pd
import math

data = quandl.get("USTREASURY/YIELD", authtoken = keys.NASDAQ_API_KEY)


recessionList = [[datetime.strptime("1990-07-01", "%Y-%m-%d").date(), datetime.strptime("1991-03-31", "%Y-%M-%d").date()],
[datetime.strptime("2001-03-01", "%Y-%m-%d").date(), datetime.strptime("2001-11-31", "%Y-%M-%d").date()],
[datetime.strptime("2007-12-01", "%Y-%m-%d").date(), datetime.strptime("2009-06-30", "%Y-%M-%d").date()],
[datetime.strptime("2020-02-01", "%Y-%m-%d").date(), datetime.strptime("2020-04-30", "%Y-%M-%d").date()]]