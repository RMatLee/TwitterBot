import tweepyimport, Tkinter, tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
