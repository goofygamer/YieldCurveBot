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




def api():
    auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_KEY_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path = None):
    if image_path:
        api.update_status_with_media(message, image_path)
        print("Successful Tweet!")
    return


if __name__ == '__main__':
    api = api()
    tweet(api, distance.days(), f"images/Graph{str(data.data.index[-1].date())}.png")


