class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print("Valor actual:", self.valor)


class OperacionDecorator:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        self.numero.imprimir()


class SumarDos(OperacionDecorator):
    def imprimir(self):
        self.numero.imprimir()
        self.numero.valor += 2
        print("Después de sumarle 2:", self.numero.valor)


class MultiplicarPorDos(OperacionDecorator):
    def imprimir(self):
        self.numero.imprimir()
        self.numero.valor *= 2
        print("Después de multiplicar por 2:", self.numero.valor)


class DividirPorTres(OperacionDecorator):
    def imprimir(self):
        self.numero.imprimir()
        self.numero.valor /= 3
        print("Después de dividir por 3:", self.numero.valor)


# Ejemplo de uso
num = Numero(5)
num.imprimir()

print("\nOperaciones agregadas:")
operacion_suma = SumarDos(num)
operacion_mult = MultiplicarPorDos(operacion_suma)
operacion_div = DividirPorTres(operacion_mult)

operacion_div.imprimir()
