class Hamburguesa:
    def __init__(self):
        self.estado = MostradorState()

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def entregar(self):
        self.estado.entregar()


class EstadoEntrega:
    def entregar(self):
        raise NotImplementedError("Subclases deben implementar este método")


class MostradorState(EstadoEntrega):
    def entregar(self):
        print("La hamburguesa está lista para ser retirada en el mostrador.")


class RetiroClienteState(EstadoEntrega):
    def entregar(self):
        print("La hamburguesa está lista para ser retirada por el cliente.")


class DeliveryState(EstadoEntrega):
    def entregar(self):
        print("La hamburguesa está lista para ser enviada por delivery.")


# Ejemplo de uso
if __name__ == "__main__":
    hamburguesa = Hamburguesa()

    # Entrega en mostrador
    hamburguesa.cambiar_estado(MostradorState())
    hamburguesa.entregar()

    # Entrega para retiro por cliente
    hamburguesa.cambiar_estado(RetiroClienteState())
    hamburguesa.entregar()

    # Entrega por delivery
    hamburguesa.cambiar_estado(DeliveryState())
    hamburguesa.entregar()
