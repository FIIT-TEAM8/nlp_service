import string

import spacy

from language_processor.language_mapping import language_mapping


class LanguageProcessor:
    def __init__(self):
        self.language_mapping = language_mapping
        self.language_mapping.setdefault("default", "xx")
        self.language_key: str = "xx"
        self.nlp = spacy.load(language_mapping.get(self.language_key))  # type: ignore
        self.reload_model()

    def reload_model(self):
        self.nlp = spacy.load(language_mapping.get(self.language_key))  # type: ignore

    def set_language(self, language_tag: str, reload=True):
        if language_tag not in language_mapping.keys():
            return False, "Language key not supported"

        if not language_tag == self.language_key:
            self.language_key = language_tag
            if reload:
                try:
                    self.reload_model()
                except:
                    return False, "Could not load language model"
            return True, "Language set successfuly"

        return False, "Something went wrong"

    def analyze_text(self, text: str):
        doc = self.nlp(text)
        entities = []
        ent_types = set()
        for entity in doc.ents:
            ent_types.add(entity.label_)
            entities.append({entity.text: entity.label_})
        
        print(self.language_key, ent_types)
        return entities

    def get_language(self):
        return self.language_key
