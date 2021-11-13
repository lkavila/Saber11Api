from flask import Blueprint, request, jsonify, make_response

from App.Domain.Analisis.diagrama_histograma import distribucionDeDatos, distribucionacumulada

graficasHistograma = Blueprint('graficas_histograma', __name__)


@graficasHistograma.route("/graficas/histograma-de-resultados")
def histograma():
    data = request.args
    result = distribucionDeDatos(int(data.get('periodo','')),data.get('tpuntuacion'),None,None,None)
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-departamento")
def histogramadep():
    data = request.args
    result = distribucionDeDatos(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento'),None,None)
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-municipio")
def histogramamun():
    data = request.args
    result = distribucionDeDatos(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento')
                                 ,data.get('municipio'),None)
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-colegio")
def histogramacol():
    data = request.args
    result = distribucionDeDatos(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento')
                                 ,data.get('municipio'),data.get('colegio'))
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-acumulados")
def histogramaacumulado():
    data = request.args
    result = distribucionacumulada(int(data.get('periodo','')),data.get('tpuntuacion'),None,None,None)
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-departamento-acumulados")
def histogramadepacumulado():
    data = request.args
    result = distribucionacumulada(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento'),None,None)
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-municipio-acumulados")
def histogramamunacumulado():
    data = request.args
    result = distribucionacumulada(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento')
                                 ,data.get('municipio'),None)
    return make_response(jsonify(result), 200)

@graficasHistograma.route("/graficas/histograma-de-resultados-colegio-acumulados")
def histogramacolacumulado():
    data = request.args
    result = distribucionacumulada(int(data.get('periodo','')),data.get('tpuntuacion'),data.get('departamento')
                                 ,data.get('municipio'),data.get('colegio'))
    return make_response(jsonify(result), 200)