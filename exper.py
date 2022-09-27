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
print(data)