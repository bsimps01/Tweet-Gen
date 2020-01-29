from random import random, randint, choice, sample
import sys

my_file = open("/Users/benjamin5311/dev/MakeSchool/CS1-2/Tweet-Gen/test.txt", "r")
lines = my_file.readlines()

for random_index in lines:
    random_index = randint(0, len(lines)-1)
    rand_item = lines[random_index]
    print(rand_item)

