from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analysis.busqueda_de_colegios import buscar_colegio

buscarColegio = Blueprint('buscar_colegio', __name__)


@buscarColegio.route('/buscar-colegios')
def obtener_colegios():
    data = request.args
    result = {
        f"Colegios":buscar_colegio(int(data.get('periodo', '')),data.get('departamento', ''),data.get('municipio', ''))
    }
    return make_response(jsonify(result), 200)