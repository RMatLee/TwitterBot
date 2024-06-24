from tkinter import *
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

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

# GUI Elements for inputs
label1 = Label(root, text="Search")
E1 = Entry(root, bd=5)
label2 = Label(root, text="Number of Tweets")
E2 = Entry(root, bd=5)
label3 = Label(root, text="Reply?")
E3 = Entry(root, bd=5)
label4 = Label(root, text="Response")
E4 = Entry(root, bd=5)
label5 = Label(root, text="Retweet?")
E5 = Entry(root, bd=5)
label6 = Label(root, text="Favorite?")
E6 = Entry(root, bd=5)
label7 = Label(root, text="Follow?")
E7 = Entry(root, bd=5)

# Pack the GUI elements
labels = [label1, label2, label3, label4, label5, label6, label7]
entries = [E1, E2, E3, E4, E5, E6, E7]
for label, entry in zip(labels, entries):
    label.pack()
    entry.pack()


def execute_twitter_actions():
    """
    Fetches user inputs and executes Twitter actions like replying, retweeting,
    favoriting, and following based on specified criteria.
    """
    search = E1.get()
    try:
        number_of_tweets = int(E2.get())
    except ValueError:
        print("Please enter a valid number of tweets")
        return

    # Collect input values for actions
    reply = E3.get().lower()
    phrase = E4.get()
    retweet = E5.get().lower()
    favorite = E6.get().lower()
    follow = E7.get().lower()

    # Execute actions on tweets found by search query
    for tweet in tweepy.Cursor(api.search_tweets, q=search).items(number_of_tweets):
        try:
            if reply == "yes":
                api.update_status(
                    f"@{tweet.user.screen_name} {phrase}",
                    in_reply_to_status_id=tweet.id,
                )
                print(f"Replied with {phrase} to @{tweet.user.screen_name}")

            if retweet == "yes":
                tweet.retweet()
                print("Retweeted the tweet")

            if favorite == "yes":
                tweet.favorite()
                print("Favorited the tweet")

            if follow == "yes":
                tweet.user.follow()
                print(f"Followed @{tweet.user.screen_name}")

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


# Setup and pack the button to trigger Twitter actions
submit_button = Button(root, text="Execute", command=execute_twitter_actions)
submit_button.pack()

# Run the GUI event loop
root.mainloop()
