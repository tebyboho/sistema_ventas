from werkzeug.security import generate_password_hash
from sqlalchemy import text 
from app.db import engine 

'''This is a testing function. In the future will be adapted to a production one'''
def crear_usuario(nombre, email, password, rol_id):
    # se hashea la contraseña 
    password_hash = generate_password_hash(password)
    
    
    '''Uso RAW SQL Queries, para control total de las queries'''
    
    query = text("""
                 INSERT INTO usuarios (nombre, email, password, rol_id)
                 VALUES (:nombre, :email, :password, :rol_id)
            """)
    
    with engine.connect() as conn:
        conn.execute(query, {
            'nombre': nombre,
            'email': email, 
            'password': password_hash,
            'rol_id': rol_id
        })
        conn.commit() # guardo los cambios en la BD
    print("Usuario creado con éxito✅")
    

'''Function for testing environment. In the future will be adapted as a production one'''

def eliminar_usuario(user_id=None):
    with engine.connect() as conn:
        if user_id:
            conn.execute(text(f"DELETE FROM usuarios WHERE id = {user_id}"))
        else:
            conn.execute(text("TRUNCATE TABLE usuarios RESTART IDENTITY CASCADE"))
        
        conn.commit()
    print("Usuario eliminado con éxito✅")
    

def mostrar_usuarios():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM usuarios")).fetchall()
        print(result)
        
#crear_usuario('Daira', 'correo1@gmail.com', 'admin', 1 )
#crear_usuario('Magali', 'correo2@gmail.com', 'admin', 2 )
#crear_usuario('Gabriela', 'correo3@gmail.com', 'admin', 3 )
#crear_usuario('Teby', 'correo4@gmail.com', 'admin', 4 )
#eliminar_usuario()
#mostrar_usuarios()