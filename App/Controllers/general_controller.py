from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analysis.datos_generales import obtener_departamentos_y_municipios_colegios

generalData = Blueprint('general_data', __name__)

@generalData.route('/datos-generales/departamentos-municipios-cole')
def obtener_departamentos_y_municipios():
    data = request.args
    print("Departamentos y municipio periodo",data.get('periodo',''))
    result = obtener_departamentos_y_municipios_colegios(int(data.get('periodo','')))
    return make_response(jsonify(result), 200)