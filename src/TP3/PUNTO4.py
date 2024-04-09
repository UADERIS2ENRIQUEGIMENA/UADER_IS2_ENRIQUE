class Factura:
    def __init__(self, importe, estrategia_impositiva):
        self.importe = importe
        self.estrategia_impositiva = estrategia_impositiva

    def calcular_importe_total(self):
        return self.estrategia_impositiva.calcular_importe_total(self.importe)


class EstrategiaImpositiva:
    def calcular_importe_total(self, importe):
        raise NotImplementedError("Subclases deben implementar este método")


class IVAResponsable(EstrategiaImpositiva):
    def calcular_importe_total(self, importe):
        return importe * 1.21


class IVANoInscripto(EstrategiaImpositiva):
    def calcular_importe_total(self, importe):
        return importe


class IVAExento(EstrategiaImpositiva):
    def calcular_importe_total(self, importe):
        return importe


# Ejemplo de uso
if __name__ == "__main__":
    # Factura para cliente IVA Responsable
    factura1 = Factura(100, IVAResponsable())
    print("Factura para IVA Responsable:", factura1.calcular_importe_total())

    # Factura para cliente IVA No Inscripto
    factura2 = Factura(100, IVANoInscripto())
    print("Factura para IVA No Inscripto:", factura2.calcular_importe_total())

    # Factura para cliente IVA Exento
    factura3 = Factura(100, IVAExento())
    print("Factura para IVA Exento:", factura3.calcular_importe_total())
