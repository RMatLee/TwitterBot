import tweepy
from dotenv import load_dotenv
import os

load_dotenv()  # This function loads the environment variables from the .env file

# Access the environment variables for Twitter API
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Verify credentials and get user information
user = api.verify_credentials()
print("Authenticated as: {}".format(user.name))

# Fetch and follow all followers
followers = tweepy.Cursor(api.get_followers).items()
try:
    first_follower = next(followers)
    followers = itertools.chain([first_follower], followers)
    for follower in followers:
        follower.follow()
        print("Followed {} who is following {}".format(follower.name, user.name))
except StopIteration:
    print("No followers to follow back!")
