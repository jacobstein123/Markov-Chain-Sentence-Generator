import random
import re

def get_seed(sample_text):
    text = ''.join([i for i in sample_text if i not in ['\x93','\x92','\x94','\x95',',','\x97','-','_']]) #eliminates problematic symbols that will hurt pattern detection
    lines = re.split('\. |\n|\? |\! |\.',text)
    words = [i.split() for i in lines if len(i) > 1]
    seed = ' '.join(random.choice(words)[:2]).lower()
    return seed,lines

def get_following_words(seed,lines):
    following_words = []
    for line in lines:
        line = line.lower()
        big_enough = len(line.split()) - len(seed.split()) >= 2
        if seed in line and big_enough and line.find(seed)+len(seed) < len(line):
            line_list = line.split()
            seed_list = seed.split()
            if seed_list[0] in line_list and seed_list[0] != line_list[-1] and seed_list[1] != line_list[-1]:
                if line_list[line_list.index(seed_list[0])+1] == seed_list[1]:
                    following_word = line_list[line_list.index(seed_list[0])+2]
                    following_words.append(following_word)
    return following_words

def get_most_likely_word(following_words):
    if len(following_words):
        return random.choice(following_words)
    else:
        return "#" #marks end of sentence

def generate_sentence(sample_text):
    sentence = []
    while 1:
        seed,lines = get_seed(sample_text)
        if len(seed.split()) == 2:
            break
    sentence.append(seed.split()[0])
    sentence.append(seed.split()[1])
    while 1:
        seed = ' '.join(sentence[-2:])
        following_words = get_following_words(seed,lines)
        following_word = get_most_likely_word(following_words)
        if following_word == "#":
            break
        else:
            sentence.append(following_word)
    return ' '.join(sentence).capitalize() + '.'

