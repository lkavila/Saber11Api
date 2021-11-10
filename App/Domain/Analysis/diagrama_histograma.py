from App.Domain.Analysis.utils import mantener_columnas
from App.Infrastructure.Repository.get_data import get_dataframe_for_year
import pandas as pd

def distribucionDeDatos(periodo,tpuntaje):
    result=[]
    if(tpuntaje=='PUNT_GLOBAL'):
        bins = [0,50,100,150,200,250,300,350,400,450,500]
        names=['0-50','50-100','100-150','150-200','200-250','250-300','300-350','350-400','400-450','450-500']
    if(tpuntaje!='PUNT_GLOBAL'):
        bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        names=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']
    dataframe = get_dataframe_for_year(periodo)
    dataframe = mantener_columnas(dataframe,tpuntaje)
    dataframe[tpuntaje]=pd.cut(dataframe[tpuntaje],bins,labels=names)
    dataframe = dataframe.groupby(tpuntaje).size()
    result.append({'ejex':names})
    r=[]

    for i in names:
        r.append(int(dataframe[i]))

    result.append({'ejey': r})
    return result