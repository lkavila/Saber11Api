from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analisis.datos_generales import obtener_departamentos_y_municipios_colegios,\
    total_registros_niveles_desempeno_por_calendario, probabilidad_puntaje
from App.Domain.General.cambiar_datasets import cambiar_datasets

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
    print(data)
    result = total_registros_niveles_desempeno_por_calendario(data.get('calendario'),
                                                              data.get('departamento'),
                                                              data.get('municipio'),
                                                              data.get('colegio'))
    return make_response(jsonify(result), 200)


@generalData.route('/datos-generales/probabilidad-puntaje')
def probabilidad_de_puntaje():
    data = request.args
    result = {
        "respuesta": probabilidad_puntaje(
            int(data.get('periodo', '')),
            data.get('puntaje', ''),
            int(data.get('limite_inf', '')),
            int(data.get('limite_sup', '')),
            data.get('departamento'),
            data.get('municipio'),
           )
    }
    return make_response(jsonify(result), 200)


@generalData.route('/datos-generales/cambiar-datasets')
def cambiar_datasets_endpoint():
    data = request.args
    booleano = data.get('depurar') == 'true'
    result = {
        "respuesta": cambiar_datasets(
            booleano,
           )
    }
    return make_response(jsonify(result), 200)
