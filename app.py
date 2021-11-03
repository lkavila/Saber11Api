from flask import Flask
from App.Infrastructure.Data import run as buscar_nuevos_archivos
from App.Controllers.Inicio import main
from App.Controllers.mejores_colegios_controller import mejoresColegios
from App.Controllers.diagrama_caja_controller import diagramaCaja
from App.Controllers.general_controller import generalData
from App.Controllers.buscar_colegios_controller import buscarColegio
from App.Controllers.grafica_lineas_controller import graficasLineas
from App.Controllers.promedio_general_contoller import promedioGeneralMunicipalDepartamental
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(main)
app.register_blueprint(mejoresColegios)
app.register_blueprint(diagramaCaja)
app.register_blueprint(generalData)
app.register_blueprint(buscarColegio)
buscar_nuevos_archivos()
app.register_blueprint(graficasLineas)
app.register_blueprint(promedioGeneralMunicipalDepartamental)

if __name__ == '__main__':
    app.run()
