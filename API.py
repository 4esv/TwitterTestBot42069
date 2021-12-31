from dotenv import load_dotenv
import tweepy
import time
import os

# Set up envrioment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_PRIVATE = os.getenv("API_KEY_PRIVATE")
TOKEN = os.getenv("TOKEN")
TOKEN_PRIVATE = os.getenv("_PRIVATE")


# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_KEY_PRIVATE)
auth.set_access_token(TOKEN, TOKEN_PRIVATE)

# Create API object
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(f"{tweet.text} \n")

api.update_status(i for i in [i for i in "hello"])

