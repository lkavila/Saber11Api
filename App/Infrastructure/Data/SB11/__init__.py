import pandas as pd
from time import time
import threading

def run(file_name):
    start_time = time()
    req_cols = ['ESTU_GENERO',
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
'ESTU_PRIVADO_LIBERTAD',
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
    data_type={
        'PUNT_LECTURA_CRITICA': 'int8',
'PERCENTIL_LECTURA_CRITICA':'int8',
'DESEMP_LECTURA_CRITICA':'int8',
'PUNT_MATEMATICAS':'int8',
'PERCENTIL_MATEMATICAS':'int8',
'DESEMP_MATEMATICAS':'int8',
'PUNT_C_NATURALES':'int8',
'PERCENTIL_C_NATURALES':'int8',
'DESEMP_C_NATURALES':'int8',
'PUNT_SOCIALES_CIUDADANAS':'int8',
'PERCENTIL_SOCIALES_CIUDADANAS':'int8',
'DESEMP_SOCIALES_CIUDADANAS':'int8',
'PUNT_INGLES':'int8',
'PERCENTIL_INGLES':'int8',
'DESEMP_INGLES':'category',
'PUNT_GLOBAL':'int16',
'PERCENTIL_GLOBAL':'int8',
                  'ESTU_GENERO':'category',
                  'ESTU_TIENEETNIA':'category',
              'FAMI_ESTRATOVIVIENDA':'category',
              'FAMI_PERSONASHOGAR':'category',
              'FAMI_TIENEINTERNET':'category',
              'FAMI_TIENESERVICIOTV':'category',
              'FAMI_TIENECOMPUTADOR':'category',
              'FAMI_TIENECONSOLAVIDEOJUEGOS':'category',
              'FAMI_NUMLIBROS':'category',
              'FAMI_SITUACIONECONOMICA':'category',
              'FAMI_EDUCACIONPADRE':'category',
              'FAMI_EDUCACIONMADRE':'category',
              'ESTU_DEDICACIONLECTURADIARIA':'category',
              'ESTU_DEDICACIONINTERNET':'category',
              'ESTU_HORASSEMANATRABAJA':'category',
              'COLE_NATURALEZA':'category',
              'COLE_CALENDARIO':'category',
              'COLE_BILINGUE':'category',
              'COLE_CARACTER':'category',
              'ESTU_PRIVADO_LIBERTAD':'category',
    }
    print("Se empezó a leer el xlsm...")
    datacsv = pd.read_excel('App/Infrastructure/Data/xlsm/'+file_name+'.xlsm', usecols=req_cols)

    print("Tiempo leyendo el archivo xlsm: %0.10f seconds." % (time() - start_time))

    start_time = time()
    datacsv.to_pickle("App/Infrastructure/Data/pkl/"+file_name+".pkl")
    print("Tiempo guardando el archivo pkl: %0.10f seconds." % (time() - start_time))

    start_time = time()
    data_pkl = pd.read_pickle("App/Infrastructure/Data/pkl/"+file_name+".pkl")
    print("Tiempo leyendo el archivo pkl: %0.10f seconds." % (time() - start_time))
    print("El archivo " + threading.current_thread().getName() + " se ha convertido a pkl correctamente")
"""
    start_time = time()
    columnas = data_pkl.columns.values
    puntajes = ["ESTU_DEPTO_RESIDE", "PUNT_LECTURA_CRITICA", "PUNT_MATEMATICAS", "PUNT_C_NATURALES",
                "PUNT_SOCIALES_CIUDADANAS", "PUNT_INGLES", "PUNT_GLOBAL"]
    columna_agrupar = 'ESTU_DEPTO_RESIDE'
    eliminar = []
    for x in columnas:
        if x not in puntajes:
            eliminar.append(x)
    data_pkl = data_pkl.drop(columns=eliminar)
    data_pkl = data_pkl.dropna()
    dept = list(set(data_pkl["ESTU_DEPTO_RESIDE"].values))
    dept.sort()

    print("Tiempo limpiando archivo: %0.10f seconds." % (time() - start_time))
    start_time = time()
    data_pkl2 = data_pkl.groupby(by=columna_agrupar).mean()
    print("Tiempo agrupando datos: %0.10f seconds." % (time() - start_time))
"""
