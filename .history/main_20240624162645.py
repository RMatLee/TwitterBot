import tweepy
from tkinter import *
from dotenv import load_dotenv
import os

load_dotenv()  # This function loads the environment variables from the .env file

# Access the environment variables for Twitter API
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

root = Tk()
label1 = Label(root, text="Search")
E1 = Entry(root, bd=5)
label2 = Label(root, text="Number of Tweets")
E2 = Entry(root, bd=5)
label3 = Label(root, text="Response")
E3 = Entry(root, bd=5)
label4 = Label(root, text="Reply?")
E4 = Entry(root, bd=5)
label5 = Label(root, text="Retweet?")
E5 = Entry(root, bd=5)
label6 = Label(root, text="Favorite?")
E6 = Entry(root, bd=5)
label7 = Label(root, text="Follow?")
E7 = Entry(root, bd=5)


# Verify credentials and get user information
user = api.verify_credentials()
print("Authenticated as: {}".format(user.name))

# Follow everyone who is following the authenticated user
try:
    for follower in tweepy.Cursor(api.get_followers).items():
        follower.follow()
        print("Followed {} who is following {}".format(follower.name, user.name))
except TypeError:
    print("Error: Unable to follow followers.")


def mainFunction():
    search = "Keyword"
    numberOfTweets = "Number of tweets you wish to interact with"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            print("Retweeted the tweet")

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

    tweetId = tweet.user.idusername = tweet.user.screen_name
    phrase = "What you would like your response tweet to say"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            api.update_status(
                "@" + username + " " + phrase, in_reply_to_status_id=tweetId
            )
            print("Replied with " + phrase)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


label1.pack()
E1.pack()
