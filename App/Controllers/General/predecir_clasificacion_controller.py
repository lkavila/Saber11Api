from flask import Blueprint, request, jsonify, make_response
from App.Domain.PredecirClasificacion import predecir

predecirClasificacion = Blueprint('predecir_clasificacion', __name__)


@predecirClasificacion.route('/predecir-clasificacion', methods=['POST'])
def home():
    data = request.get_json()
    if data['calendario'] == "A":
        presicion = "70%"
    else:
        presicion = "73%"

    result = {
        "prediccion":
        f"Con las variables socieconomicas dadas y según el analices hecho con los datos depurados "
        f"de los resultados obtenidos en el último exámen calendario {data.get('calendario')} y con una "
        f"presición del {presicion}, lo hemos clasificado como: {predecir(data['variables'], data['calendario'])}"
        }
    return make_response(jsonify(result), 200)
