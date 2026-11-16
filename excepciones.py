
# ==========================================
# EXCEPCIONES PERSONALIZADAS
# PROYECTO SOFTWARE FJ
# ==========================================

class ErrorSoftwareFJ(Exception):
    """Excepción general del sistema."""
    pass


class DatosInvalidosError(ErrorSoftwareFJ):
    """Error cuando los datos no son válidos."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Error cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Error cuando una reserva es incorrecta."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Error cuando una operación no está permitida."""
    pass
