from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from sqlalchemy import text
from app.db import engine
from werkzeug.security import check_password_hash
main = Blueprint('main', __name__)

@main.route('/')
def login_form():
    return render_template('login.html')  # No pongas 'templates/' acá


@main.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    print(email, password)
    
    if not email or not password:
        flash("Se requiere email y contraseña", "danger")
        return redirect(url_for('main.login_form'))
        
    query = text( "SELECT id, nombre, password, rol_id FROM usuarios where email = :email")
    
    with engine.connect() as conn:
        result = conn.execute(query, {"email": email}).fetchone()
    
    if not result:
        flash("Usuario no encontrado", "danger")
        return redirect(url_for("main.login_form"))
    
    user_id, nombre, password_hash, rol_id = result
    
    if not check_password_hash(password_hash, password):
        flash("Contraseña incorrecta", "danger")
        return redirect(url_for("main.login_form"))
    
    session["user_id"] = user_id
    session["user_role"] = rol_id
    
    #empleado, encargado, admin, superusuario
    if rol_id == 1:
        return redirect(url_for("main.dashboard_empleado"))
    elif rol_id == 2:
        return redirect(url_for("main.dashboard_encargado"))
    elif rol_id == 3:
        return redirect(url_for("main.dashboard_administrador"))
    elif rol_id == 4:
        return redirect(url_for("main.dashboard_empleado"))
    
    else:
        flash("Rol no reconocido", "danger")
        return redirect(url_for("main.login_form"))
    

@main.route('/dashboard-empleado')
def dashboard_empleado():
    return render_template('dashboard_empleado.html')

@main.route('/dashboard-encargado')
def dashboard_encargado():
    return render_template('dashboard_encargado.html')

@main.route('/dashboard-administrador')
def dashboard_administrador():
    return render_template('dashboard_administrador.html')