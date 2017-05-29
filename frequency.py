from g2p_seq2seq.g2p import G2PModel
import sys
import nltk.data
import json
import re
from StringIO import StringIO

sentences = open("phonemes.txt", "r").readlines()

frequencies = {}
total = 0

for sentence in sentences:
	for ph in sentence.split():
		total += 1
		frequencies[ph] = frequencies.get(ph, 0) + 1

for k, v in frequencies.iteritems():
	frequencies[k] = float(v) / total

output = open("phfreq.json", "w")

output.write(json.dumps(frequencies))