from App.Infrastructure.Repository.get_data import get_dataframe_for_year


def registros_colegio(periodo, departamento, municipio, colegio,  inicio):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]
    dataframe = dataframe[dataframe['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]
    return dataframe[inicio:(inicio+20)].to_dict()

