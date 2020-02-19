from flask import Flask
from dictogram import Dictogram
from listogram import Listogram

app = Flask(__name__)

@app.route('/')
def generate_words():
    lines = Dictogram("./EAP.text")
    sentence = ""

    num_word = 10
    for i in range(num_words):
        word =  sample_by_frequency(my_histogram)
        sentence += " " + word

    return sentence

if __name__ == '__main__':
    app.run()