import pandas as pd
from time import time
import threading
import numpy as np
from App.Infrastructure.Data.aws import subir_dataset_v2
import os


def run(file_name):
    start_time = time()
    req_cols = [
        'ESTU_GENERO',
        'ESTU_TIENEETNIA',
        'ESTU_DEPTO_RESIDE',
        'ESTU_MCPIO_RESIDE',
        'FAMI_ESTRATOVIVIENDA',
        'FAMI_PERSONASHOGAR',
        'FAMI_TIENEINTERNET',
        'FAMI_TIENESERVICIOTV',
        'FAMI_TIENECOMPUTADOR',
        'FAMI_TIENECONSOLAVIDEOJUEGOS',
        'FAMI_NUMLIBROS',
        'FAMI_SITUACIONECONOMICA',
        'FAMI_EDUCACIONPADRE',
        'FAMI_EDUCACIONMADRE',
        'ESTU_DEDICACIONLECTURADIARIA',
        'ESTU_DEDICACIONINTERNET',
        'ESTU_HORASSEMANATRABAJA',
        'COLE_NOMBRE_ESTABLECIMIENTO',
        'COLE_COD_DANE_ESTABLECIMIENTO',
        'COLE_CODIGO_ICFES',
        'COLE_NATURALEZA',
        'COLE_CALENDARIO',
        'COLE_BILINGUE',
        'COLE_CARACTER',
        'COLE_AREA_UBICACION',
        'COLE_MCPIO_UBICACION',
        'COLE_DEPTO_UBICACION',
        'PUNT_LECTURA_CRITICA',
        'PERCENTIL_LECTURA_CRITICA',
        'DESEMP_LECTURA_CRITICA',
        'PUNT_MATEMATICAS',
        'PERCENTIL_MATEMATICAS',
        'DESEMP_MATEMATICAS',
        'PUNT_C_NATURALES',
        'PERCENTIL_C_NATURALES',
        'DESEMP_C_NATURALES',
        'PUNT_SOCIALES_CIUDADANAS',
        'PERCENTIL_SOCIALES_CIUDADANAS',
        'DESEMP_SOCIALES_CIUDADANAS',
        'PUNT_INGLES',
        'PERCENTIL_INGLES',
        'DESEMP_INGLES',
        'PUNT_GLOBAL',
        'PERCENTIL_GLOBAL',
    ]
    data_type = {
        'PUNT_LECTURA_CRITICA': np.int8,
        'PERCENTIL_LECTURA_CRITICA': np.int8,
        'DESEMP_LECTURA_CRITICA': np.int8,
        'PUNT_MATEMATICAS': np.int8,
        'PERCENTIL_MATEMATICAS': np.int8,
        'DESEMP_MATEMATICAS': np.int8,
        'PUNT_C_NATURALES': np.int8,
        'PERCENTIL_C_NATURALES': np.int8,
        'DESEMP_C_NATURALES': np.int8,
        'PUNT_SOCIALES_CIUDADANAS': np.int8,
        'PERCENTIL_SOCIALES_CIUDADANAS': np.int8,
        'DESEMP_SOCIALES_CIUDADANAS': np.int8,
        'PUNT_INGLES': np.int8,
        'PERCENTIL_INGLES': np.int8,
        'DESEMP_INGLES': 'category',
        'PUNT_GLOBAL': np.int16,
        'PERCENTIL_GLOBAL': np.int8,
        'ESTU_GENERO': 'category',
        'ESTU_TIENEETNIA': 'category',
        'FAMI_ESTRATOVIVIENDA': 'category',
        'FAMI_PERSONASHOGAR': 'category',
        'FAMI_TIENEINTERNET': 'category',
        'FAMI_TIENESERVICIOTV': 'category',
        'FAMI_TIENECOMPUTADOR': 'category',
        'FAMI_TIENECONSOLAVIDEOJUEGOS': 'category',
        'FAMI_NUMLIBROS': 'category',
        'FAMI_SITUACIONECONOMICA': 'category',
        'FAMI_EDUCACIONPADRE': 'category',
        'FAMI_EDUCACIONMADRE': 'category',
        'ESTU_DEDICACIONLECTURADIARIA': 'category',
        'ESTU_DEDICACIONINTERNET': 'category',
        'ESTU_HORASSEMANATRABAJA': 'category',
        'COLE_NATURALEZA': 'category',
        'COLE_CALENDARIO': 'category',
        'COLE_BILINGUE': 'category',
        'COLE_CARACTER': 'category',
    }
    print("Se empezó a leer el xlsm...")
    path_data_xlsm = 'App/Infrastructure/Data/xlsm/'
    path_data_pickle = 'App/Infrastructure/Data/pickle/'
    data = pd.read_excel(path_data_xlsm + file_name + '.xlsm', usecols=req_cols)
    data = data.apply(lambda x: 'NA' if ((x.name == 'COLE_BILINGUE' or x.name == 'COLE_CARACTER') and x is None) else x)
    data = data.dropna()
    data = data.astype(dtype=data_type)
    print("Tiempo leyendo y limpiando el archivo xlsm: %0.10f seconds." % (time() - start_time))

    print(data.info())

    start_time = time()
    subir_dataset_v2(data, file_name + ".pkl")
    print("Tiempo subiendo dataset a bucket s3: %0.10f seconds." % (time() - start_time))

    #os.remove(path_data_xlsm + file_name + '.xlsm')
    # os.remove(path_data_pickle+file_name+".pickle")
    print("El hilo " + threading.current_thread().getName() + " ha terminado correctamente")
