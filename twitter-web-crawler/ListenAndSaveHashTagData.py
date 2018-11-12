import tweepy
from tweepy import Stream, OAuthHandler
from HashtagListener import HashtagListener

#this class search for a hashtag and tracks the stream over twitter and save on python.json

consumer_key = "xsfJwYCkMGIrsHyeqUQmjBWDy"
consumer_secret = "YbbAx3NzxuHZScTPdmhSGA08KtO5C5YIOJSffjAniatx6N7v9z"
access_token = "51848952-p4tETlaEQNhTNsuK6dYzebqczKsZ2OMFSonpi75kV"
access_token_secret = "gwtQz8rN78FclDa4moQRcbG5SukUlX7SnIPrS0VzhaYJo"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

hashtag = input("Name the hashtag -> ")

twitter_stream = Stream(auth, HashtagListener())
twitter_stream.filter(track=[hashtag])
