import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.history.append(memento)
        if len(self.history) > 4:  # Mantener solo los últimos 4 estados
            del self.history[0]

    def undo(self, steps=0):
        if steps >= len(self.history):
            steps = len(self.history) - 1
        if steps < 0:
            steps = 0

        memento = self.history[-1 - steps]
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps=0):
        writer.undo(steps)


if __name__ == '__main__':
    os.system("clear")
    caretaker = FileWriterCaretaker()

    writer = FileWriterUtility("GFG.txt")

    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se invoca al <undo>")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo>")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

