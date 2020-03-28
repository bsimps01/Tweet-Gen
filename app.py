from flask import Flask, render_template, request, url_for
from dictogram import Dictogram
from listogram import Listogram
from random import random
from markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def generate_words():
    words_list = []
    with open('./EAP.text') as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split():
                words_list.append(word)
    #lines = Dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    markovchain = MarkovChain(words_list)
    '''sentence = ""
    num_words = 20
    for i in range(num_words):
        word = lines.sample()
        sentence += " " + word
    return sentence'''
    sentence = markovchain.walk(24)
    
    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)