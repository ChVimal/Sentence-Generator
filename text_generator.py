import random
from collections import defaultdict

import regex as re
from nltk import trigrams
from nltk.tokenize import regexp_tokenize

with open(input(), encoding='utf-8') as file:
    data = file.readlines()
data = ''.join(data)

tokens = regexp_tokenize(data, r'[^ \n\t]+')
tri_gram = []
for tri in list(trigrams(tokens)):
    tri_gram.append((tri[0] + " " + tri[1], tri[2]))

tri_gram_dict = defaultdict(lambda: defaultdict(int))
for i in tri_gram:
    tri_gram_dict[i[0]][i[1]] += 1

for _ in range(10):
    sentence = ['', '']
    while re.match('^[A-Z].*[^?.!]$', sentence[0]) is None:
        sentence.pop()
        sentence.pop()
        sentence += random.choice(list(tri_gram_dict.keys())).split(' ')
    last_bi_gram = sentence[-2] + ' ' + sentence[-1]
    while not (len(sentence) >= 5 and re.match('.*[?.!]$', last_bi_gram)):
        bi_grams = list(tri_gram_dict[last_bi_gram].keys())
        weight = list(tri_gram_dict[last_bi_gram].values())
        sentence += random.choices(bi_grams, weight, k=1)[0].split()
        last_bi_gram = sentence[-2] + ' ' + sentence[-1]
    print(' '.join(sentence))
