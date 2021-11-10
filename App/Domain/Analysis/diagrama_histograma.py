from App.Domain.Analysis.utils import mantener_columnas
from App.Infrastructure.Repository.get_data import get_dataframe_for_year
import pandas as pd

def distribucionDeDatos(periodo,tpuntaje,departamento,municipio,colegio):
    result=[]
    r = []
    bins= newbins(tpuntaje)
    names=newnames(tpuntaje)
    result.append({'ejex': names})
    df=newdf(periodo,tpuntaje,departamento,municipio,colegio)
    df[tpuntaje]=pd.cut(df[tpuntaje],bins,labels=names)
    df = df.groupby(tpuntaje).size()
    for i in names:
        r.append(int(df[i]))

    result.append({'ejey': r})
    return result

def newbins(tpuntaje):
    if (tpuntaje == 'PUNT_GLOBAL'):
        bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    if (tpuntaje != 'PUNT_GLOBAL'):
        bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    return bins

def newnames(tpuntaje):
    if (tpuntaje == 'PUNT_GLOBAL'):
        names = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450','450-500']
    if (tpuntaje != 'PUNT_GLOBAL'):
        names = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']

    return names

def newdf(periodo,tpuntaje,departamento,municipio,colegio):
    df = get_dataframe_for_year(periodo)
    df = mantener_columnas(df,[tpuntaje,'COLE_DEPTO_UBICACION','COLE_MCPIO_UBICACION','COLE_NOMBRE_ESTABLECIMIENTO'])
    if(departamento!=None):
        df = df[df['COLE_DEPTO_UBICACION'] == departamento.upper()]
        if (municipio != None):
            df = df[df['COLE_MCPIO_UBICACION'] == municipio.upper()]
            if (colegio != None):
                df = df[df['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]
    return df