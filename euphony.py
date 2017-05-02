import json
from scipy.misc import comb

phfreq = open("phfreq.json", "r")
phonemes = json.loads(phfreq.read())

setences = open("phonemes.txt", "r")
"""lotr = open("books/lotr.txt", "r")

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = tokenizer.tokenize(unicode(lotr.read()))"""

def bie(sentence):
	alpha = 0.05
	n = len(sentence)
	euph = []
	for ph in sentence:
		P = 0.0
		p = phonemes[ph]
		for k in xrange(n):
			P += comb(n, k)*pow(p, k)*pow(1-p, n-k)
		if P < alpha:
			euph.append(100*(alpha - P))
		else:
			print P
			euph.append(0.0)

	return sum(euph)

bie()