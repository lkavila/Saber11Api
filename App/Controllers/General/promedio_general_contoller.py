from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analisis.promedios_y_desviaciones import promedio_nacional, desviacion_nacional, promedio_departamental, \
    desviacion_departamental, promedio_municipal, desviacion_municipal

promedioGeneralMunicipalDepartamental = Blueprint('promedio_general', __name__)

@promedioGeneralMunicipalDepartamental.route('/promedio-general')
def promedioGeneral():
    data = request.args
    periodo = int(data.get('periodo', ''))
    result = {
        f"promedio {periodo}": promedio_nacional (periodo),
        f"desviacion {periodo}": desviacion_nacional(periodo)
    }
    return make_response(jsonify(result), 200)


@promedioGeneralMunicipalDepartamental.route('/promedio-departamento')
def promedioDepartamento():
    data = request.args
    periodo=int(data.get('periodo', ''))
    result = {
        f"promedio {periodo}": promedio_departamental (periodo),
        f"desviacion {periodo}": desviacion_departamental(periodo)
    }
    return make_response(jsonify(result), 200)

@promedioGeneralMunicipalDepartamental.route('/promedio-municipal')
def promedioMunicipal():
    data = request.args
    periodo = int(data.get('periodo', ''))
    result ={
        f"promedio {periodo}": promedio_municipal(periodo),
        f"desviacion {periodo}": desviacion_municipal(periodo)
    }
    return make_response(jsonify(result), 200)