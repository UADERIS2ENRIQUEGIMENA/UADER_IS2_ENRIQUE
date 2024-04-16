class LaminaAcero:
    def __init__(self, espesor, ancho):
        self.espesor = espesor
        self.ancho = ancho

    def producir(self, laminador):
        pass

class Laminador:
    def __init__(self, longitud):
        self.longitud = longitud

    def laminar(self, lamina):
        pass

class Laminador5m(Laminador):
    def __init__(self):
        super().__init__(5)

    def laminar(self, lamina):
        print(f"Laminando lamina de {lamina.ancho} metros en un laminador de 5 metros")

class Laminador10m(Laminador):
    def __init__(self):
        super().__init__(10)

    def laminar(self, lamina):
        print(f"Laminando lamina de {lamina.ancho} metros en un laminador de 10 metros")

class LaminaConcreta(LaminaAcero):
    def producir(self, laminador):
        laminador.laminar(self)

# Ejemplo de uso
lamina = LaminaConcreta(0.5, 1.5)

laminador_5m = Laminador5m()
laminador_10m = Laminador10m()

lamina.producir(laminador_5m)
lamina.producir(laminador_10m)
