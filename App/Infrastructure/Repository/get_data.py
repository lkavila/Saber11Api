from App.Infrastructure.Data.aws import ver_archivos_SB11_en_bucket, obtener_dataframe, obtener_modelo
from time import time
import pandas as pd


def get_dataframe(name):
    for df in datasets:
        if df['nombre'] == name:
            return df['dataframe']
    return False


datasets = []
archivos_en_bucket = ver_archivos_SB11_en_bucket()['Contents']


res = input("Desea leer los datasets locales o desde s3? 1: Leer datos locales, 2: Leer datos desde S3.   ")
#res = "1"
print("su respuesta es: ", res)
if res == "2":
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

    dataframe_20171 = get_dataframe("SB11_20171.pkl")
    dataframe_20172 = get_dataframe("SB11_20172.pkl")
    dataframe_20181 = get_dataframe("SB11_20181.pkl")
    dataframe_20182 = get_dataframe("SB11_20182.pkl")
    dataframe_20191 = get_dataframe("SB11_20191.pkl")
    dataframe_20192 = get_dataframe("SB11_20192.pkl")
    dataframe_20201 = get_dataframe("SB11_20201.pkl")
    dataframe_20202 = get_dataframe("SB11_20202.pkl")
    dataframe_20211 = get_dataframe("SB11_20211.pkl")
    print("Tiempo leyendo datasets en bucket s3: %0.10f seconds." % (time() - start_time))
else:
    try:
        path_data = 'App/Infrastructure/Data/pickle/'
        dataframe_20171 = pd.read_pickle(path_data + "SB11_20171.pkl")
        dataframe_20172 = pd.read_pickle(path_data + "SB11_20172.pkl")
        dataframe_20181 = pd.read_pickle(path_data + "SB11_20181.pkl")
        dataframe_20182 = pd.read_pickle(path_data + "SB11_20182.pkl")
        dataframe_20191 = pd.read_pickle(path_data + "SB11_20191.pkl")
        dataframe_20192 = pd.read_pickle(path_data + "SB11_20192.pkl")
        dataframe_20201 = pd.read_pickle(path_data + "SB11_20201.pkl")
        dataframe_20202 = pd.read_pickle(path_data + "SB11_20202.pkl")
        dataframe_20211 = pd.read_pickle(path_data + "SB11_20211.pkl")

    except FileNotFoundError:
        print('File not found!!')

    except Exception:
        print('Another Error!!')


def get_dataframe_for_year(year):
    if year == 20171:
        return dataframe_20171
    elif year == 20172:
        return dataframe_20172
    elif year == 20181:
        return dataframe_20181
    elif year == 20182:
        return dataframe_20182
    elif year == 20191:
        return dataframe_20191
    elif year == 20192:
        return dataframe_20192
    elif year == 20201:
        return dataframe_20201
    elif year == 20202:
        return  dataframe_20202
    elif year == 20211:
        return dataframe_20211
    else:
        return None


def get_classification_model(calendario):
    return obtener_modelo(calendario)



