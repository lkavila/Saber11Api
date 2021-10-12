from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analysis.promedios_y_desviaciones import desviacion_municipal

promedioMunicipal = Blueprint('promedio_municipal', __name__)

@promedioMunicipal.route('/promediomunicipal')
def home():
    data = request.get_json()
    result = {
       # f"promedio {data['periodo']}": promedio_municipal (data['periodo']),
        f"desviacion {data['periodo']}": desviacion_municipal(data['periodo'])
    }

    return make_response(jsonify(result), 200)