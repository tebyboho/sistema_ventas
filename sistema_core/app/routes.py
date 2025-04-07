from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def login_form():
    return render_template('login.html')  # No pongas 'templates/' acá


