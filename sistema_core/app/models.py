from sqlalchemy import create_engine, MetaData, Table
from app.db import engine

# Instancia de MetaData
metadata = MetaData()

# Reflejar las tablas ya existentes en la base de datos
metadata.reflect(bind=engine)

# Asignar las tablas reflejadas a variables para usarlas en el código
usuarios = metadata.tables["usuarios"]
roles = metadata.tables["roles"]
productos = metadata.tables["productos"]
categorias = metadata.tables["categorias"]
ventas = metadata.tables["ventas"]
detalles_ventas = metadata.tables["detalles_ventas"]
stock = metadata.tables["stock"]
sucursales = metadata.tables["sucursales"]

print("✅ Tablas reflejadas correctamente.")
