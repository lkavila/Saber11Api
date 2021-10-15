from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analysis.utils import mantener_columnas


def buscar_colegio(periodo):
    dataframe= get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_NOMBRE_ESTABLECIMIENTO']
    dataframe = mantener_columnas(dataframe, columnas_mantener)
    return dataframe.groupby(by='COLE_NOMBRE_ESTABLECIMIENTO').to_dict()


def buscar_colegio_departamento(periodo,departamento):
    return 1


def buscar_colegio_municipio(periodo,departamento,municipio):
    return 1