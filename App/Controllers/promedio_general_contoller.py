from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analysis.promedios_y_desviaciones import promedio_nacional, desviacion_nacional

promedioGeneral = Blueprint('promedio_general', __name__)

@promedioGeneral.route('/promediogeneral')
def home():
    data = request.get_json()
    result = {
        f"promedio {data['periodo']}": promedio_nacional (data['periodo']),
        f"desviacion {data['periodo']}": desviacion_nacional(data['periodo'])
    }

    return make_response(jsonify(result), 200)