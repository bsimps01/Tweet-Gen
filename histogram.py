import random
import sys

filename = open("/Users/benjamin5311/dev/MakeSchool/CS1-2/Tweet-Gen/EAP.text", "r")
lines = filename.readlines()

word_histogram = {}

def histogram():
    for word in lines:
        word = word.rstrip()
        word_histogram[word] = word_histogram.get(word, 0) + 1
    return word_histogram

def unique_words():
    pass
def frequency():
    pass

if __name__ == '__main__':
    print(histogram())