import requests
import keys
import nasdaqdatalink
import quandl
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime, timedelta
import pandas as pd
import math
import distance
import data
import graph
import tweepy

print(f"images/Graph{str(data.data.index[-1].date())}.png")