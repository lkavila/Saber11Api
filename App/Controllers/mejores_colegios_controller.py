from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analysis.mejores_colegios import mejores_colegios

mejoresColegios = Blueprint('mejores_colegios', __name__)

@mejoresColegios.route('/mejores-colegios')
def home():
    data = request.args
    print("Mejores colegios periodo",data.get('periodo',''))
    print(data)
    result = {
        f"mejoresColegios": mejores_colegios(int(data.get('periodo','')),
                                             data.get('departamento'),
                                             data.get('municipio'),
                                             ['PUNT_GLOBAL'],
                                             int(data.get('top','')),
                                             int(data.get('num_estudiantes','')))
        }
    return make_response(jsonify(result), 200)