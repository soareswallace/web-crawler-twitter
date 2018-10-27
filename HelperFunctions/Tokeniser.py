from nltk.tokenize import word_tokenize
from TokeniserWithEmotions import preprocess

tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print (word_tokenize(tweet))

tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(preprocess(tweet))