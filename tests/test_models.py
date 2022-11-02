import pytest

from language_processor.language_mapping import language_mapping
from language_processor.languageprocessor import LanguageProcessor


@pytest.mark.skip
@pytest.mark.parametrize("language", language_mapping.keys())
def test_changing_language(language):
    lp = LanguageProcessor()
    lp.set_language(language, reload=False)
    assert lp.get_language() == language

@pytest.mark.parametrize("language", language_mapping.keys())
def test_running_analysis(language):
    lp = LanguageProcessor()
    lp.set_language(language)
    with open("example.txt", "r", encoding="utf-8") as file:
        text = ''.join(file.readlines())
        output = lp.analyze_text(text=text)
        assert output
        
