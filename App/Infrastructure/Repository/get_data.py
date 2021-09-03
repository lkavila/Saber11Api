from App.Infrastructure.Data.aws import ver_archivos_en_bucket, obtener_dataframe
from time import time
import pandas as pd


def get_dataframe(name):
    for df in datasets:
        if df['nombre'] == name:
            return df['dataframe']
    return False


datasets = []
archivos_en_bucket = ver_archivos_en_bucket()['Contents']


res = input("Desea leer los datasets locales o desde s3? 1: Si, 2: No.   ")
print("su respuesta es: ", res)
if res == "1":
    print("Leyendo datasets de bucket s3")
    start_time = time()
    try:
        for file in archivos_en_bucket:
            dataset = {'nombre': file['Key'], 'dataframe': obtener_dataframe(file['Key'])}
            datasets.append(dataset)

    except FileNotFoundError:
        print('File not found!!')

    except Exception:
        print('Another Error!!')

    dataframe_20191 = get_dataframe("SB11_20191.pkl")
    dataframe_20192 = get_dataframe("SB11_20192.pkl")
    dataframe_20201 = get_dataframe("SB11_20201.pkl")
    dataframe_20202 = get_dataframe("SB11_20202.pkl")
    dataframe_20211 = get_dataframe("SB11_20211.pkl")
    print("Tiempo leyendo datasets en bucket s3: %0.10f seconds." % (time() - start_time))
else:
    try:
        path_data = 'App/Infrastructure/Data/pickle/'
        dataframe_20191 = pd.read_pickle(path_data + "SB11_20191.pkl")
        dataframe_20192 = pd.read_pickle(path_data + "SB11_20192.pkl")
        dataframe_20201 = pd.read_pickle(path_data + "SB11_20201.pkl")
        dataframe_20202 = pd.read_pickle(path_data + "SB11_20202.pkl")
        dataframe_20211 = pd.read_pickle(path_data + "SB11_20211.pkl")

    except FileNotFoundError:
        print('File not found!!')

    except Exception:
        print('Another Error!!')





