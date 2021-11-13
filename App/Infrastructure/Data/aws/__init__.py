import boto3
import pandas as pd
import joblib

bucket_name = 'saber11-datasets'
prefix_depurados = 'depurados'
prefix_no_depurados = 'no-depurados'
bucket_model_name = "modelos-saber-11"
s3_client = boto3.client('s3')
models_path = "App/Infrastructure/Data/models"


def ver_archivos_SB11_en_bucket(prefix):
    response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=25, Prefix=prefix+'/SB11',)
    return response


def obtener_dataframe(file_name):
    return pd.read_pickle(f"s3://{bucket_name}/{file_name}")


def obtener_modelos_desde_s3():
    file_name = f"random_forest_saber_11_{20202}.joblib"
    s3_client.download_file(bucket_model_name, file_name, f"{models_path}/{file_name}")
    file_name = f"random_forest_saber_11_{20211}.joblib"
    s3_client.download_file(bucket_model_name, file_name, f"{models_path}/{file_name}")


def obtener_modelo(calendario):
    if calendario == "A":
        periodo = 20202
    else:
        periodo = 20211
    file_name = f"random_forest_saber_11_{periodo}.joblib"
    return joblib.load(f"{models_path}/{file_name}")
