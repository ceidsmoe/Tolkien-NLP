# Tolkien-NLP

I've included in this file most of what you'll need to reproduce my results. Obviously due to copyright law you won't find the full text of Lord of the Rings here, but the text file of phonemes should suffice to run the remaining code. You should be able to just run euphony.py and generate the necessary coefficients.

From there, the included Jupyter notebook should suffice to parse through the output and see how I arrived at my results.

If you would like to regenerate the frequencies, just run frequency.py. 

I wouldn't recommend trying to regenerate the phonemes, as phonemes.py took around 4 hours to run for me (I attempted to parallelize it using Spark, but G2PModel.decode isn't pickleable and hence doesn't play nice with Spark). I accepted this awful runtime only because I knew I'd only have to generate the phonemes once. In addition, I leave it to your devices to obtain a copy of Lord of the Rings to run this file (though obtaining an epub via the means of your choice and converting it to plaintext should be a pretty trivial task).

[The installation instructions for G2PModel can be found here.](https://github.com/cmusphinx/g2p-seq2seq) You only need to do this if you wish to run phonemes.py.

NLTK, SciPy, Jupyter, and inflect can all be acquired via the normal means of pip. NLTK will also require the additional step of going to a python shell. Enter:

import nltk
nltk.download()

Then navigate to the "Models" tab, select "punkt", and click download.