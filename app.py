from flask import Flask

from App.Controllers.promedio_municipios import promedioMunicipal
from App.Infrastructure.Data import run as buscar_nuevos_archivos
from App.Controllers.Inicio import main
from App.Controllers.mejores_colegios_controller import mejoresColegios
from App.Controllers.promedio_general_contoller import  promedioGeneral
from App.Controllers.promedio_departamentos_controller import promedioDepartamento
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(main)
app.register_blueprint(mejoresColegios)
app.register_blueprint(promedioGeneral)
app.register_blueprint(promedioDepartamento)
app.register_blueprint(promedioMunicipal)
buscar_nuevos_archivos()

if __name__ == '__main__':
    app.run()
