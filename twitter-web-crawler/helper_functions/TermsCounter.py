import operator
import json
from collections import Counter, defaultdict
from TokeniserWithEmotions import preprocess
from nltk.corpus import stopwords
from nltk import bigrams
import string
import sys

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'via', u"\u2026", '🖥', '🕰', '🎮', '💎', u"\u0020"]

fname = '../python.json'
def count_them_all():
    with open(fname, 'r') as f:
        count_stop = Counter()
        count_hash = Counter()
        count_only = Counter()
        count_biagram = Counter()
        for line in f:
            tweet = json.loads(line)
            terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
            terms_hash = [term for term in preprocess(tweet['text']) 
                if term.startswith('#')]
            terms_only = [term for term in preprocess(tweet['text']) 
                if term not in stop and
                not term.startswith(('#', '@'))]
            terms_bigram = bigrams(terms_hash)
                # mind the ((double brackets))
                # startswith() takes a tuple (not a list) if 
                # we pass a list of inputs
            #Create a list with all terms
            #Update the counter
            count_stop.update(terms_stop)
            count_hash.update(terms_hash)
            count_only.update(terms_only)
            count_biagram.update(terms_bigram)
        #Print the first 5 most frequent words
        print ("Stop words -> " + str(count_stop.most_common(30)))
        # print ("Hashtags -> " + str(count_hash.most_common(30)))
        # print ("Terms only -> " + str(count_only.most_common(30)))
        # print ("Biagrams -> " + str(count_biagram.most_common(30)))
        
def detect_co_ocurrences():
    com = defaultdict(lambda : defaultdict(int))
    # f is the file pointer to the JSON data set
    with open(fname, 'r') as f:
        for line in f: 
            tweet = json.loads(line)
            terms_only = [term for term in preprocess(tweet['text']) 
                        if term not in stop 
                        and not term.startswith(('#', '@'))]
        
            # Build co-occurrence matrix
            for i in range(len(terms_only)-1):            
                for j in range(i+1, len(terms_only)):
                    w1, w2 = sorted([terms_only[i], terms_only[j]])                
                    if w1 != w2:
                        com[w1][w2] += 1
    com_max = []
    for t1 in com:
        t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:30]
        for t2, t2_count in t1_max_terms:
            com_max.append(((t1, t2, t2_count)))
            # Get the most frequent co-occurrences
        terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
    print(terms_max[:5])

def search_co_ocurrency_specific():
    search_word = sys.argv[1] # pass a term as a command-line argument
    count_search = Counter()
    with open(fname, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            terms_only = [term for term in preprocess(tweet['text']) 
                        if term not in stop 
                        and not term.startswith(('#', '@'))]
            if search_word in terms_only:
                count_search.update(terms_only)
        print("Co-occurrence for %s:" % search_word)
        print(count_search.most_common(20))

# count_them_all()
detect_co_ocurrences()
# search_co_ocurrency_specific()