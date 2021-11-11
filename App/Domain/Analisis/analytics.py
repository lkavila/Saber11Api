from App.Infrastructure.Repository import get_data
from App.Domain.Analisis.utils import mantener_columnas, puntajes
from time import time


def obtener_puntajes_por_departamento(dataframe):
    start_time = time()

    columna_agrupar = 'ESTU_DEPTO_RESIDE'
    data_pkl = mantener_columnas(dataframe, puntajes)
    # dept = list(set(data_pkl["ESTU_DEPTO_RESIDE"].values))
    # dept.sort()

    print("Tiempo limpiando archivo: %0.10f seconds." % (time() - start_time))
    start_time = time()
    data_pkl2 = data_pkl.groupby(by=columna_agrupar).mean()
    print("Tiempo agrupando datos: %0.10f seconds." % (time() - start_time))

    return data_pkl2


def o_p_d_20191():
    df = get_data.dataframe_20191
    return obtener_puntajes_por_departamento(df)


def o_p_d_20192():
    df = get_data.dataframe_20192
    return obtener_puntajes_por_departamento(df)


def o_p_d_20201():
    df = get_data.dataframe_20201
    return obtener_puntajes_por_departamento(df)


def o_p_d_20202():
    df = get_data.dataframe_20202
    return obtener_puntajes_por_departamento(df)


def o_p_d_20211():
    df = get_data.dataframe_20211
    return obtener_puntajes_por_departamento(df)
