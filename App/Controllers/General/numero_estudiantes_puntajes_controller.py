from flask import Blueprint, request, jsonify, make_response
from App.Domain.Analisis.numero_estudiantes_puntaje import obtenerNumeroEstudiantesPorRangoPuntaje


numeroDeEsrudiantesPorRangoPuntaje = Blueprint('numero-estuddiantes-puntaje', __name__)


@numeroDeEsrudiantesPorRangoPuntaje.route('/numero-estudiantes-por-puntaje')
def numeroEstudiantesPuntaje():
    data = request.args
    respuesta = {"puntaje_estudiantes": obtenerNumeroEstudiantesPorRangoPuntaje(int(data.get('periodo', '')),
                                                                         data.get('puntaje'),
                                                                         data.get('departamento'),
                                                                         data.get('municipio'),
                                                                         data.get('colegio'))}
    return make_response(jsonify(respuesta), 200)
