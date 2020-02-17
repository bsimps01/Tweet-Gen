from flask import Flask
from histogram import histogram
from sample import sample_by_frequency

app = Flask(__name__)

@app.route('/')
def generate_words():
    lines = histogram("./EAP.text")
    sentence = ""

    num_word = 10
    for i in range(num_words):
        word =  sample_by_frequency(my_histogram)
        sentence += " " + word

    return sentence

if __name__ == '__main__':
    app.run()