import tweepyimport, Tkinter, tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
