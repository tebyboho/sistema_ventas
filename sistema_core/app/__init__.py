from flask import Flask
from .routes.main_routes import routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "una_clave_segura"
    app.register_blueprint(routes)  
    return app
