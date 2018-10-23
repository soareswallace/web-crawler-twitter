import tweepy

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

public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print tweet.text