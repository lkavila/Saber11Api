from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analysis.mejores_colegios import mejores_colegios

mejoresColegios = Blueprint('mejores_colegios', __name__)


@mejoresColegios.route('/mejores-colegios')
def home():
    data = request.get_json()
    result = {
        f"Mejores colegios {data['periodo']}": mejores_colegios(data['periodo'], data['departamento'],
                                                                data['municipio'], data['puntajes'],
                                                                data['top'], data['num_estudiantes']),
    }

    return make_response(jsonify(result), 200)
