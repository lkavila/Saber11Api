from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analisis.utils import mantener_columnas, periodos, puntajes, desempenos
import numpy
from scipy.stats import norm

def obtener_departamentos_y_municipios_colegios(periodo):
    dataframe = get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_DEPTO_UBICACION', 'COLE_MCPIO_UBICACION']
    dataframe = mantener_columnas(dataframe, columnas_mantener)
    dataframe['Result'] = dataframe.set_index('COLE_DEPTO_UBICACION').values.tolist()
    dataframe = dataframe.groupby('COLE_DEPTO_UBICACION')['Result'].apply(list)
    diccionario = dataframe.to_dict()
    departamentos = []
    for key in diccionario:
        lista_municipios = []
        for municipios in diccionario[key]:
            lista_municipios.append(municipios[0])
        departamentos.append({"ciudades": list(set(lista_municipios)), "departamento": key})
    return departamentos


def total_registros_niveles_desempeno_por_periodo(periodo, departamento=None, municipio=None, colegio=None):
    dataframe = get_dataframe_for_year(periodo)
    columnas_a_mantener = puntajes + desempenos
    if departamento is not None:
        columnas_a_mantener.append('COLE_DEPTO_UBICACION')
    if municipio is not None:
        columnas_a_mantener.append('COLE_MCPIO_UBICACION')
    if colegio is not None:
        columnas_a_mantener.append('COLE_NOMBRE_ESTABLECIMIENTO')
    dataframe = mantener_columnas(dataframe, columnas_a_mantener)
    if departamento is not None:
        dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    if municipio is not None:
        dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]
    if colegio is not None:
        dataframe = dataframe[dataframe['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]
    total_estudiantes = dataframe.shape[0]
    resultado = {}
    datos_periodo = {'Total_estudiantes': total_estudiantes}

    for puntaje in puntajes:
        datos_periodo['Promedio '+puntaje] = round(numpy.mean(dataframe[puntaje].values), 2)

    for desempeno in desempenos:
        datos_periodo['Porcentaje '+desempeno] = dataframe[desempeno].value_counts()\
            .apply(lambda x: round((x/total_estudiantes)*100), 1).to_dict()

    resultado[f'Periodo {periodo}'] = datos_periodo

    return resultado


def total_registros_niveles_desempeno_por_calendario(calendario):
    resultado = []
    for periodo in periodos:
        if (calendario == "A") & (periodo % 2 == 0):
            resultado.append(total_registros_niveles_desempeno_por_periodo(periodo))
        if (calendario == "B") & (periodo % 2 != 0):
            resultado.append(total_registros_niveles_desempeno_por_periodo(periodo))
    return resultado


def probabilidad_puntaje(periodo, puntaje, limite_inf, limite_sup, departamento=None, municipio=None, colegio=None):
    dataframe = get_dataframe_for_year(periodo)
    columnas_a_mantener = puntajes + desempenos
    if departamento is not None:
        columnas_a_mantener.append('COLE_DEPTO_UBICACION')
    if municipio is not None:
        columnas_a_mantener.append('COLE_MCPIO_UBICACION')
    if colegio is not None:
        columnas_a_mantener.append('COLE_NOMBRE_ESTABLECIMIENTO')
    dataframe = mantener_columnas(dataframe, columnas_a_mantener)
    if departamento is not None:
        dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    if municipio is not None:
        dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]
    if colegio is not None:
        dataframe = dataframe[dataframe['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]

    promedio = numpy.mean(dataframe[puntaje].values)
    desviacion_estandar = numpy.std(dataframe[puntaje].values)

    cdf_upper_limit = norm(loc=promedio, scale=desviacion_estandar).cdf(limite_sup)
    cdf_lower_limit = norm(loc=promedio, scale=desviacion_estandar).cdf(limite_inf)
    probabilidad = (round(cdf_upper_limit - cdf_lower_limit, 3))*100
    resultado = f'La probabilidad de que un estudiante obtenga un puntaje en el rango {limite_inf}-{limite_sup} ' \
                f'con las condiciones dadas es: {probabilidad}%'

    return resultado
