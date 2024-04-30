import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

    def preset(self, station):
        print("Sintonizando a la frecuencia memorizada {} {}".format(station, self.name))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
        self.memories = {}

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def preset_station(self, memory, station):
        self.memories[memory] = station

    def preset(self, memory):
        if memory in self.memories:
            self.radio.state.preset(self.memories[memory])
        else:
            print("No hay frecuencia memorizada en la memoria {}".format(memory))

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"
        self.memories = {}

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def preset_station(self, memory, station):
        self.memories[memory] = station

    def preset(self, memory):
        if memory in self.memories:
            self.radio.state.preset(self.memories[memory])
        else:
            print("No hay frecuencia memorizada en la memoria {}".format(memory))

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def preset_station(self, memory, station):
        self.state.preset_station(memory, station)

    def preset(self, memory):
        self.state.preset(memory)

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()

    # Configurar memorias
    radio.preset_station("M1", "89.1")  # Memoria M1 para FM
    radio.preset_station("M2", "1250")  # Memoria M2 para AM

    print("\nMemorias configuradas:")
    print("M1 (FM):", radio.amstate.memories.get("M1", "Vacía"))
    print("M2 (AM):", radio.fmstate.memories.get("M2", "Vacía"))

    # Agregar frecuencia memorizada durante el ciclo de barrido
    radio.preset("M1")
    radio.preset("M2")
    radio.scan()  # Continuar con el ciclo de barrido
