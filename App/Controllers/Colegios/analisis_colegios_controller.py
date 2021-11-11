from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analisis.analisis_colegio import registros_colegio

analisisColegio = Blueprint('analisis_colegio', __name__)


@analisisColegio.route('/analisis-colegio/registros')
def registros_colegio():
    data = request.args
    result = {
        f"registros":registros_colegio(int(data.get('periodo', '')),
                                        data.get('departamento'),
                                        data.get('municipio'),
                                        data.get('colegio'),
                                        int(data.get('inicio', ''))
                                    )
    }
    return make_response(jsonify(result), 200)
