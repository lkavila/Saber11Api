from flask import Flask
from App.Controllers.Colegios.mejores_colegios_controller import mejoresColegios
from App.Controllers.General.diagrama_caja_controller import diagramaCaja
from App.Controllers.General.general_controller import generalData
from App.Controllers.Colegios.buscar_colegios_controller import buscarColegio
from App.Controllers.General.grafica_lineas_controller import graficasLineas
from App.Controllers.General.grafica_histograma_controller import graficasHistograma
from App.Controllers.General.promedio_general_contoller import promedioGeneralMunicipalDepartamental
from App.Controllers.General.predecir_clasificacion_controller import predecirClasificacion
from App.Controllers.Colegios.analisis_colegios_controller import analisisColegio
from App.Controllers.General.numero_estudiantes_puntajes_controller import numeroDeEsrudiantesPorRangoPuntaje
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(analisisColegio)
app.register_blueprint(mejoresColegios)
app.register_blueprint(diagramaCaja)
app.register_blueprint(generalData)
app.register_blueprint(buscarColegio)
app.register_blueprint(graficasLineas)
app.register_blueprint(graficasHistograma)
app.register_blueprint(promedioGeneralMunicipalDepartamental)
app.register_blueprint(predecirClasificacion)
app.register_blueprint(numeroDeEsrudiantesPorRangoPuntaje)

if __name__ == '__main__':
    app.run()
