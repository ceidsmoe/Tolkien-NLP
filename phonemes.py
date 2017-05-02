from pprint import pprint
from g2p_seq2seq.g2p import G2PModel
import tensorflow as tf
import sys
import os
import nltk.data
import json
import re
import inflect
from operator import add
from StringIO import StringIO
import string

reload(sys)
sys.setdefaultencoding('utf8')
lotr = open("books/lotr.txt", "r")

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = tokenizer.tokenize(unicode(lotr.read()))

iengine = inflect.engine()

g2p_model = G2PModel('g2p-seq2seq-cmudict')
g2p_model.load_decode_model()

def is_number(s):
    try:
        f = int(s)
        return True
    except:
        return False
    
def sentence_to_phoneme(sentence):
    words = []
    for word in re.split('\W+', sentence):
        if word == '':
            continue
        
        if is_number(word):
            word = iengine.number_to_words(int(word))
        word = word.lower().replace(",", "")
        words += word.split("-")
        
    return g2p_model.decode(words, StringIO())

phonemes = map(sentence_to_phoneme, sentences)

output = open("phonemes.txt", "w+")
for ph in phonemes:
	output.write(ph + "\n")