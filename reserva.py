
# ==========================================
# CLASE RESERVA
# ==========================================

from entidad import Entidad
from cliente import Cliente
from servicio import Servicio

from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    OperacionNoPermitidaError
)

from logs_config import logger


class Reserva(Entidad):

    def __init__(self, identificacion, cliente, servicio, duracion):

        super().__init__(identificacion)

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("Cliente inválido.")

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Servicio inválido.")

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaInvalidaError("Duración inválida.")

        servicio.validar_parametros(duracion)

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._costo = 0

        logger.info("Reserva creada: %s", identificacion)

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    def confirmar(self, *args, **kwargs):

        if self._estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "La reserva no está pendiente."
            )

        if not self._servicio.disponible:
            raise ServicioNoDisponibleError(
                "El servicio no está disponible."
            )

        self._costo = self._servicio.calcular_costo(
            self._duracion, *args, **kwargs
        )

        self._estado = "Confirmada"

        logger.info("Reserva confirmada: %s", self.identificacion)

        return self._costo

    def cancelar(self):

        if self._estado in ("Cancelada", "Procesada"):
            raise OperacionNoPermitidaError(
                "No se puede cancelar esta reserva."
            )

        self._estado = "Cancelada"

        logger.info("Reserva cancelada: %s", self.identificacion)

    def procesar(self):

        if self._estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "Primero debe confirmar la reserva."
            )

        self._estado = "Procesada"

        logger.info("Reserva procesada: %s", self.identificacion)

    def describir(self):

        return (
            f"Reserva: {self.identificacion}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duración: {self._duracion} horas\n"
            f"Estado: {self._estado}\n"
            f"Costo: ${self._costo}"
        )
