from flask import Flask
from dictogram import Dictogram
from listogram import Listogram
from random import random

app = Flask(__name__)

@app.route('/')
def generate_words():
    #with open('./EAP.text') as f:
        #words = f.readlines()
    lines = Dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    sentence = ""
    num_words = 20
    for i in range(num_words):
        word = lines.sample()
        sentence += " " + word
    return sentence

if __name__ == '__main__':
    app.run()