from string import punctuation
import csv
import pandas as pd
from lxml import etree
import nltk
import re
from hazm import *
from nltk.corpus import stopwords


def prepare_text(txt_file):
    with open ('txt_file.txt', "r") as myfile:
        data=myfile.read()
    # print(data)
    token_list = []
    token_list += nltk.word_tokenize(data)
    print(len(token_list))
    # print(token_list)

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
    # print(words)
    return words


df = pd.read_csv('ted_talks.csv', usecols=['title', 'description'])
# print(df)
df.to_csv('new.csv', index=False)
with open('txt_file.txt', "w") as my_output_file:
    with open('new.csv', "r") as my_input_file:
        data_with_header = list(csv.reader(my_input_file))
        data_wthot_hd = data_with_header[1:]
        [ my_output_file.write(" ".join(row)+' , ') for row in data_wthot_hd]
    my_output_file.close()

list = prepare_text('txt_file.txt')
print(list)
