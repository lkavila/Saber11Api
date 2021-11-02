from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analysis.utils import mantener_columnas


def buscar_colegio(periodo):
    dataframe= get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_NOMBRE_ESTABLECIMIENTO']
    dataframe = mantener_columnas(dataframe, columnas_mantener)
    dataframe = dataframe.groupby('COLE_NOMBRE_ESTABLECIMIENTO')
    return dataframe.apply(list).to_dict()

def buscar_colegio_departamento(periodo,departamento):
    dataframe = get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_NOMBRE_ESTABLECIMIENTO','COLE_DEPTO_UBICACION']
    dataframe = mantener_columnas(dataframe, columnas_mantener)
    dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION']== departamento.upper()]
    dataframe = dataframe.groupby(['COLE_NOMBRE_ESTABLECIMIENTO'])
    return dataframe.apply(list).to_dict()


def buscar_colegio_municipio(periodo,departamento,municipio):
    dataframe = get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_NOMBRE_ESTABLECIMIENTO', 'COLE_DEPTO_UBICACION', 'COLE_MCPIO_UBICACION']
    dataframe = mantener_columnas(dataframe, columnas_mantener)
    dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]
    dataframe = dataframe.groupby(['COLE_NOMBRE_ESTABLECIMIENTO'])
    return dataframe.apply(list).to_dict()