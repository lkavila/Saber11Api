import os
import importlib
import threading


def get_pkl_name(full_name):
    if full_name[:-4] == '.pkl':
        return full_name[:10]


def get_xlsm_name(full_name):
    if full_name[:-5] == '.xlsm':
        return full_name[:10]


def run():
    path_data = 'App/Infrastructure/Data'
    path_xlsm = path_data + '/xlsm'
    path_pkl = path_data + '/pkl'

    xlsm_files = set()
    for file in os.listdir(path_xlsm):
        xlsm_files.add(get_xlsm_name(file))

    pkl_files = set()
    for file in os.listdir(path_pkl):
        pkl_files.add(get_pkl_name(file))

    pkl_faltantes = xlsm_files - pkl_files
    print("Archivos nuevos", end=" ")
    print(pkl_faltantes)
    if len(pkl_faltantes) > 0:
        for file in pkl_faltantes:
            print(file)
            full_module_name = 'App.Infrastructure.Data.SB11'
            SB11 = importlib.import_module(full_module_name)
            threading.Thread(target=SB11.run, args=(file,), name=file).start()
