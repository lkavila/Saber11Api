from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analysis.diagrama_caja import diagrama_caja

diagramaCaja = Blueprint('diagrama_caja', __name__)

@diagramaCaja.route('/diagrama_caja')
def diagrama_caja_global():
    data = request.args
    print("Diagrma de caja", data.get('periodo', ''))
    resultado = diagrama_caja(int(data.get('periodo', '')), data.get('variable'), data.get('puntaje'))
    return make_response(jsonify(resultado), 200)
