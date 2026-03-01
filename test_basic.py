from analyzer import normalize_text, tokenize, TextAnalyzer


def test_normalization():
    text = "Hola, Mundo!! Python 3."
    normalized = normalize_text(text)
    assert normalized == "hola mundo python 3"


def test_tokenization():
    text = "hola mundo hola"
    tokens = tokenize(text)
    assert tokens == ["hola", "mundo", "hola"]


def test_count():
    analyzer = TextAnalyzer("hola hola mundo")
    analyzer.analyze()
    assert analyzer.counts["hola"] == 2
    assert analyzer.counts["mundo"] == 1


if __name__ == "__main__":
    test_normalization()
    test_tokenization()
    test_count()
    print("Todas las pruebas pasaron correctamente.")