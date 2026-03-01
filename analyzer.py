import string


def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("El texto debe ser un string.")

    text = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    text = " ".join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    if not text:
        return []
    return text.split()


class TextAnalyzer:
    def __init__(self, text: str):
        if not text.strip():
            raise ValueError("El texto no puede estar vacío.")

        self.original_text = text
        self.normalized_text = ""
        self.tokens = []
        self.counts = {}

    def analyze(self):
        self.normalized_text = normalize_text(self.original_text)
        self.tokens = tokenize(self.normalized_text)

        for token in self.tokens:
            self.counts[token] = self.counts.get(token, 0) + 1

    def report(self):
        total = len(self.tokens)
        unique = len(set(self.tokens))

        print("\n========== REPORTE ==========")
        print(f"Total de tokens: {total}")
        print(f"Tokens únicos: {unique}")

        if total == 0:
            print("No hay datos para analizar.")
            return

        print("\nTop 10 tokens más frecuentes:")
        sorted_tokens = sorted(self.counts.items(), key=lambda x: x[1], reverse=True)

        for token, count in sorted_tokens[:10]:
            print(f"{token}: {count}")

        avg_length = sum(len(t) for t in self.tokens) / total
        print(f"\nLongitud promedio de palabra: {avg_length:.2f}")

        max_len = max(len(t) for t in self.tokens)
        min_len = min(len(t) for t in self.tokens)

        longest = {t for t in self.tokens if len(t) == max_len}
        shortest = {t for t in self.tokens if len(t) == min_len}

        print(f"Palabras más largas: {longest}")
        print(f"Palabras más cortas: {shortest}")

    def query(self, word: str):
        word = word.lower()
        freq = self.counts.get(word, 0)
        total = len(self.tokens)

        if total == 0:
            print("No hay datos.")
            return

        percentage = (freq / total) * 100

        print("\n----- Consulta -----")
        print(f"Frecuencia: {freq}")
        print(f"Porcentaje: {percentage:.2f}%")

        if freq == 0:
            print("La palabra no aparece en el texto.")
        elif freq == 1:
            print("Clasificación: rara")
        elif freq >= 5:
            print("Clasificación: común")
        else:
            print("Clasificación: moderada")