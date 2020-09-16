


import tweepy
import os
from dotenv import load_dotenv
from tweepy import OAuthHandler, API

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)

api = API(auth)
print("API CLINET", api)

user = api.get_user('s2t2')
print("TWITTER USER:", type(user))
print(user.id)
print(user.screen_name)
print(user.name)


tweets = api.user_timeline("s2t2", tweet_mode="extended")
print("TWEETS", type(tweets))
print(type(tweets[0]))

tweet = tweets[0]
print(tweet.id)
print(tweet.full_text)

breakpoint()