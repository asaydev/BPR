from string import punctuation
import csv
import pandas as pd
from lxml import etree
import nltk

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




tree = etree.parse('Persian.xml')
root = tree.getroot()
print(root[0][3].tag)
