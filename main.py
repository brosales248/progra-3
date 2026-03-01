from analyzer import TextAnalyzer


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                raise ValueError("El archivo está vacío.")
            return content
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except OSError:
        print("Error: Ruta inválida o problema de lectura.")
    except ValueError as e:
        print(f"Error: {e}")
    return ""


def read_console() -> str:
    print("Pegue el texto. Escriba END en una línea para finalizar:")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    text = "\n".join(lines)

    if not text.strip():
        print("Error: Texto vacío.")
    return text


def main():
    print("===== TEXT ANALYZER =====")
    print("1 - Modo archivo")
    print("2 - Modo consola")

    option = input("Seleccione una opción: ")

    if option == "1":
        path = input("Ingrese la ruta del archivo: ")
        text = read_file(path)
    elif option == "2":
        text = read_console()
    else:
        print("Opción inválida.")
        return

    if not text:
        return

    try:
        analyzer = TextAnalyzer(text)
        analyzer.analyze()
        analyzer.report()
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Modo interactivo
    while True:
        word = input("\nIngrese palabra para consultar (exit para salir): ")
        if word.lower() == "exit":
            print("Saliendo...")
            break
        analyzer.query(word)


if __name__ == "__main__":
    main()