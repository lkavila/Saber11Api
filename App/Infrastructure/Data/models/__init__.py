import os
import joblib


def verificar_modelo(file_name):
    for file in os.listdir(os.curdir):
        print(file)
        if file == file_name:
            return True
        return False


def get_model(file_name):
    return joblib.load(f"{os.curdir}/{file_name}")
