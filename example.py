import SentenceGenerator

with open('huckfinn.txt','r') as textfile: #load the text to analyze
    sample_text = textfile.read()

#Generating one sentence:
print SentenceGenerator.generate_sentence(sample_text)

#Generating a paragraph:
sentences = 5
print ' '.join([SentenceGenerator.generate_sentence(sample_text) for i in xrange(sentences)])
