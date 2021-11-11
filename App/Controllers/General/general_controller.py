from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analisis.datos_generales import obtener_departamentos_y_municipios_colegios, total_registros_niveles_desempeno_por_calendario

generalData = Blueprint('general_data', __name__)

@generalData.route('/datos-generales/departamentos-municipios-cole')
def obtener_departamentos_y_municipios():
    data = request.args
    print("Departamentos y municipio periodo",data.get('periodo',''))
    result = obtener_departamentos_y_municipios_colegios(int(data.get('periodo','')))
    return make_response(jsonify(result), 200)


@generalData.route('/datos-generales/promedios-desempenos')
def obtener_promedios_y_desempenos():
    data = request.args
    result = total_registros_niveles_desempeno_por_calendario((data.get('calendario','')))
    return make_response(jsonify(result), 200)