from flask import Flask
from App.Infrastructure.Data import run as buscar_nuevos_archivos
from App.Controllers.Inicio import main
from App.Controllers.mejores_colegios_controller import mejoresColegios
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(main)
app.register_blueprint(mejoresColegios)
buscar_nuevos_archivos()

if __name__ == '__main__':
    app.run()
