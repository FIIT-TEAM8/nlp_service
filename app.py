import json

from flask import Flask, jsonify, request

from language_processor.languageprocessor import LanguageProcessor

app = Flask(__name__)
language_processor = LanguageProcessor()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/models/release/<key>')
def set_language(key):
    language_processor.release_model(key)
    return jsonify({"ok": True, "msg": "Model {} freed".format(key)})


@app.get('/models')
def get_models():
    model_keys = language_processor.get_model_keys()
    return jsonify({"ok": True, "keys": model_keys})


@app.post('/analyse')
def analyze():
    content = request.get_json()
    if content is None:
        return jsonify({"ok": False, "msg": "Non-supported body type"}), 400

    if content.get("language") is None:
        return jsonify({"ok": False, "msg": "Missing field: language"}), 400

    if content.get("text") is None:
        return jsonify({"ok": False, "msg": "Missing field: text"}), 400
    
    tags = language_processor.analyze_text(content.get("text"), content.get("language"))
    return jsonify({"ok": True, "tags": tags})



if __name__ == '__main__':
    app.run()

