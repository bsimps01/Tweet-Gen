from flask import Flask
from dictogram import Dictogram
from listogram import Listogram

app = Flask(__name__)

@app.route('/')
def generate_words():
    with open('./EAP.text') as f:
        words = f.readlines()
        lines = Dictogram(words)
    sentence = ""
    return lines.sample()
    num_words = 10

if __name__ == '__main__':
    app.run()