from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analisis.diagrama_histograma import distribucionDeDatos, distribucionacumulada

graficasHistograma = Blueprint('graficas_histograma', __name__)


@graficasHistograma.route("/graficas/histograma-de-resultados")
def histograma():
    data = request.args
    result = distribucionDeDatos(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento')
                                 ,data.get('municipio'),data.get('colegio'))
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-acumulados")
def histogramaacumulado():
    data = request.args
    result = distribucionacumulada(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento')
                                 ,data.get('municipio'),data.get('colegio'))
    return make_response(jsonify(result), 200)
