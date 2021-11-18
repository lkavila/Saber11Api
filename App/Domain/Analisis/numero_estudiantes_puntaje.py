from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analisis.utils import mantener_columnas


def obtenerNumeroEstudiantesPorRangoPuntaje(periodo, puntaje, departamento, municipio, colegio):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe, ['COLE_NOMBRE_ESTABLECIMIENTO', 'COLE_DEPTO_UBICACION', 'COLE_MCPIO_UBICACION', puntaje])
    if departamento is not None:
        dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    if municipio is not None:
        dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]
    if colegio is not None:
        dataframe = dataframe[dataframe['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]

    aproximar = 2
    if puntaje == "PUNT_GLOBAL":
        aproximar = 10
    dataframe[puntaje] = dataframe[puntaje].apply(lambda x: round(x/aproximar)*aproximar)
    return dataframe[puntaje].value_counts().to_dict()


