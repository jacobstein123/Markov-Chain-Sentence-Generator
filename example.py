import SentenceGenerator

sample_text = open('huckfinn.txt','r').read() #load the text to analyze

#Generating one sentence:
print SentenceGenerator.generate_sentence(sample_text)

#Generating a paragraph:
sentences = 5
print ' '.join([SentenceGenerator.generate_sentence(sample_text) for i in xrange(sentences)])
