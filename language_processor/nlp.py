import string

import spacy

from language_processor.language_mapping import language_mapping


class NLP:
    def __init__(self):
        spacy.prefer_gpu()

        self.language_mapping = language_mapping
        self.language_key = "xx"
        self.nlp = spacy.load(language_mapping.get(self.language_key))

    def reload_model(self):
        self.nlp = spacy.load(language_mapping.get(self.language_key))

    def set_language(self, language_tag: string):
        if language_tag not in language_mapping.keys():
            return False

        if not language_tag == self.language_key:
            self.language_key = language_tag
            self.reload_model()
            return True

    def get_language(self):
        return self.language_key
