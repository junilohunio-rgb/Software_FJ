
# ==========================================
# SERVICIOS ESPECIALIZADOS SOFTWARE FJ
# ==========================================

from servicio import Servicio
from excepciones import DatosInvalidosError


class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, precio_base, capacidad):

        super().__init__(codigo, nombre, precio_base)

        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError("Capacidad inválida.")

        self.capacidad = capacidad

    def validar_parametros(self, duracion):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError("Duración inválida.")

    def calcular_costo(self, duracion, *args, **kwargs):

        self.validar_parametros(duracion)

        impuesto = kwargs.get("impuesto", 0.19)
        descuento = kwargs.get("descuento", 0)

        if len(args) > 2:
            raise DatosInvalidosError("Demasiados parámetros.")

        if len(args) >= 1:
            impuesto = args[0]

        if len(args) == 2:
            descuento = args[1]

        costo = self._precio_base * duracion

        return self.aplicar_impuestos_y_descuentos(
            costo, impuesto, descuento
        )

    def describir(self):

        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} | "
            f"Precio por hora: ${self._precio_base}"
        )


class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio_base, cantidad):

        super().__init__(codigo, nombre, precio_base)

        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise DatosInvalidosError("Cantidad inválida.")

        self.cantidad = cantidad

    def validar_parametros(self, duracion):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError("Duración inválida.")

    def calcular_costo(self, duracion, *args, **kwargs):

        self.validar_parametros(duracion)

        impuesto = kwargs.get("impuesto", 0.19)
        descuento = kwargs.get("descuento", 0)

        if len(args) > 2:
            raise DatosInvalidosError("Demasiados parámetros.")

        if len(args) >= 1:
            impuesto = args[0]

        if len(args) == 2:
            descuento = args[1]

        costo = self._precio_base * duracion * self.cantidad

        return self.aplicar_impuestos_y_descuentos(
            costo, impuesto, descuento
        )

    def describir(self):

        return (
            f"Equipo: {self.nombre} | "
            f"Cantidad: {self.cantidad} | "
            f"Precio por hora: ${self._precio_base}"
        )


class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio_base, especialidad):

        super().__init__(codigo, nombre, precio_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("Especialidad inválida.")

        self.especialidad = especialidad.strip()

    def validar_parametros(self, duracion):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError("Duración inválida.")

    def calcular_costo(self, duracion, *args, **kwargs):

        self.validar_parametros(duracion)

        impuesto = kwargs.get("impuesto", 0.19)
        descuento = kwargs.get("descuento", 0)

        if len(args) > 2:
            raise DatosInvalidosError("Demasiados parámetros.")

        if len(args) >= 1:
            impuesto = args[0]

        if len(args) == 2:
            descuento = args[1]

        costo = self._precio_base * duracion

        return self.aplicar_impuestos_y_descuentos(
            costo, impuesto, descuento
        )

    def describir(self):

        return (
            f"Asesoría: {self.nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Precio por hora: ${self._precio_base}"
        )
