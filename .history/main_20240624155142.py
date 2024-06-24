import tweepyimport, Tkinter, tweepy
from dotenv import load_dotenv
import os

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
