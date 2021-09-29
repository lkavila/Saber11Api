from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analysis.promedios_y_desviaciones import promedio_departamental, desviacion_departamental

promedioDepartamento = Blueprint('promedio_departamento', __name__)

@promedioDepartamento.route('/promedio-departamento')
def home():
    data = request.get_json()
    result = {
        f"promedio {data['periodo']}": promedio_departamental (data['periodo']),
        f"desviacion {data['periodo']}": desviacion_departamental(data['periodo'])
    }

    return make_response(jsonify(result), 200)