import pandas as pd
from time import time
import threading
import numpy as np
from App.Infrastructure.Data.aws import subir_dataset_v2
import os

fecha_presentacion_examen = pd.Timestamp('2019-03-10T12')
"""
Fechas de presentación
SB11_20211: 21 de marzo del 2021
SB11_20202: domingo 9 de agosto de 2020
SB11_20201: sábado 24 de octubre de 2020
SB11_20192: 11 de agosto del 2019
SB11_20191: 10 de marzo del 2019 
SB11_20182: 12 de agosto del 2018
SB11_20181: 25 de febrero del 2018
SB11_20172: 27 de agosto del 2017
SB11_20171: 12 de marzo del 2017
"""


def definir_fecha(file_name):
    if file_name == 'SB11_20211':
        return pd.Timestamp('2021-03-21T12')  # No tiene ESTU_NSE_INDIVIDUAL ni ESTU_NSE_ESTABLECIMIENTO

    elif file_name == 'SB11_20202':
        return pd.Timestamp('2020-08-9T12')

    elif file_name == 'SB11_20201':
        return pd.Timestamp('2020-10-24T12')  # No tiene ESTU_NSE_INDIVIDUAL ni ESTU_NSE_ESTABLECIMIENTO

    elif file_name == 'SB11_20192':
        return pd.Timestamp('2019-08-11T12')

    elif file_name == 'SB11_20191':
        return pd.Timestamp('2019-03-10T12')

    elif file_name == 'SB11_20182':
        return pd.Timestamp('2018-08-12T12')  # INS_ESTU es texto

    elif file_name == 'SB11_20181':
        return pd.Timestamp('2018-02-25T12')  # INS_ESTU es texto

    elif file_name == 'SB11_20172':
        return pd.Timestamp('2017-08-27T12')  # INS_ESTU es texto

    elif file_name == 'SB11_20171':
        return pd.Timestamp('2017-03-12T12')  # INS_ESTU es texto

    else:
        return pd.Timestamp('2019-08-11T12')

def calcular_edad(fecha_nacimiento):
    if isinstance(fecha_nacimiento, str):
        print(fecha_nacimiento)
        return 16.5
    else:
        edad = (fecha_presentacion_examen-fecha_nacimiento).days /365.2425
        if edad <=12:
            return 16.5
        elif edad >= 116.5:
            return (edad-100)
        else:
            return edad

def transformar_NSE(nse):
    if isinstance(nse, str):
        if nse == 'NSE1':
            return 1
        elif nse == 'NSE2':
            return 2
        elif nse == 'NSE3':
            return 3
        elif nse == 'NSE4':
            return 4
        else:
            return None
    else:
        return nse


def run(file_name):
    fecha_presentacion_examen = definir_fecha(file_name)
    print("Fecha de prensentación del examen: ", fecha_presentacion_examen)
    start_time = time()
    req_cols = [
        'ESTU_GENERO',
        'ESTU_FECHANACIMIENTO',
        'ESTU_TIENEETNIA',
        'ESTU_DEPTO_RESIDE',
        'ESTU_MCPIO_RESIDE',
        'FAMI_ESTRATOVIVIENDA',
        'FAMI_CUARTOSHOGAR',
        'FAMI_PERSONASHOGAR',
        'FAMI_TIENEINTERNET',
        'FAMI_TIENESERVICIOTV',
        'FAMI_TIENECOMPUTADOR',
        'FAMI_TIENECONSOLAVIDEOJUEGOS',
        'FAMI_TIENEAUTOMOVIL',
        'FAMI_NUMLIBROS',
        'FAMI_SITUACIONECONOMICA',
        'FAMI_EDUCACIONPADRE',
        'FAMI_EDUCACIONMADRE',
        'FAMI_COMECARNEPESCADOHUEVO',
        'ESTU_DEDICACIONLECTURADIARIA',
        'ESTU_DEDICACIONINTERNET',
        'ESTU_HORASSEMANATRABAJA',
        'COLE_NOMBRE_ESTABLECIMIENTO',
        'COLE_NATURALEZA',
        'COLE_CALENDARIO',
        'COLE_BILINGUE',
        'COLE_CARACTER',
        'COLE_JORNADA',
        'COLE_CALENDARIO',
        'COLE_AREA_UBICACION',
        'COLE_MCPIO_UBICACION',
        'COLE_DEPTO_UBICACION',
        'PUNT_LECTURA_CRITICA',
        'DESEMP_LECTURA_CRITICA',
        'PUNT_MATEMATICAS',
        'DESEMP_MATEMATICAS',
        'PUNT_C_NATURALES',
        'DESEMP_C_NATURALES',
        'PUNT_SOCIALES_CIUDADANAS',
        'DESEMP_SOCIALES_CIUDADANAS',
        'PUNT_INGLES',
        'DESEMP_INGLES',
        'PUNT_GLOBAL',
        'PERCENTIL_GLOBAL',
    ]

    data_type = {
        'PUNT_LECTURA_CRITICA': np.int8,
        'DESEMP_LECTURA_CRITICA': np.int8,
        'PUNT_MATEMATICAS': np.int8,
        'DESEMP_MATEMATICAS': np.int8,
        'PUNT_C_NATURALES': np.int8,
        'DESEMP_C_NATURALES': np.int8,
        'PUNT_SOCIALES_CIUDADANAS': np.int8,
        'DESEMP_SOCIALES_CIUDADANAS': np.int8,
        'PUNT_INGLES': np.int8,
        'DESEMP_INGLES': 'category',
        'PUNT_GLOBAL': np.int16,
        'PERCENTIL_GLOBAL': np.int8,
        'ESTU_EDAD': np.float32,
        'ESTU_GENERO': 'category',
        'ESTU_TIENEETNIA': 'category',
        'FAMI_ESTRATOVIVIENDA': np.int8,
        'FAMI_PERSONASHOGAR': 'category',
        'FAMI_TIENEINTERNET': 'category',
        'FAMI_TIENESERVICIOTV': 'category',
        'FAMI_TIENECOMPUTADOR': 'category',
        'FAMI_TIENECONSOLAVIDEOJUEGOS': 'category',
        'FAMI_TIENEAUTOMOVIL': 'category',
        'FAMI_NUMLIBROS': 'category',
        'FAMI_SITUACIONECONOMICA': 'category',
        'FAMI_EDUCACIONPADRE': 'category',
        'FAMI_EDUCACIONMADRE': 'category',
        'FAMI_CUARTOSHOGAR': 'category',
        'FAMI_COMECARNEPESCADOHUEVO': 'category',
        'ESTU_DEDICACIONLECTURADIARIA': 'category',
        'ESTU_DEDICACIONINTERNET': 'category',
        'ESTU_HORASSEMANATRABAJA': 'category',
        'COLE_NATURALEZA': 'category',
        'COLE_CALENDARIO': 'category',
        'COLE_BILINGUE': 'category',
        'COLE_CARACTER': 'category',
        'COLE_JORNADA': 'category',
        'COLE_CALENDARIO': 'category',
        'COLE_AREA_UBICACION': 'category',
    }

    estrato_familia_numero = {

        "FAMI_ESTRATOVIVIENDA": {"Estrato 6": 6, "Estrato 5": 5, "Estrato 4": 4, "Estrato 3": 3,
                                 "Estrato 2": 2, "Estrato 1": 1, "Sin Estrato": 0},
        "FAMI_CUARTOSHOGAR": {"Uno": 1, "Dos": 2, "Tres": 3, "Cuatro": 4, "Cinco": 5, "Seis o mas": 6},
    }

    if file_name != 'SB11_20211' and file_name != 'SB11_20201':
        req_cols.append('ESTU_NSE_INDIVIDUAL')
        req_cols.append('ESTU_NSE_ESTABLECIMIENTO')


    print("Se empezó a leer el xlsm...")
    path_data_xlsm = 'App/Infrastructure/Data/xlsm/'
    path_data_pickle = 'App/Infrastructure/Data/pickle/'

    data = pd.read_excel(path_data_xlsm + file_name + '.xlsm', usecols=req_cols)
    print("Tiempo leyendo el archivo xlsm: %0.10f seconds." % (time() - start_time))
    print(data.info())
    start_time = time()

    if file_name != 'SB11_20211' and file_name != 'SB11_20201':
        data['ESTU_NSE_INDIVIDUAL'] = data['ESTU_NSE_INDIVIDUAL'].apply(transformar_NSE)
        data = data[data['ESTU_NSE_INDIVIDUAL'].notna()]
        data = data.astype(dtype={'ESTU_NSE_INDIVIDUAL': np.int8, 'ESTU_NSE_ESTABLECIMIENTO': np.int8})

    data = data.apply(lambda x: 'NA' if ((x.name == 'COLE_BILINGUE' or x.name == 'COLE_CARACTER') and x is None) else x)

    data = data.dropna()

    data['ESTU_EDAD'] = data['ESTU_FECHANACIMIENTO'].apply(calcular_edad)
    data = data.drop(columns=['ESTU_FECHANACIMIENTO'])
    data = data[(data['ESTU_EDAD'] >= 13) | (data['ESTU_EDAD'] <= 90)]  # Eliminar edades absurdas

    data = data.replace(estrato_familia_numero)
    data = data.astype(dtype=data_type)
    print("Tiempo limpiando el archivo xlsm: %0.10f seconds." % (time() - start_time))

    print(data.info())

    start_time = time()
    subir_dataset_v2(data, file_name + ".pkl")
    print("Tiempo subiendo dataset a bucket s3: %0.10f seconds." % (time() - start_time))

    os.remove(path_data_xlsm + file_name + '.xlsm')
    # os.remove(path_data_pickle+file_name+".pickle")
    print("El hilo " + threading.current_thread().getName() + " ha terminado correctamente")
