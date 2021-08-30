import pandas as pd

pkls_path = "App/Infrastructure/Data/pkl/"
data_pkl_20191 = pd.read_pickle(pkls_path+"SB11_20191.pkl")
data_pkl_20192 = pd.read_pickle(pkls_path+"SB11_20192.pkl")
data_pkl_20201 = pd.read_pickle(pkls_path+"SB11_20201.pkl")
data_pkl_20202 = pd.read_pickle(pkls_path+"SB11_20202.pkl")
data_pkl_20211 = pd.read_pickle(pkls_path+"SB11_20211.pkl")

def df_20191():
    return data_pkl_20191


def df_20192():
    return data_pkl_20192


def df_20201():
    return data_pkl_20201


def df_20202():
    return data_pkl_20202

def df_20211():
    return data_pkl_20211