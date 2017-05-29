# Tolkien-NLP

I've included in this file most of what you'll need to reproduce my results. Obviously due to copyright law you won't find the full text of Lord of the Rings here, but the text file of phonemes should suffice to run the remaining code. You should be able to just run euphony.py and generate the necessary coefficients.

From there, the included Jupyter notebook should suffice to parse through the output and see how I arrived at my results.

If you would like to regenerate the frequencies, just run frequency.py. 

I wouldn't recommend trying to regenerate the phonemes, as phonemes.py took around 4 hours to run for me (I attempted to parallelize it using Spark, but G2PModel.decode isn't pickleable and hence doesn't play nice with Spark). I accepted this awful runtime only because I knew I'd only have to generate the phonemes once. In addition, I leave it to your devices to obtain a copy of Lord of the Rings to run this file (though obtaining an epub via the means of your choice and converting it to plaintext is a pretty trivial task).