from string import punctuation
import csv
import pandas as pd
from lxml import etree
import nltk
from hazm import *

puncf = r"!\"#$،%&'()*+,-.؟/:;<=>?@[\]^_`{|}~"
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
    title = word_tokenize(child.findall(".//{http://www.mediawiki.org/xml/export-0.10/}title")[0].text)
    desc = word_tokenize(child.findall(".//{http://www.mediawiki.org/xml/export-0.10/}text")[0].text)
    persian_title_token += title
    persian_desc_token += desc
for item in persian_title_token:
    if item in punct:
        persian_title_token.remove(item)

for item in persian_desc_token:
    if item in punct:
        persian_desc_token.remove(item)
print(persian_title_token)
print(persian_desc_token)
