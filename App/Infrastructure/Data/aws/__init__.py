import boto3
import pandas as pd

bucket_name = 'saber11-datasets'
s3_client = boto3.client('s3')


def subir_dataset(path, name):
    s3_client.upload_file(path+"/"+name, bucket_name, name)


def subir_dataset_v2(dataframe, name):
    dataframe.to_pickle(f"s3://{bucket_name}/{name}")


def ver_archivos_en_bucket():
    response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=25, Prefix='SB11',)
    return response


def obtener_dataframe(file_name):
    return pd.read_pickle(f"s3://{bucket_name}/{file_name}")
