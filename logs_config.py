
# ==========================================
# CONFIGURACIÓN DE REGISTRO DE EVENTOS
# PROYECTO SOFTWARE FJ
# ==========================================

import logging

logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8
)

logger = logging.getLogger("SoftwareFJ")
