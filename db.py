from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import os
from config.config import DB_CONFIG


# Construcción de la URL de conexión
DATABASE_URL = URL.create(
    drivername="postgresql",
    username=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    database=DB_CONFIG["dbname"],
)

# Crear la conexión a la base de datos
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver las consultas en consola

# Función para obtener la conexión
def get_connection():
    return engine.connect()