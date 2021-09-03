import os
import threading
from App.Infrastructure.Data.SB11 import run as save_data
from App.Infrastructure.Repository.get_data import archivos_en_bucket


def get_pkl_name(full_name):
    if full_name[-4:] == '.pkl':
        return full_name[:10]
    return None


def get_xlsm_name(full_name):
    if full_name[-5:] == '.xlsm':
        return full_name[:10]
    return None


def recorrer_archivos(path):
    files = set()
    for file in os.listdir(path):
        if path[-5:] == '/xlsm':
            file_name = get_xlsm_name(file)
        else:
            file_name = None
        if file_name is not None:
            files.add(file_name)
    return files


def run():
    path_data = 'App/Infrastructure/Data'
    path_xlsm = path_data + '/xlsm'

    xlsm_files = recorrer_archivos(path_xlsm)
    pkl_files = set()
    for dicc in archivos_en_bucket:
        pkl_files.add(get_pkl_name(dicc['Key']))

    faltantes = xlsm_files - pkl_files

    print("Archivos nuevos", faltantes)
    if len(faltantes) > 0:
        for file in faltantes:
            threading.Thread(target=save_data, args=(file,), name=file).start()
