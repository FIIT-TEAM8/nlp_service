import pytest
import time

from language_processor.language_mapping import language_mapping
from language_processor.languageprocessor import LanguageProcessor
lp = LanguageProcessor()

# @pytest.mark.skip
# @pytest.mark.parametrize("language", language_mapping.keys())
# def test_changing_language(language):
#     lp = LanguageProcessor()
#     lp.set_language(language, load=False)
#     assert lp.get_language() == language

@pytest.mark.parametrize("language", language_mapping.keys())
def test_running_analysis(language):
    print("\n------------------------------------------------")
    with open("example.txt", "r", encoding="utf-8") as file:
        print("language", language)
        t0 = time.perf_counter()
        text = ''.join(file.readlines())
        output = lp.analyze_text(text=text, language=language)
        assert output
        t1 = time.perf_counter()
        output = lp.analyze_text(text=text, language=language)
        t2 = time.perf_counter()
        total_time = t2 - t0
        cold_start_time = t1 - t0
        warm_start_time = t2 - t1
        print("total time", total_time)
        print("cold start time", cold_start_time)
        print("warm start time", warm_start_time)
        print(output)
        print(lp.get_model_entity_labels(language=language))
        lp.release_model(language=language)
        
