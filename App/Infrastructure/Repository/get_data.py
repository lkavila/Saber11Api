from App.Infrastructure.Data.aws import ver_archivos_SB11_en_bucket, obtener_dataframe, \
    obtener_modelo, obtener_modelos_desde_s3, prefix_depurados, prefix_no_depurados
from App.Infrastructure.Repository.choose_datasets import ChooseDatasets
from time import time
import pandas as pd
import os


def get_dataframe(tipo_dataset, periodo):
    for df in datasets:
        if (df['tipo_dataset'] == tipo_dataset) & (df['periodo'] == str(periodo)):
            return df['dataframe']
    return False


def get_dataframes_from_s3(prefix):
    try:
        archivos_en_bucket = ver_archivos_SB11_en_bucket(prefix)['Contents']
        long = len(prefix)
        print(archivos_en_bucket)
        for file in archivos_en_bucket:
            print(file)
            print(file['Key'])
            print(file['Key'][long+6:long+6+5])
            dataset = {'tipo_dataset': prefix, 'periodo': file['Key'][long+6:long+6+5], 'dataframe': obtener_dataframe(file['Key'])}
            datasets.append(dataset)

    except FileNotFoundError:
        print('File not found!!')


def get_dataframes_from_local(path, prefix):
    try:
        for file in os.listdir(path):
            if file[:5] == 'SB11_':
                dataset = {'tipo_dataset': prefix, 'periodo': file[5:10], 'dataframe': pd.read_pickle(path+'/'+file)}
                datasets.append(dataset)

    except FileNotFoundError:
        print('File not found!!')


def get_dataframe_for_year(year):
    if tipos_datasets.es_tipo_depurado():
        return get_dataframe(prefix_depurados, year)
    else:
        return get_dataframe(prefix_no_depurados, year)


def change_datasets_type(es_depurados):
    tipos_datasets.cambiar_datasets(es_depurados)
    return f'Tipo de datasets cambiado correctamente; usar datasets depurados: {es_depurados} '


def get_classification_model(calendario):
    return obtener_modelo(calendario)


datasets = []
tipos_datasets = ChooseDatasets()

res = input("Desea descargar los modelos de clasificación desde el s3? 1: Si, otro: Leer datos locales:     ")
if res == "1":
    obtener_modelos_desde_s3()

res = input("Desea leer los datasets desde s3 (tomará alrededor de 4 minutos)? 1: Si, otro: Leer datos locales:   ")
if res == "1":
    print("Leyendo datasets de bucket s3")
    start_time = time()
    get_dataframes_from_s3(prefix_depurados)
    get_dataframes_from_s3(prefix_no_depurados)
    print("Tiempo leyendo datasets en bucket s3: %0.10f seconds." % (time() - start_time))
else:
    path_data = 'App/Infrastructure/Data/pickle/' + prefix_no_depurados
    get_dataframes_from_local(path_data, prefix_no_depurados)
    path_data = 'App/Infrastructure/Data/pickle/' + prefix_depurados
    get_dataframes_from_local(path_data, prefix_depurados)
