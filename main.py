from contador import ContadorPalabras

def main():
    texto = input("Introduce el texto para contar las palabras: ")
    contador = ContadorPalabras(texto)
    print(f"El número de palabras es: {contador.contar_palabras()}")

if __name__ == "__main__":
    main()
