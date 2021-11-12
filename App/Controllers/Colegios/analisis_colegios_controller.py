from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analisis.analisis_colegio import registros_colegio
from App.Domain.Analisis.datos_generales import total_registros_niveles_desempeno_por_periodo, probabilidad_puntaje

analisisColegio = Blueprint('analisis_colegio', __name__)


@analisisColegio.route('/analisis-colegio/registros')
def registros_por_colegio():
    data = request.args
    result = {
        "respuesta": registros_colegio(
            int(data.get('periodo', '')),
            data.get('departamento'),
            data.get('municipio'),
            data.get('colegio'),
            int(data.get('inicio', '')),
        )
    }
    return make_response(jsonify(result), 200)


@analisisColegio.route('/analisis-colegio/desempeno')
def desempeno_colegio():
    data = request.args
    result = {
        "respuesta": total_registros_niveles_desempeno_por_periodo(
            int(data.get('periodo', '')),
            data.get('departamento'),
            data.get('municipio'),
            data.get('colegio'),
           )
    }
    return make_response(jsonify(result), 200)


@analisisColegio.route('/analisis-colegio/probabilidad-puntaje')
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
            data.get('colegio'),
           )
    }
    return make_response(jsonify(result), 200)