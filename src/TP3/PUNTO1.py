class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate_factorial(self, number):
        if number < 0:
            raise ValueError("El número debe ser no negativo.")
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        return factorial


# Ejemplo de uso
if __name__ == "__main__":
    # Obtener la instancia única
    calculator1 = FactorialCalculator()
    calculator2 = FactorialCalculator()

    # Ambos objetos son la misma instancia
    print(calculator1 is calculator2)  # Devolverá True

    # Calcular el factorial de un número
    number = 5
    factorial = calculator1.calculate_factorial(number)
    print(f"El factorial de {number} es: {factorial}")
