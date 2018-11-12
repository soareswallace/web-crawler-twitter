import operator
import json
from collections import Counter
from helper_functions.TokeniserWithEmotions import preprocess
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

# Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)
# Count hashtags only
terms_hash = [term for term in preprocess(tweet['text'])
              if term.startswith('#')]
# Count terms only (no hashtags, no mentions)
terms_only = [term for term in preprocess(tweet['text'])
              if term not in stop and
              not term.startswith(('#', '@'))]
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if
              # we pass a list of inputs

fname = 'python.json'

with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        #Create a list with all terms
        #Update the counter
        count_all.update(terms_stop)
    #Print the first 5 most frequent words
    print (count_all.most_common(30))
