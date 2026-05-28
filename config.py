import os
from pathlib import Path
import sys

RUTA_DATOS = os.path.join(
    os.path.expanduser("~"),
    "Documents",
    "MecaSoftData"
)

RUTA_FOTOS_PERSONAL = os.path.join(
    RUTA_DATOS,
    "fotos_personal"
)

RUTA_FOTOS_VEHICULOS = os.path.join(
    RUTA_DATOS,
    "fotos_vehiculos"
)

RUTA_BACKUPS = os.path.join(
    RUTA_DATOS,
    "backups"
)

RUTA_DB = os.path.join(
    RUTA_DATOS,
    "gestion_mecanica.db"
)

def inicializar_sistema():

    os.makedirs(RUTA_DATOS, exist_ok=True)

    os.makedirs(
        RUTA_FOTOS_PERSONAL,
        exist_ok=True
    )

    os.makedirs(
        RUTA_FOTOS_VEHICULOS,
        exist_ok=True
    )

    os.makedirs(
        RUTA_BACKUPS,
        exist_ok=True
    )

    print("Directorios del sistema verificados.")


def ruta_recurso(relative_path):
    if getattr(sys, "frozen", False):
        base_path = Path(sys.executable).parent
    else:
        base_path = Path(__file__).parent

    return str(base_path / relative_path)