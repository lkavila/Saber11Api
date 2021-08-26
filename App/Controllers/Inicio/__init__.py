from flask import Blueprint

main = Blueprint('inicio', __name__)

@main.route('/')
def home():
    return 'Welcome home'