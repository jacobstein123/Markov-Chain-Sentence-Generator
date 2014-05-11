Markov-Chain-Sentence-Generator
===============================

**How To Use:**

* Place the sample text you want to analyze in the same folder as main.py

* Replace the file name (huckfinn.txt) in main.py with the file name of your desired text

* Call `generate_sentences(sample_text)` to create a sentence based on the text patterns in the sample text

**Algorithm Explanation:**

The central idea of the algorithm is to pick two "seed" words from the start of a random sentence in the sample text. Then it will use those seed words to determine all the possible words that could come next. It will then pick one of those words, based on how likely they are to be chosen. It will continue with this until one of the words chosen is determined to be a "sentence ending" word.
