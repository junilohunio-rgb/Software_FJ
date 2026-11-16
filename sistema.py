
# ==========================================
# CLASE PRINCIPAL SOFTWARE FJ
# ==========================================

from cliente import Cliente
from servicio import Servicio
from reserva import Reserva

from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    ErrorSoftwareFJ
)

from logs_config import logger


class SoftwareFJ:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

        logger.info("Sistema Software FJ iniciado.")

    def registrar_cliente(self, cliente):

        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("Cliente inválido.")

        if any(c.identificacion == cliente.identificacion
               for c in self.clientes):
            raise DatosInvalidosError("Cliente duplicado.")

        self.clientes.append(cliente)

        logger.info("Cliente registrado correctamente.")

    def registrar_servicio(self, servicio):

        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError("Servicio inválido.")

        if any(s.codigo == servicio.codigo for s in self.servicios):
            raise DatosInvalidosError("Servicio duplicado.")

        self.servicios.append(servicio)

        logger.info("Servicio registrado correctamente.")

    def registrar_reserva(self, reserva):

        if not isinstance(reserva, Reserva):
            raise ReservaInvalidaError("Reserva inválida.")

        if not any(c is reserva._cliente for c in self.clientes):
            raise ReservaInvalidaError("Cliente no registrado.")

        if not any(s is reserva._servicio for s in self.servicios):
            raise ReservaInvalidaError("Servicio no registrado.")

        if any(r.identificacion == reserva.identificacion
               for r in self.reservas):
            raise ReservaInvalidaError("Reserva duplicada.")

        self.reservas.append(reserva)

        logger.info("Reserva registrada correctamente.")

    def listar_clientes(self):

        print("\n===== CLIENTES =====")

        for cliente in self.clientes:
            print(cliente.describir())

    def listar_servicios(self):

        print("\n===== SERVICIOS =====")

        for servicio in self.servicios:
            print(servicio.describir())

    def listar_reservas(self):

        print("\n===== RESERVAS =====")

        for reserva in self.reservas:
            print(reserva.describir())
            print("-" * 40)

    def ejecutar_operacion(self, descripcion, operacion):

        print(f"\nOPERACIÓN: {descripcion}")

        try:

            operacion()

        except ErrorSoftwareFJ as error:

            logger.error("Error controlado: %s", error)

            print("ERROR CONTROLADO:", error)

        except Exception as error:

            logger.exception("Error inesperado.")

            print("ERROR INESPERADO:", error)

        else:

            logger.info("Operación exitosa: %s", descripcion)

            print("Operación exitosa.")

        finally:

            print("El sistema continúa funcionando.")
