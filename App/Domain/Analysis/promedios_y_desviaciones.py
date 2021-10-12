from App.Domain.Analysis.utils import mantener_columnas
from App.Infrastructure.Repository.get_data import get_dataframe, get_dataframe_for_year


def promedio_nacional (periodo):
    dataframe= get_dataframe_for_year(periodo)
    columnas_mantener = ['PUNT_LECTURA_CRITICA','PUNT_MATEMATICAS','PUNT_C_NATURALES',
        'PUNT_SOCIALES_CIUDADANAS','PUNT_INGLES','PUNT_GLOBAL',]
    dataframe = mantener_columnas(dataframe, columnas_mantener)

    return dataframe.mean().to_json()

def promedio_departamental(periodo):
    dataframe = get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_DEPTO_UBICACION','PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS', 'PUNT_C_NATURALES',
                         'PUNT_SOCIALES_CIUDADANAS', 'PUNT_INGLES', 'PUNT_GLOBAL', ]
    dataframe = mantener_columnas(dataframe, columnas_mantener)

    return dataframe.groupby(by='COLE_DEPTO_UBICACION').mean().to_json()
def desviacion_nacional(periodo):
    dataframe = get_dataframe_for_year(periodo)
    columnas_mantener = ['PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS', 'PUNT_C_NATURALES',
                         'PUNT_SOCIALES_CIUDADANAS', 'PUNT_INGLES', 'PUNT_GLOBAL', ]
    dataframe = mantener_columnas(dataframe, columnas_mantener)

    return dataframe.std().to_json()

def desviacion_departamental(periodo):
    dataframe = get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_DEPTO_UBICACION','PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS', 'PUNT_C_NATURALES',
                         'PUNT_SOCIALES_CIUDADANAS', 'PUNT_INGLES', 'PUNT_GLOBAL', ]
    dataframe = mantener_columnas(dataframe, columnas_mantener)

    return dataframe.groupby(by='COLE_DEPTO_UBICACION').std().to_json()

def desviacion_municipal(periodo):
    dataframe = get_dataframe_for_year(periodo)
    columnas_mantener = ['COLE_DEPTO_UBICACION', 'PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS', 'PUNT_C_NATURALES',
                         'PUNT_SOCIALES_CIUDADANAS', 'PUNT_INGLES', 'PUNT_GLOBAL', ]
    dataframe = mantener_columnas(dataframe, columnas_mantener)

    return dataframe.groupby(['COLE_MCPIO_UBICACION','COLE_DEPTO_UBICACION']).std().to_json()