from string import punctuation
import csv
import pandas as pd
from lxml import etree

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

print(my_dict)
tree = etree.parse('Persian.xml')
root = tree.getroot()
print(root[0][3].tag)


# print("punctuation : ",punctuation)
punck = list(punctuation)
