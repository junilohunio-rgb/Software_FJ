
# ==========================================
# CLASE CLIENTE
# ==========================================

from entidad import Entidad
from excepciones import DatosInvalidosError
from logs_config import logger


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        self.__nombre = None
        self.__correo = None
        self.__telefono = None

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

        logger.info("Cliente registrado: %s", identificacion)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatosInvalidosError("Nombre inválido.")

        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise DatosInvalidosError("Correo inválido.")

        self.__correo = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        if not isinstance(valor, str) or not valor.isdigit() or len(valor) < 7:
            raise DatosInvalidosError("Teléfono inválido.")

        self.__telefono = valor

    def describir(self):

        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )
