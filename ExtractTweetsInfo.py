import json
from TokeniserWithEmotions import preprocess

with open('python.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        print tokens

