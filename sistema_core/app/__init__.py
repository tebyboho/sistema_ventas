from flask import Flask
from .routes.main_routes import main
from .routes.stock_routes import stock

def create_app():
    app = Flask(__name__)
    app.secret_key = "una_clave_segura"
    app.register_blueprint(main)  
    app.register_blueprint(stock)
    return app
