from pprint import pprint
from g2p_seq2seq.g2p import G2PModel
import sys
import os
import nltk.data
import json
import re
import inflect
from operator import add
from StringIO import StringIO
import string

words = open("phoneme_output.txt", "r").readlines()

total = len(words)
frequencies = {}


g2p_model = G2PModel('g2p-seq2seq-cmudict')
g2p_model.load_decode_model()

M = {}

for word in words:
	for ph in word.split()[1:]:
		if len(ph) > 2:
			sub_phs = M.get(ph, [])

			if not sub_phs:
				sub_phs = g2p_model.decode([ph], StringIO())
				M[ph] = sub_phs

			for sph in sub_phs[0].split():
				frequencies[sph] = frequencies.get(sph, 0) + 1
		else:
			frequencies[ph] = frequencies.get(ph, 0) + 1

for k, v in frequencies.iteritems():
	frequencies[k] = float(v) / total

output = open("phfreq.json", "w")

output.write(json.dump(frequencies))