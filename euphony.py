import json
import sys
import nltk.data
from scipy.misc import comb
from collections import Counter

euph_heuristic = {"IY": 1.0, "AA": 1.0, "CH": -0.5, "ZH": 1.0, "EH": 0.5, "DH": 1.0, "F": 1.0, "AH": 0.5, "K": -1.0, "SH": 0.0, "M": 1.0, "L": 1.0, "AO": 1.0, "N": 1.0, "IH": 0.5, "HH": 1.0, "B": -1.0, "JH": 0.0, "T": -1.0, "AW": 1.0, "V": 1.0, "Y": 1.0, "AE": 1.0, "AY": 1.0, "Z": 0.0, "D": -1.0, "G": -1.0, "P": -1.0, "UW": 1.0, "OY": 1.0, "S": 0.0, "NG": 0.0, "W": 0.0, "R": 1.0, "UH": 0.5, "TH": 1.0, "OW": 1.0, "EY": 1.0, "ER": 1.0}

phfreq = open("phfreq.json", "r")
phonemes = json.loads(phfreq.read())

phsentences = open("phonemes.txt", "r")

output1 = open("euphony-scores.txt", "w")
#output2 = open("escore2.txt", "w")

reload(sys)
sys.setdefaultencoding('utf8')
lotr = open("books/lotr.txt", "r")

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = tokenizer.tokenize(unicode(lotr.read()))

data = zip(sentences, phsentences)

def euphonize(sentence):
	score = 0.0
	sentence = sentence.split()
	
	if len(sentence) <= 0:
		return 0.0

	for ph in sentence:
		score += euph_heuristic[ph]

	return score#/len(sentence)

def bie(sentence):
	phfreq = open("phfreq.json", "r")
	phonemes = json.loads(phfreq.read())

	sentence = sentence.split()
	alpha = 0.05
	n = len(sentence)
	euph = 0.0
	for ph, count in Counter(sentence).iteritems():
		if count < 2 or euph_heuristic[ph] <= 0.0:
			continue
		P = 0.0
		p = phonemes.get(ph, 0.0)

		for k in xrange(count, n):
			P += comb(n, k)*pow(p, k)*pow(1-p, n-k)

		if P < alpha:
			euph += (100*(alpha - P))

	return euph

n = len(data)

score = []

for i, d in enumerate(data):
	print "%f" % (100.0 * i / n)
	x1 = bie(d[1])
	#x2 = euphonize(d[1])
	output1.write("%f\n" % x1)

print "done"