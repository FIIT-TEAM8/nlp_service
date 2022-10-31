from flask import Flask, request, jsonify
from language_processor.nlp import NLP

app = Flask(__name__)
nlp = NLP()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/language/<key>')
def set_language(key):
    success = nlp.set_language(key)
    return jsonify({"ok": success})


@app.get('/language')
def get_language():
    language = nlp.get_language()
    return jsonify({"language_key": language})


if __name__ == '__main__':
    app.run()
