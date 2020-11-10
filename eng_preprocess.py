from string import punctuation
import csv
import pandas as pd
from lxml import etree
import nltk
import re
from hazm import *
from nltk.corpus import stopwords

df = pd.read_csv('ted_talks.csv', usecols=['title', 'description'])
# print(df)
df.to_csv('new.csv', index=False)
my_dict = {}
with open('new.csv', 'r') as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for row in rd:
        new_key = row['title']
        new_values = (row['description'])
        my_dict[new_key] = new_values

token_list = []
for key, value in my_dict.items():
     token_list += nltk.word_tokenize(key)
     token_list += nltk.word_tokenize(value)

#print(my_dict)
punck=list(punctuation)
punck += ["``","''","`","'","--","’"]
# print(punck)

for item in token_list:
    if item in punck:
        token_list.remove(item)
# print(token_list)

stopWords = set(stopwords.words())
token_list = [word for word in token_list if len(word) > 1]
token_list = [word for word in token_list if not word.isnumeric()]
token_list = [word for word in token_list if not re.search('^[0-9]+\\.[0-9]+$', word)]
token_list = [word.lower() for word in token_list]
words = [word for word in token_list if word not in stopWords]
print(words)
