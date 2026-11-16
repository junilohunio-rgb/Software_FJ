
# ==========================================
# CLASE ABSTRACTA ENTIDAD
# ==========================================

from abc import ABC, abstractmethod

from excepciones import DatosInvalidosError


class Entidad(ABC):

    def __init__(self, identificacion):

        if not isinstance(identificacion, str) or not identificacion.strip():
            raise DatosInvalidosError(
                "La identificación es obligatoria."
            )

        self._identificacion = identificacion.strip()

    @property
    def identificacion(self):
        return self._identificacion

    @abstractmethod
    def describir(self):
        pass
