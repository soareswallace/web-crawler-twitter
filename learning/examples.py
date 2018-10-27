import tweepy
import json

consumer_key = "xsfJwYCkMGIrsHyeqUQmjBWDy"
consumer_secret = "YbbAx3NzxuHZScTPdmhSGA08KtO5C5YIOJSffjAniatx6N7v9z"
access_token = "51848952-p4tETlaEQNhTNsuK6dYzebqczKsZ2OMFSonpi75kV"
access_token_secret = "gwtQz8rN78FclDa4moQRcbG5SukUlX7SnIPrS0VzhaYJo"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

username = "katyperry"

# Number of tweets to pull
tweetCount = 20

def process_or_store(tweet):
   print(json.dumps(tweet))

#home timeline
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print (tweet.text)

#tweets from my timeline in json format
for status in tweepy.Cursor(api.user_timeline).items(10):
   print(process_or_store(status._json))

#search for a especific user
results = api.user_timeline(id = username, count = tweetCount)
for tweet in results:
    print (tweet.text)