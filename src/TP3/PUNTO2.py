class TaxCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate_taxes(self, base_amount):
        iva = base_amount * 0.21
        iibb = base_amount * 0.05
        municipal_contributions = base_amount * 0.012
        total_tax = iva + iibb + municipal_contributions
        return total_tax


# Ejemplo de uso
if __name__ == "__main__":
    # Obtener la instancia única del calculador de impuestos
    tax_calculator1 = TaxCalculator()
    tax_calculator2 = TaxCalculator()

    # Ambos objetos son la misma instancia
    print(tax_calculator1 is tax_calculator2)  # Devolverá True

    # Calcular impuestos para un importe base
    base_amount = 1000
    total_tax = tax_calculator1.calculate_taxes(base_amount)
    print(f"Total de impuestos a pagar: {total_tax}")
