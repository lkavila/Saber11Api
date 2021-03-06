from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analisis.grafico_de_lineas import promedio_gen, variable_economica, desviacion_economica, \
    promediocolegio, promedioDepto, promediomunicipio

graficasLineas = Blueprint('graficas_lineas', __name__)

@graficasLineas.route('/graficas/linea-promedios')
def promedios():
    data = request.args
    result = promedio_gen(int(data.get('periodo','')),data.get('tpuntuacion'))
    return make_response(jsonify(result), 200)

@graficasLineas.route('/graficas/linea-desviaciones')
def desviaciones():
    data = request.args
    result = promedio_gen(int(data.get('periodo','')),data.get('tpuntuacion'))
    return make_response(jsonify(result), 200)

@graficasLineas.route('/graficas/linea-promedio-variablesocioeconomica')
def promedio_var_socioeconomico():
    data = request.args
    result=variable_economica(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('variablesocio'))
    return make_response(jsonify(result), 200)

@graficasLineas.route('/graficas/linea-desviacion-variablesocioeconomica')
def desviacion_var_socioeconomico():
    data = request.args
    result=desviacion_economica(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('variablesocio'))
    return make_response(jsonify(result), 200)
#-------------------------------------------------------------------------------------------------
@graficasLineas.route('/graficas/linea-promedios-colegios')
def promediosColegios():
    data = request.args
    result = promediocolegio(int(data.get('periodo',''))
                             ,data.get('departamento')
                             ,data.get('municipio')
                             ,data.get('colegio')
                             ,data.get('tpuntuacion'))
    return make_response(jsonify(result), 200)

@graficasLineas.route('/graficas/linea-promedios-departamento')
def promediosDepartamentos():
    data = request.args
    result = promedioDepto(int(data.get('periodo',''))
                             ,data.get('departamento')
                             ,data.get('tpuntuacion'))
    return make_response(jsonify(result), 200)

@graficasLineas.route('/graficas/linea-promedio-municipios')
def promediosMunicipio():
    data = request.args
    result = promediomunicipio(int(data.get('periodo',''))
                             ,data.get('departamento')
                             ,data.get('municipio')
                             ,data.get('tpuntuacion'))
    return make_response(jsonify(result), 200)