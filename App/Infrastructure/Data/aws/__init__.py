import boto3
import pandas as pd
import joblib
import os

bucket_name = 'saber11-datasets'
bucket_model_name = "modelos-saber-11"
s3_client = boto3.client('s3')


def subir_dataset(path, name):
    s3_client.upload_file(path+"/"+name, bucket_name, name)


def subir_dataset_v2(dataframe, name):
    dataframe.to_pickle(f"s3://{bucket_name}/{name}")


def ver_archivos_SB11_en_bucket():
    response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=25, Prefix='SB11',)
    return response


def obtener_dataframe(file_name):
    return pd.read_pickle(f"s3://{bucket_name}/{file_name}")


def verificar_modelo(path, file_name):
    for file in os.listdir(path):
        print(file)
        if file == file_name:
            return True
        return False


def obtener_modelo(calendario):
    if calendario == "A":
        periodo = 20202
    else:
        periodo = 20211
    print("periodo", periodo)
    path = "App/Infrastructure/Data/models"
    file_name = f"random_forest_saber_11_{periodo}.joblib"

    if not verificar_modelo(path, file_name):
        print("Descargando modelo desde s3")
        s3_client.download_file(bucket_model_name, file_name, f"{path}/{file_name}")
    return joblib.load(f"{path}/{file_name}")
