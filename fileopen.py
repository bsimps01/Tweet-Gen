from random import randint, choice

my_file = open("/Users/benjamin5311/dev/MakeSchool/CS1-2/words.txt", "r")
lines = my_file.readlines()
random_index = randint(0, len(lines)-1)
rand_item = lines[random_index]
print(rand_item)

#rand_item = choice(lines)

my_file.close()