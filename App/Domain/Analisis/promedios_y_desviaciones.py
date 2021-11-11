from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analisis.utils import mantener_columnas, puntajes


def promedio_nacional (periodo):
    dataframe= get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe, puntajes)
    return dataframe.mean().to_dict()


def promedio_departamental(periodo):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe, puntajes.append('COLE_DEPTO_UBICACION'))
    return dataframe.groupby(by='COLE_DEPTO_UBICACION').mean().to_dict()

def promedio_municipal(periodo):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe, puntajes.append('COLE_MCPIO_UBICACION'))
    return dataframe.groupby(by='COLE_MCPIO_UBICACION').mean().to_dict()


def desviacion_nacional(periodo):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe, puntajes)
    return dataframe.std(ddof=0).to_dict()


def desviacion_departamental(periodo):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe, puntajes.append('COLE_DEPTO_UBICACION'))
    return dataframe.groupby(by='COLE_DEPTO_UBICACION').std(ddof=0).to_dict()


def desviacion_municipal(periodo):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe, puntajes.append('COLE_MCPIO_UBICACION'))
    return dataframe.groupby(by='COLE_MCPIO_UBICACION').std(ddof=0).to_dict()


