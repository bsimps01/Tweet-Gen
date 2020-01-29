import random

words = ["how", "now", "brown", "cow"]

def random_cow():
    
    for rand_index in words:
        rand_index = random.randint(0, len(words) - 1)
        print(words[rand_index])
    return True

if __name__ == '__main__':
    random_cow()