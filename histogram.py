import random
import sys

#filename = open("/Users/benjamin5311/dev/MakeSchool/CS1-2/Tweet-Gen/EAP.text", "r")
#lines = filename.readlines()

#word_histogram = {}

def histogram():
    filename = open("/Users/benjamin5311/dev/MakeSchool/CS1-2/Tweet-Gen/EAP.text", "r")
    lines = filename.readlines()

    word_histogram = {}
    
    for line in lines:
        for word in line.split():
            word = word.rstrip()
            word_histogram[word] = word_histogram.get(word, 0) + 1
    return word_histogram

def unique_words():
    word_count = 0
    for word in word_histogram:
        if word_histogram[word] == 1:
            word_count += 1
    return(word_count)

def frequency():
    for word in word_histogram:
        print(f'Word found: {word}, Word Count: {word_histogram[word]}')
    else:
        return (f'There are {unique_words()} unique words.')

if __name__ == '__main__':
    print(histogram())
    print(unique_words())
    print(frequency())