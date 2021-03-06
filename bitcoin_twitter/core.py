# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['connector']

# Cell
from nbdev.showdoc import *
import os
import json
import urllib.parse
import requests
from requests.auth import AuthBase
import tweepy as tw
import pandas as pd

# Cell
class connector:
    def __init__(self,consumer_key, consumer_secret,n_items=1000,
                query='#Bitcoin -filter:retweets lang:en'):
        self.auth = tw.OAuthHandler(consumer_key, consumer_secret)
        self.n_items = n_items,
        self.query = query
        self.api = tw.API(self.auth)

    def get_tweets(self,query='',n_items=''):
        if query=='':
            query=self.query
        if n_items == '':
            n_times=self.n_items
        info = [[tweet.id,
                 tweet.text,
                 tweet.created_at,
                 tweet.user.id,
                 tweet.user.name,
                 tweet.user.screen_name,
                 tweet.retweet_count,
                 tweet.geo,
                 tweet.coordinates]
                for tweet in tw.Cursor(self.api.search, q=self.query)\
                .items(1000)]
        df_tweets = pd.DataFrame(info)
        df_tweets.columns = ['tweet_id',
                     'tweet_text',
                     'tweet_created_at',
                     'tweet_user_id',
                     'user_name',
                     'user_screen_name',
                     'retweet_count',
                     'tweet_geo',
                     'tweet_coordinates']
        return df_tweets