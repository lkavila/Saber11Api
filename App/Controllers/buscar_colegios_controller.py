from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analysis.busqueda_de_colegios import buscar_colegio

buscarColegio = Blueprint('buscar_colegio', __name__)


@buscarColegio.route('/buscar-colegios')
def obtener_colegios():
    data = request.args
    result = buscar_colegio((int(data.get('periodo', ''))))
    return make_response(jsonify(result), 200)


@buscarColegio.route('/buscar-colegios-dpto')
def obtener_colegios_depto():
    data = request.args
    result = (int(data.get('periodo', '')))
    return make_response(jsonify(result), 200)


@buscarColegio.route('/buscar-colegios-mcpio')
def obtener_colegios_mcpio():
    data = request.args
    result = (int(data.get('periodo', '')))
    return make_response(jsonify(result), 200)