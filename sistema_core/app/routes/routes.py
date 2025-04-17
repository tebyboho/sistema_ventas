from app.routes.main_routes import main
#from app.routes.auth_routes import auth_bp
#from app.routes.ventas_routes import ventas_bp
#from app.routes.stock_routes import stock_bp
#from app.routes.dashboard_routes import dashboard_bp

def register_blueprints(app):
    app.register_blueprint(main)  # login y dashboards, main_bp
    #app.register_blueprint(auth_bp)
    #app.register_blueprint(ventas_bp)
    #app.register_blueprint(stock_bp)
    #app.register_blueprint(dashboard_bp)
