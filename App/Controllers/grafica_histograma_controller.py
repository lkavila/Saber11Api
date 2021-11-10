from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analysis.diagrama_histograma import distribucionDeDatos

graficasHistograma = Blueprint('graficas_histograma', __name__)


@graficasHistograma.route("/graficas/histograma-de-resultados")
def histograma():
    data = request.args
    result = distribucionDeDatos(int(data.get('periodo','')),data.get('tpuntuacion'))
    return make_response(jsonify(result), 200)