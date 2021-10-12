from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analysis.utils import mantener_columnas


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
