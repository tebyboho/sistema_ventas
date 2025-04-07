from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import SQLAlchemyError
from app.config import DB_CONFIG


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

def test_connection():
    try:
        with engine.connect() as connection:
            print("✅ Conexión a PostgreSQL exitosa.")
    except SQLAlchemyError as e:
        print(f"❌ Error de conexión: {e}")
        
if __name__ == "__main__":
    test_connection()