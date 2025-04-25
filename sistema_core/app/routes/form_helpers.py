from sqlalchemy import text
from app.db import engine


def get_form_data(*tables):
    """
    Devuelve los registros de las tablas pasadas como argumentos.
    Ej: get_form_data("categorias", "talles") → {"categorias": [...], "talles": [...]}
    """
    
    data = {}
    
    with engine.connect() as conn:
        for table in tables:
            try: 
                result = conn.execute(text(f"SELECT id, nombre FROM {table}")).fetchall()
                data[table] = result
            except Exception as e:
                print(f"[Error] No se pudo obtener la tabla {table}: {e}")
                data[table] = []
    
    return data