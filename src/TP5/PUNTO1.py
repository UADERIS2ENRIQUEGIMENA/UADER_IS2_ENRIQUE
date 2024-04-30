class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, number):
        if self.successor:
            self.successor.handle_request(number)
        else:
            print(f"El número {number} no fue consumido.")

class NumeroPrimoHandler(Handler):
    def handle_request(self, number):
        if self._es_primo(number):
            print(f"El número {number} es primo.")
        else:
            super().handle_request(number)

    def _es_primo(self, number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

class NumeroParHandler(Handler):
    def handle_request(self, number):
        if self._es_par(number):
            print(f"El número {number} es par.")
        else:
            super().handle_request(number)

    def _es_par(self, number):
        return number % 2 == 0

# Configurar la cadena de responsabilidad
handler_par = NumeroParHandler()
handler_primo = NumeroPrimoHandler(handler_par)

# Probar la cadena de responsabilidad con números del 1 al 100
for i in range(1, 101):
    handler_primo.handle_request(i)

