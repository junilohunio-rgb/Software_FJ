
# ==========================================
# PROGRAMA PRINCIPAL
# SOFTWARE FJ
# ==========================================

import logging

from cliente import Cliente

from servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reserva import Reserva
from sistema import SoftwareFJ

from excepciones import DatosInvalidosError


def ejecutar_sistema():

    sistema = SoftwareFJ()

    print("=" * 55)
    print("       BIENVENIDO AL SISTEMA SOFTWARE FJ")
    print("=" * 55)

    # OPERACIÓN 1: Cliente válido

    cliente1 = Cliente(
        "1001",
        "Carlos Pérez",
        "carlos@gmail.com",
        "3001234567"
    )

    sistema.ejecutar_operacion(
        "Registro de cliente válido",
        lambda: sistema.registrar_cliente(cliente1)
    )

    # OPERACIÓN 2: Segundo cliente

    cliente2 = Cliente(
        "1002",
        "María López",
        "maria@gmail.com",
        "3101234567"
    )

    sistema.ejecutar_operacion(
        "Registro de segundo cliente",
        lambda: sistema.registrar_cliente(cliente2)
    )

    # OPERACIÓN 3: Cliente inválido

    sistema.ejecutar_operacion(
        "Registro de cliente con correo inválido",
        lambda: sistema.registrar_cliente(
            Cliente(
                "1003",
                "Pedro Ruiz",
                "correo_invalido",
                "3201234567"
            )
        )
    )

    # OPERACIÓN 4: Servicio de salas

    sala = ReservaSala(
        "S001",
        "Sala de conferencias",
        50000,
        20
    )

    sistema.ejecutar_operacion(
        "Registro de sala",
        lambda: sistema.registrar_servicio(sala)
    )

    # OPERACIÓN 5: Servicio de equipos

    equipo = AlquilerEquipo(
        "S002",
        "Computadores",
        15000,
        5
    )

    sistema.ejecutar_operacion(
        "Registro de equipos",
        lambda: sistema.registrar_servicio(equipo)
    )

    # OPERACIÓN 6: Servicio de asesoría

    asesoria = AsesoriaEspecializada(
        "S003",
        "Asesoría informática",
        80000,
        "Tecnología"
    )

    sistema.ejecutar_operacion(
        "Registro de asesoría",
        lambda: sistema.registrar_servicio(asesoria)
    )

    # OPERACIÓN 7: Servicio incorrecto

    sistema.ejecutar_operacion(
        "Crear servicio con precio inválido",
        lambda: sistema.registrar_servicio(
            ReservaSala("S004", "Sala inválida", -100, 10)
        )
    )

    # OPERACIÓN 8: Reserva de sala

    reserva1 = Reserva(
        "R001", cliente1, sala, 2
    )

    def reservar_sala():

        sistema.registrar_reserva(reserva1)

        costo = reserva1.confirmar(
            impuesto=0.19,
            descuento=10
        )

        print("Costo de la reserva:", costo)

    sistema.ejecutar_operacion(
        "Reserva exitosa de sala",
        reservar_sala
    )

    # OPERACIÓN 9: Reserva de equipos

    reserva2 = Reserva(
        "R002", cliente2, equipo, 3
    )

    def reservar_equipo():

        sistema.registrar_reserva(reserva2)

        print("Costo:", reserva2.confirmar())

    sistema.ejecutar_operacion(
        "Reserva de equipos",
        reservar_equipo
    )

    # OPERACIÓN 10: Reserva de asesoría

    reserva3 = Reserva(
        "R003", cliente1, asesoria, 2
    )

    def reservar_asesoria():

        sistema.registrar_reserva(reserva3)

        print("Costo:", reserva3.confirmar(0.19, 5))

    sistema.ejecutar_operacion(
        "Reserva de asesoría",
        reservar_asesoria
    )

    # OPERACIÓN 11: Duración negativa

    sistema.ejecutar_operacion(
        "Reserva con duración negativa",
        lambda: sistema.registrar_reserva(
            Reserva("R004", cliente1, sala, -2)
        )
    )

    # OPERACIÓN 12: Servicio no disponible

    sala.disponible = False

    reserva4 = Reserva(
        "R005", cliente2, sala, 1
    )

    def reservar_no_disponible():

        sistema.registrar_reserva(reserva4)
        reserva4.confirmar()

    sistema.ejecutar_operacion(
        "Servicio no disponible",
        reservar_no_disponible
    )

    sala.disponible = True

    # OPERACIÓN 13: Cancelación

    sistema.ejecutar_operacion(
        "Cancelar reserva de equipos",
        reserva2.cancelar
    )

    # OPERACIÓN 14: Procesar reserva

    sistema.ejecutar_operacion(
        "Procesar reserva confirmada",
        reserva1.procesar
    )

    # OPERACIÓN 15: Cancelación no permitida

    sistema.ejecutar_operacion(
        "Cancelar reserva procesada",
        reserva1.cancelar
    )

    # OPERACIÓN 16: Cálculo con descuento

    sistema.ejecutar_operacion(
        "Calcular costo con descuento",
        lambda: print(
            sala.calcular_costo(2, 0.19, 15)
        )
    )

    # OPERACIÓN 17: Cálculo estándar

    sistema.ejecutar_operacion(
        "Calcular costo estándar",
        lambda: print(
            asesoria.calcular_costo(2)
        )
    )

    # OPERACIÓN 18: Encadenamiento de excepciones

    def encadenar_error():

        try:
            int("dato incorrecto")

        except ValueError as error:

            raise DatosInvalidosError(
                "Error de conversión de datos."
            ) from error

    sistema.ejecutar_operacion(
        "Encadenamiento de excepciones",
        encadenar_error
    )

    # OPERACIÓN 19: Consultar información

    sistema.ejecutar_operacion(
        "Consultar clientes",
        sistema.listar_clientes
    )

    # OPERACIÓN 20: Consultar servicios

    sistema.ejecutar_operacion(
        "Consultar servicios",
        sistema.listar_servicios
    )

    # OPERACIÓN 21: Consultar reservas

    sistema.ejecutar_operacion(
        "Consultar reservas",
        sistema.listar_reservas
    )

    print("\n" + "=" * 55)
    print("       RESUMEN FINAL SOFTWARE FJ")
    print("=" * 55)

    print("Total de clientes:", len(sistema.clientes))
    print("Total de servicios:", len(sistema.servicios))
    print("Total de reservas:", len(sistema.reservas))

    print("\nEventos y errores guardados en software_fj.log")


if __name__ == "__main__":

    try:

        ejecutar_sistema()

    except Exception:

        logging.exception("Error crítico del sistema.")

        print("Se presentó un error crítico.")

    finally:

        logging.shutdown()

        print("\nPROGRAMA FINALIZADO.")
