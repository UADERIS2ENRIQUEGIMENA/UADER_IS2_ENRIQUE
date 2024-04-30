class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, id_emito):
        for observer in self._observers:
            observer.update(id_emito)


class Observer:
    def __init__(self, id_esperado):
        self._id_esperado = id_esperado

    def update(self, id_emito):
        if id_emito == self._id_esperado:
            print(f"¡El ID emitido ({id_emito}) coincide con el ID esperado ({self._id_esperado})!")


# Implementar cuatro clases de observadores con IDs específicos
class ObserverA(Observer):
    def __init__(self):
        super().__init__("ABCD")

class ObserverB(Observer):
    def __init__(self):
        super().__init__("EFGH")

class ObserverC(Observer):
    def __init__(self):
        super().__init__("IJKL")

class ObserverD(Observer):
    def __init__(self):
        super().__init__("MNOP")


# Crear un sujeto y suscribir los observadores
subject = Subject()
subject.attach(ObserverA())
subject.attach(ObserverB())
subject.attach(ObserverC())
subject.attach(ObserverD())

# Emitir 8 IDs
IDs = ["ABCD", "EFGH", "IJKL", "MNOP", "QRST", "UVWX", "YZ12", "3456"]
for ID in IDs:
    subject.notify(ID)
