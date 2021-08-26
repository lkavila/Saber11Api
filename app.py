from flask import Flask
from App.Infrastructure.Data import run as buscar_nuevos_archivos
from App.Controllers.Inicio import main

app = Flask(__name__)

app.register_blueprint(main)
buscar_nuevos_archivos()

if __name__ == '__main__':
    app.run()
