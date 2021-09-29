from flask import Flask
from App.Infrastructure.Data import run as buscar_nuevos_archivos
from App.Controllers.Inicio import main
from App.Controllers.mejores_colegios_controller import mejoresColegios
from App.Controllers.promedio_general_contoller import  promedioGeneral
from App.Controllers.promedio_departamentos_controller import promedioDepartamento
app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(mejoresColegios)
app.register_blueprint(promedioGeneral)
app.register_blueprint(promedioDepartamento)
buscar_nuevos_archivos()

if __name__ == '__main__':
    app.run()
