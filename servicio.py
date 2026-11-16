
# ==========================================
# CLASE ABSTRACTA SERVICIO
# ==========================================

from abc import ABC, abstractmethod

from excepciones import DatosInvalidosError


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base):

        if not isinstance(codigo, str) or not codigo.strip():
            raise DatosInvalidosError("Código inválido.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("Nombre inválido.")

        if isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)) or precio_base <= 0:
            raise DatosInvalidosError("Precio inválido.")

        self._codigo = codigo
        self._nombre = nombre
        self._precio_base = float(precio_base)
        self._disponible = True

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):

        if not isinstance(valor, bool):
            raise DatosInvalidosError("Disponibilidad inválida.")

        self._disponible = valor

    @abstractmethod
    def calcular_costo(self, duracion, *args, **kwargs):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    def aplicar_impuestos_y_descuentos(
        self, costo, impuesto=0.19, descuento=0
    ):

        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 1:
            raise DatosInvalidosError("Impuesto inválido.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("Descuento inválido.")

        total = costo * (1 - descuento / 100)
        total *= (1 + impuesto)

        return round(total, 2)
