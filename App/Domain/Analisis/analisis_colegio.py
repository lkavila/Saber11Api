from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analisis.utils import mantener_columnas


def registros_colegio(periodo, departamento, municipio, colegio,  inicio):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]
    dataframe = dataframe[dataframe['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]
    return dataframe[inicio:20].to_dict()
