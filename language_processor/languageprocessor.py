import string

import spacy

from language_processor.language_mapping import language_mapping
from collections import Counter


class LanguageProcessor:
    def __init__(self):
        self.language_mapping: dict = language_mapping
        self.default_language: str = "xx"
        self.models: dict = {
            "xx": spacy.load(language_mapping.get(self.default_language))  # type: ignore
        }

    def is_loaded(self, language: str):
        if language not in language_mapping:
            return False
        if not language in self.models or self.models[language] is None:
            return False

        return True

    def get_model_entity_labels(self, language: str):
        if (self.is_loaded(language=language)):
            return self.models[language].get_pipe("ner").labels
        else:
            return []

    def load_model(self, language: str):
        if not self.is_loaded(language=language):
            self.models[language] = spacy.load(language_mapping.get(language))  # type: ignore
            
    def get_model_keys(self):
        return list(self.models.keys())

    def release_model(self, language: str):
        self.models.pop(language, None)

    def set_language(self, language: str, load=True):
        if language not in language_mapping:
            language = self.default_language

        if load:
            try:
                self.load_model(language=language)
                return True, "Language loaded"
            except Exception as e:
                print(e)
                return False, "Could not load model"

        return False, "Something went wrong"

    def analyze_text(self, text: str, language: str):
        self.set_language(language, load=True)
        if language not in language_mapping:
            language = self.default_language
        doc = self.models[language](text=text)
        
        return self.sort_to_bins(doc.ents)

    def sort_to_bins(self, entities: list):
        result_dict: dict = {"PER": Counter([]), "LOC": Counter([]), "ORG": Counter([]), "MISC": Counter([])}
        PER_tags = ["PER", "DERIV_PER", "PERSON", "persName", "PRS"]
        ORG_tags = ["ORG", "PRODUCT", "EVENT", "GPE_ORG", "orgName", "FACILITY", "ORGANIZATION"]
        LOC_tags = ["LOC", "LANGUAGE", "GPE_LOC", "geogName", "placeName"]

        for entity in entities:
            if entity.label_ in PER_tags:
                result_dict["PER"].update([entity.text])
                continue
            if entity.label_ in ORG_tags:
                result_dict["ORG"].update([entity.text])
                continue
            if entity.label_ in LOC_tags:
                result_dict["LOC"].update([entity.text])
                continue
            else:
                result_dict["MISC"].update([entity.text])

        return result_dict