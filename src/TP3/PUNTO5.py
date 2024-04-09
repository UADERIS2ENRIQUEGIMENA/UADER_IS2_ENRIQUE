class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = []
        self.alas = []
        self.tren_aterrizaje = None

    def __str__(self):
        partes = [self.body] + self.turbinas + self.alas + [self.tren_aterrizaje]
        partes_str = ', '.join(partes)
        return f"Avión: [{partes_str}]"


class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self, body):
        self.avion.body = body

    def construir_turbina(self, turbina):
        self.avion.turbinas.append(turbina)

    def construir_alas(self, alas):
        self.avion.alas.extend(alas)

    def construir_tren_aterrizaje(self, tren):
        self.avion.tren_aterrizaje = tren

    def obtener_avion(self):
        return self.avion


class AvionDirector:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion(self):
        self.builder.construir_body("Cuerpo del avión")
        self.builder.construir_turbina("Turbina 1")
        self.builder.construir_turbina("Turbina 2")
        self.builder.construir_alas(["Ala izquierda", "Ala derecha"])
        self.builder.construir_tren_aterrizaje("Tren de aterrizaje")


# Ejemplo de uso
if __name__ == "__main__":
    builder = AvionBuilder()
    director = AvionDirector(builder)
    director.construir_avion()
    avion = builder.obtener_avion()
    print(avion)
