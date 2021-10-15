from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analysis.busqueda_de_colegios import buscar_colegio, buscar_colegio_departamento, \
    buscar_colegio_municipio

buscarColegio = Blueprint('buscar_colegio', __name__)


@buscarColegio.route('/buscar-colegios')
def obtener_colegios():
    data = request.args
    result = {
        f"Colegios":buscar_colegio((int(data.get('periodo', ''))))
    }
    return make_response(jsonify(result), 200)


@buscarColegio.route('/buscar-colegios-dpto')
def obtener_colegios_depto():
    data = request.args
    result = {
        f"Colegios":buscar_colegio_departamento(int(data.get('periodo', '')),data.get('departamento', ''))
    }
    return make_response(jsonify(result), 200)


@buscarColegio.route('/buscar-colegios-mcpio')
def obtener_colegios_mcpio():
    data = request.args
    result = {
        f"Colegios":buscar_colegio_municipio(int(data.get('periodo', '')),data.get('departamento', ''),data.get('municipio', ''))
    }
    return make_response(jsonify(result), 200)