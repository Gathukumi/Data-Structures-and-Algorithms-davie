import re

def word_frequency(sentence):
    word_count = {}
    words = re.findall(r'\b\w+\b', sentence.lower())

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count