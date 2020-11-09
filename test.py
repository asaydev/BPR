from string import punctuation
import csv
import pandas as pd
from lxml import etree
import nltk
from hazm import *

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

#print(my_dict)
# print("punctuation : ",punctuation)
punck=list(punctuation)
punct = r"!\"#$،%&'()*+,-./:;<=>?@[\]^_`{|}~"


title_token_list = []
desc_token_list = []
for key, value in my_dict.items():
     title_token_list += nltk.word_tokenize(key)
     desc_token_list += nltk.word_tokenize(value)
for item in title_token_list:
    if item in punck:
        title_token_list.remove(item)
for item in desc_token_list:
    if item in punck:
        desc_token_list.remove(item)
tagged_title = nltk.pos_tag(title_token_list)
tagged_desc = nltk.pos_tag(desc_token_list)
#print(tagged_title)
#print(tagged_desc)

persian_dict = {}
tree = etree.parse('Persian.xml')
root = tree.getroot()
persian_title_token = []
persian_desc_token = []
tagged_per_title = []
tagged_per_desc = []
persian_doc_counter = 0
tagger = POSTagger(model='resources/postagger.model')
for child in root:
    new_key = child.findall(".//{http://www.mediawiki.org/xml/export-0.10/}title")[0].text
    new_value = child.findall(".//{http://www.mediawiki.org/xml/export-0.10/}text")[0].text
    persian_dict[new_key] = new_value
    persian_doc_counter = persian_doc_counter +1

for key, value in persian_dict.items():
    persian_title_token += word_tokenize(key)
    # print(persian_title_token)
    persian_desc_token += word_tokenize(value)
    # print(persian_desc_token)

for item in persian_title_token:
    if item in punct:
        persian_title_token.remove(item)
    tagged_per_title += tagger.tag(item)
for item in persian_desc_token:
    if item in punct:
        persian_desc_token.remove(item)
    tagged_per_desc += tagger.tag(item)

print(tagged_per_desc)
print(tagged_per_title)
