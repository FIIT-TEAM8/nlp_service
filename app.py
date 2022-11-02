import json

from flask import Flask, jsonify, request

from language_processor.languageprocessor import LanguageProcessor

app = Flask(__name__)
nlp = LanguageProcessor()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/language/<key>')
def set_language(key):
    success, message = nlp.set_language(key)
    return jsonify({"ok": success, "msg": message})


@app.get('/language')
def get_language():
    language = nlp.get_language()
    return jsonify({"language_key": language})


@app.post('/analyze')
def analyze():
    content = request.get_json()
    if content is None:
        return jsonify({"ok": False, "msg": "Non-supported body type"}), 400

    tags = nlp.analyze_text(content.get("text"))
    return jsonify({"ok": True, "tags": tags})



if __name__ == '__main__':
    app.run()

