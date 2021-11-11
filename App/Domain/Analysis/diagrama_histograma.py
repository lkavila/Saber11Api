from App.Domain.Analysis.utils import mantener_columnas
from App.Infrastructure.Repository.get_data import get_dataframe_for_year
import pandas as pd

def distribucionDeDatos(periodo,tpuntaje,departamento,municipio,colegio):
    result=[]
    r = []
    bins= newbins(tpuntaje)
    names=newnames(tpuntaje)
    result.append({'ejex': names})
    df=newdf(periodo,tpuntaje,departamento,municipio,colegio,bins,names)
    total = 0
    for i in names:
        j=int(df[i])
        r.append(j)
        total = total + j

    result.append({'ejey': r})
    result.append({'Total de datos': total})
    return result
def distribucionacumulada(calendario,tpuntaje,departamento,municipio,colegio):
    result=[]
    r = []
    bins = newbins(tpuntaje)
    names = newnames(tpuntaje)
    result.append({'ejex': names})
    df1 = newdf((2017*10)+calendario, tpuntaje, departamento, municipio, colegio,bins,names)
    df2 = newdf((2018*10)+calendario, tpuntaje, departamento, municipio, colegio,bins,names)
    df3 = newdf((2019*10)+calendario, tpuntaje, departamento, municipio, colegio,bins,names)
    df4 = newdf((2020*10)+calendario, tpuntaje, departamento, municipio, colegio,bins,names)
    total=0
    for i in names:
        j=int(df1[i]+df2[i]+df3[i]+df4[i])
        r.append(j)
        total=total+j

    result.append({'ejey': r})
    result.append({'Total de datos': total})
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

def newdf(periodo,tpuntaje,departamento,municipio,colegio,bins,names):
    df = get_dataframe_for_year(periodo)
    df = mantener_columnas(df,[tpuntaje,'COLE_DEPTO_UBICACION','COLE_MCPIO_UBICACION','COLE_NOMBRE_ESTABLECIMIENTO'])
    if(departamento!=None):
        df = df[df['COLE_DEPTO_UBICACION'] == departamento.upper()]
        if (municipio != None):
            df = df[df['COLE_MCPIO_UBICACION'] == municipio.upper()]
            if (colegio != None):
                df = df[df['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]


    df[tpuntaje]=pd.cut(df[tpuntaje],bins,labels=names)
    df = df.groupby(tpuntaje).size()
    return df