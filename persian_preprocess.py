from string import punctuation
import csv
import pandas as pd
from lxml import etree
import nltk
from hazm import *
from hazm import stopwords_list

puncf = "!\"#$،%&'()*+,-.؟/::;<=>?@[\]^_`{|}~"
punct = ["~", "{", "|", "}", ":", "؟", "?", "(", ")", "!", ".", "،", "[", "]", "<", ">", "="]

tree = etree.parse('Persian.xml')
root = tree.getroot()
persian_title_token = []
persian_desc_token = []
# tagged_per_title = []
# tagged_per_desc = []
persian_doc_counter = 0
normalizer = Normalizer()
stemmer = Stemmer()
stop_words = []
stop_words += stopwords_list()
stop_words += punct


# print(stop_words)


def delete_stop_word(token):
    temp = token
    for item in temp:
        if item in stop_words:
            print(item)
            temp.remove(item)
    return temp


print(punct)
for child in root:
    persian_doc_counter = persian_doc_counter + 1
    title_normal = normalizer.normalize(child.findall(".//{http://www.mediawiki.org/xml/export-0.10/}title")[0].text)
    desc_normal = normalizer.normalize(child.findall(".//{http://www.mediawiki.org/xml/export-0.10/}text")[0].text)
    title = word_tokenize(title_normal)
    desc = word_tokenize(desc_normal)
    persian_title_token += delete_stop_word(title)
    persian_desc_token += delete_stop_word(desc)
    if persian_doc_counter == 1:
        break

print(len(persian_desc_token))
print(persian_desc_token)
