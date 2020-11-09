from string import punctuation
import csv
import pandas as pd
from lxml import etree
import nltk
from hazm import *

puncf = r"!\"#$،%&'()*+,-./:;<=>?@[\]^_`{|}~"
punct = list(puncf)

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
    # tagged_per_title += tagger.tag(item)
for item in persian_desc_token:
    if item in punct:
        persian_desc_token.remove(item)
    # tagged_per_desc += tagger.tag(item)

print(tagged_per_desc)
print(tagged_per_title)
