class ContadorPalabras:
    def __init__(self, texto):
        self.texto = texto
        
    def contar_palabras(self):
        palabras = self.texto.split()
        return len(palabras)
