Markov-Chain-Sentence-Generator
===============================

**How To Use:**

* Place the sample text you want to analyze in the same folder as SentenceGenerator.py

* Import SentenceGenerator into your project 

* Create a string `sample_text` with the contents of the textfile you wish to analyze

* Call `SentenceGenerator.generate_sentences(sample_text)` to create a sentence based on the text patterns in the sample text

* For an example usage and how to create paragraphs, see example.py

**Algorithm Explanation:**

The central idea of the algorithm is to pick two "seed" words from the start of a random sentence in the sample text. Then it will use those seed words to determine all the possible words that could come next. It will then pick one of those words, based on how likely they are to be chosen. It will continue with this until one of the words chosen is determined to be a "sentence ending" word.
