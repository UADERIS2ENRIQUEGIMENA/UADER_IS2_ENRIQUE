import time
import copy

class PrototipoAnidamiento:
    def __init__(self, nivel):
        self.nivel = nivel

    def clonar(self):
        return copy.deepcopy(self)

def procesar_anidamiento(prototipo, nivel):
    if nivel == 0:
        return

    print(f"Procesando nivel {nivel}...")
    time.sleep(2)  # Simulación de carga de procesamiento de 2 segundos

    nuevo_prototipo = prototipo.clonar()
    procesar_anidamiento(nuevo_prototipo, nivel - 1)

if __name__ == "__main__":
    prototipo_inicial = PrototipoAnidamiento(20)
    procesar_anidamiento(prototipo_inicial, 20)
