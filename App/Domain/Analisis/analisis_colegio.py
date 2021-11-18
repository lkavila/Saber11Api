from App.Infrastructure.Repository.get_data import get_dataframe_for_year


def registros_colegio(periodo, departamento, municipio, colegio,  inicio):
    dataframe = get_dataframe_for_year(periodo)
    dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]
    dataframe = dataframe[dataframe['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]
    dataframe = dataframe.drop(columns=['COLE_DEPTO_UBICACION', 'COLE_MCPIO_UBICACION', 'COLE_NOMBRE_ESTABLECIMIENTO'])
    dataframe = dataframe.astype('object')
    dataframe = dataframe[inicio:(inicio + 20)]
    resultado = []
    for i in dataframe.index:
        estudiante = {}
        for variable in dataframe.columns:
            estudiante[variable] = dataframe[variable][i]
        resultado.append(estudiante)
    return resultado

