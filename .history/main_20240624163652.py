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

# Setup GUI Labels and Entries
label1 = Label(root, text="Search")
E1 = Entry(root, bd=5)
label1.pack()
E1.pack()

label2 = Label(root, text="Number of Tweets")
E2 = Entry(root, bd=5)
label2.pack()
E2.pack()

label3 = Label(root, text="Reply?")
E3 = Entry(root, bd=5)

label4 = Label(root, text="Response")
E4 = Entry(root, bd=5)


def get_inputs():
    search = E1.get()
    numberOfTweets = E2.get()
    try:
        numberOfTweets = int(numberOfTweets)
    except ValueError:
        print("Number of Tweets needs to be an integer")
        return
    mainFunction(search, numberOfTweets)


def mainFunction(search, numberOfTweets):
    # Execute Twitter functionalities based on inputs
    for tweet in tweepy.Cursor(api.search_tweets, q=search).items(numberOfTweets):
        try:
            tweet.retweet()
            print("Retweeted the tweet")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


# Button to trigger the main function
submit_button = Button(root, text="Submit", command=get_inputs)
submit_button.pack()

root.mainloop()
