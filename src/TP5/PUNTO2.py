class IteradorCadena:
    def __init__(self, cadena):
        self._cadena = cadena
        self._indice = 0
        self._sentido_directo = True

    def __iter__(self):
        return self

    def __next__(self):
        if self._sentido_directo:
            if self._indice < len(self._cadena):
                caracter = self._cadena[self._indice]
                self._indice += 1
                return caracter
            else:
                raise StopIteration
        else:
            if self._indice >= 0:
                caracter = self._cadena[self._indice]
                self._indice -= 1
                return caracter
            else:
                raise StopIteration

    def cambiar_sentido(self):
        self._sentido_directo = not self._sentido_directo


# Ejemplo de uso
cadena = "Hola Mundo"
iterador = IteradorCadena(cadena)

# Recorrido en sentido directo
print("Sentido directo:")
for caracter in iterador:
    print(caracter, end=" ")
print()

# Cambiar sentido
iterador.cambiar_sentido()

# Recorrido en sentido inverso
print("Sentido inverso:")
for caracter in iterador:
    print(caracter, end=" ")
print()
