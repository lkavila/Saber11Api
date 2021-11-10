from App.Domain.Analysis.utils import mantener_columnas
from App.Infrastructure.Repository.get_data import get_dataframe_for_year


def promedio_gen(calendario,tipoPuntaje):
    result=[]
    if(calendario < 1 or calendario > 2):
        dataframe1 = newdf(20171,tipoPuntaje).mean().to_dict()
        dataframe2 = newdf(20181,tipoPuntaje).mean().to_dict()
        dataframe3 = newdf(20191,tipoPuntaje).mean().to_dict()
        dataframe4 = newdf(20201,tipoPuntaje).mean().to_dict()
        dataframe5 = newdf(20172,tipoPuntaje).mean().to_dict()
        dataframe6 = newdf(20182,tipoPuntaje).mean().to_dict()
        dataframe7 = newdf(20192,tipoPuntaje).mean().to_dict()
        dataframe8 = newdf(20202,tipoPuntaje).mean().to_dict()
        x = ['2017', '2018', '2019', '2020']
        result.append({'ejex': x})
        result.append({'ejey1': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],dataframe4[tipoPuntaje]]})
        result.append({'ejey2': [dataframe5[tipoPuntaje], dataframe6[tipoPuntaje], dataframe7[tipoPuntaje],dataframe8[tipoPuntaje]]})
    else:
        dataframe1 = newdf((2017*10)+calendario, tipoPuntaje).mean().to_dict()
        dataframe2 = newdf((2018*10)+calendario, tipoPuntaje).mean().to_dict()
        dataframe3 = newdf((2019*10)+calendario, tipoPuntaje).mean().to_dict()
        dataframe4 = newdf((2020*10)+calendario, tipoPuntaje).mean().to_dict()
        x = ['2017'+str(calendario), '2018'+str(calendario), '2019'+str(calendario), '2020'+str(calendario)]
        result.append({'ejex': x})
        result.append({'ejey': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje], dataframe4[tipoPuntaje]]})

    return result

def desviaciones_generales(calendario,tipoPuntaje):
    result = []
    if (calendario < 1 or calendario > 2):
        dataframe1 = newdf(20171, tipoPuntaje).std().to_dict()
        dataframe2 = newdf(20181, tipoPuntaje).std().to_dict()
        dataframe3 = newdf(20191, tipoPuntaje).std().to_dict()
        dataframe4 = newdf(20201, tipoPuntaje).std().to_dict()
        dataframe5 = newdf(20172, tipoPuntaje).std().to_dict()
        dataframe6 = newdf(20182, tipoPuntaje).std().to_dict()
        dataframe7 = newdf(20192, tipoPuntaje).std().to_dict()
        dataframe8 = newdf(20202, tipoPuntaje).std().to_dict()
        x = ['2017', '2018', '2019', '2020']
        result.append({'ejex': x})
        result.append({'ejey1': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                 dataframe4[tipoPuntaje]]})
        result.append({'ejey2': [dataframe5[tipoPuntaje], dataframe6[tipoPuntaje], dataframe7[tipoPuntaje],
                                 dataframe8[tipoPuntaje]]})
    else:
        dataframe1 = newdf((2017 * 10) + calendario, tipoPuntaje).std().to_dict()
        dataframe2 = newdf((2018 * 10) + calendario, tipoPuntaje).std().to_dict()
        dataframe3 = newdf((2019 * 10) + calendario, tipoPuntaje).std().to_dict()
        dataframe4 = newdf((2020 * 10) + calendario, tipoPuntaje).std().to_dict()
        x = ['2017' + str(calendario), '2018' + str(calendario), '2019' + str(calendario), '2020' + str(calendario)]
        result.append({'ejex': x})
        result.append({'ejey': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                dataframe4[tipoPuntaje]]})

    return result

def variable_economica(calendario,tipoPuntaje,variableEconomica):
    result = []
    if(calendario > 0 and calendario < 3):
        columnasmantener = [tipoPuntaje, variableEconomica]
        dataframe1 = newdf((2017 * 10) + calendario, [tipoPuntaje,variableEconomica]).groupby(by=variableEconomica).mean()
        dataframe2 = newdf((2018 * 10) + calendario, [tipoPuntaje,variableEconomica]).groupby(by=variableEconomica).mean()
        dataframe3 = newdf((2019 * 10) + calendario, [tipoPuntaje,variableEconomica]).groupby(by=variableEconomica).mean()
        dataframe4 = newdf((2020 * 10) + calendario, [tipoPuntaje,variableEconomica]).groupby(by=variableEconomica).mean()
        list = newdf((2020 * 10) + calendario,variableEconomica)
        list = list.drop_duplicates()
        list =list.sort_values(by=variableEconomica)
        for d1,d2,d3,d4,l1 in zip(dataframe1[tipoPuntaje],dataframe2[tipoPuntaje],dataframe3[tipoPuntaje],dataframe4[tipoPuntaje],list[variableEconomica]):
            v1=[d1,d2,d3,d4]
            result.append({l1:v1})
        result.append(promedio_gen(calendario,tipoPuntaje))
    return result


def desviacion_economica(calendario,tipoPuntaje,variableEconomica):
    result = []
    if (calendario > 0 and calendario < 3):
        columnasmantener = [tipoPuntaje, variableEconomica]
        dataframe1 = newdf((2017 * 10) + calendario, [tipoPuntaje, variableEconomica]).groupby(by=variableEconomica).std()
        dataframe2 = newdf((2018 * 10) + calendario, [tipoPuntaje, variableEconomica]).groupby(by=variableEconomica).std()
        dataframe3 = newdf((2019 * 10) + calendario, [tipoPuntaje, variableEconomica]).groupby(by=variableEconomica).std()
        dataframe4 = newdf((2020 * 10) + calendario, [tipoPuntaje, variableEconomica]).groupby(by=variableEconomica).std()
        list = newdf((2020 * 10) + calendario,variableEconomica)
        list = list.drop_duplicates()
        list = list.sort_values(by=variableEconomica)
        for d1, d2, d3, d4, l1 in zip(dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                      dataframe4[tipoPuntaje], list[variableEconomica]):
            v1 = [d1, d2, d3, d4]
            result.append({l1: v1})
        result.append(promedio_gen(calendario, tipoPuntaje))
    return result

def promediocolegio(calendario,departamento,municipio,colegio,tipoPuntaje):
    mantener_colum=['COLE_DEPTO_UBICACION', 'COLE_MCPIO_UBICACION','COLE_NOMBRE_ESTABLECIMIENTO']
    mantener_colum.append(tipoPuntaje)
    result= []
    dataframe1 = newdf((2017 * 10) + calendario, mantener_colum)
    dataframe2 = newdf((2018 * 10) + calendario, mantener_colum)
    dataframe3 = newdf((2019 * 10) + calendario, mantener_colum)
    dataframe4 = newdf((2020 * 10) + calendario, mantener_colum)
    x = ['2017' + str(calendario), '2018' + str(calendario), '2019' + str(calendario), '2020' + str(calendario)]
    dataframe1 = filtrar(dataframe1,departamento,municipio,colegio)
    dataframe2 = filtrar(dataframe2,departamento,municipio,colegio)
    dataframe3 = filtrar(dataframe3,departamento,municipio,colegio)
    dataframe4 = filtrar(dataframe4,departamento,municipio,colegio)
    result.append({'ejex': x})
    result.append({'ejeypromedio': [dataframe1.mean()[tipoPuntaje], dataframe2.mean()[tipoPuntaje], dataframe3.mean()[tipoPuntaje],dataframe4.mean()[tipoPuntaje]]})
    result.append({'ejeydesviacion': [dataframe1.std()[tipoPuntaje], dataframe2.std()[tipoPuntaje], dataframe3.std()[tipoPuntaje],dataframe4.std()[tipoPuntaje]]})
    result.append({'ejeymejorpuntaje': mejores(dataframe1,dataframe2,dataframe3,dataframe4,tipoPuntaje)})
    result.append({'ejeypeorpuntaje': peores(dataframe1,dataframe2,dataframe3,dataframe4,tipoPuntaje)})
    return result

def promedioDepto(calendario,departamento,tipoPuntaje):
    mantener_colum = ['COLE_DEPTO_UBICACION',]
    mantener_colum.append(tipoPuntaje)
    result = []
    dataframe1 = newdf((2017 * 10) + calendario, mantener_colum)
    dataframe2 = newdf((2018 * 10) + calendario, mantener_colum)
    dataframe3 = newdf((2019 * 10) + calendario, mantener_colum)
    dataframe4 = newdf((2020 * 10) + calendario, mantener_colum)
    x = ['2017' + str(calendario), '2018' + str(calendario), '2019' + str(calendario), '2020' + str(calendario)]
    dataframe1 = filtrar(dataframe1, departamento, None, None)
    dataframe2 = filtrar(dataframe2, departamento, None, None)
    dataframe3 = filtrar(dataframe3, departamento, None, None)
    dataframe4 = filtrar(dataframe4, departamento, None, None)
    result.append({'ejex': x})
    result.append({'ejeypromedio': [dataframe1.mean()[tipoPuntaje], dataframe2.mean()[tipoPuntaje],dataframe3.mean()[tipoPuntaje],dataframe4.mean()[tipoPuntaje]]})
    result.append( {'ejeydesviacion': [dataframe1.std()[tipoPuntaje], dataframe2.std()[tipoPuntaje], dataframe3.std()[tipoPuntaje],dataframe4.std()[tipoPuntaje]]})
    result.append({'ejeymejorpuntaje': mejores(dataframe1,dataframe2,dataframe3,dataframe4,tipoPuntaje)})
    result.append({'ejeypeorpuntaje': peores(dataframe1,dataframe2,dataframe3,dataframe4,tipoPuntaje)})

    return result
def promediomunicipio(calendario,departamento,municipio,tipoPuntaje):
    mantener_colum=['COLE_DEPTO_UBICACION', 'COLE_MCPIO_UBICACION']
    mantener_colum.append(tipoPuntaje)
    result= []
    dataframe1 = newdf((2017 * 10) + calendario, mantener_colum)
    dataframe2 = newdf((2018 * 10) + calendario, mantener_colum)
    dataframe3 = newdf((2019 * 10) + calendario, mantener_colum)
    dataframe4 = newdf((2020 * 10) + calendario, mantener_colum)
    x = ['2017' + str(calendario), '2018' + str(calendario), '2019' + str(calendario), '2020' + str(calendario)]
    dataframe1 = filtrar(dataframe1,departamento,municipio,None)
    dataframe2 = filtrar(dataframe2,departamento,municipio,None)
    dataframe3 = filtrar(dataframe3,departamento,municipio,None)
    dataframe4 = filtrar(dataframe4,departamento,municipio,None)
    result.append({'ejex': x})
    result.append({'ejeypromedio': [dataframe1.mean()[tipoPuntaje], dataframe2.mean()[tipoPuntaje], dataframe3.mean()[tipoPuntaje],dataframe4.mean()[tipoPuntaje]]})
    result.append({'ejeydesviacion': [dataframe1.std()[tipoPuntaje], dataframe2.std()[tipoPuntaje], dataframe3.std()[tipoPuntaje],dataframe4.std()[tipoPuntaje]]})

    result.append({'ejeymejorpuntaje':mejores(dataframe1,dataframe2,dataframe3,dataframe4,tipoPuntaje) })
    result.append({'ejeypeorpuntaje': peores(dataframe1,dataframe2,dataframe3,dataframe4,tipoPuntaje)})
    return result


def mejores (df1,df2,df3,df4,tipoPuntaje):
    mejores=[]
    df1=df1.sort_values(by=tipoPuntaje, ascending=False).head(1)
    df2=df2.sort_values(by=tipoPuntaje, ascending=False).head(1)
    df3=df3.sort_values(by=tipoPuntaje, ascending=False).head(1)
    df4=df4.sort_values(by=tipoPuntaje, ascending=False).head(1)
    for d1,d2,d3,d4 in zip(df1[tipoPuntaje],df2[tipoPuntaje],df3[tipoPuntaje],df4[tipoPuntaje]):
        mejores.append(d1)
        mejores.append(d2)
        mejores.append(d3)
        mejores.append(d4)
    return mejores

def peores(df1,df2,df3,df4,tipoPuntaje):
    peores=[]
    df1 = df1.sort_values(by=tipoPuntaje, ascending=True).head(1)
    df2 = df2.sort_values(by=tipoPuntaje, ascending=True).head(1)
    df3 = df3.sort_values(by=tipoPuntaje, ascending=True).head(1)
    df4 = df4.sort_values(by=tipoPuntaje, ascending=True).head(1)
    for d1,d2,d3,d4 in zip(df1[tipoPuntaje],df2[tipoPuntaje],df3[tipoPuntaje],df4[tipoPuntaje]):
        peores.append(d1)
        peores.append(d2)
        peores.append(d3)
        peores.append(d4)
    return peores
def filtrar(df,departamento,municipio,colegio):
    df = df[df['COLE_DEPTO_UBICACION'] == departamento.upper()]
    if(municipio!=None):
        df = df[df['COLE_MCPIO_UBICACION'] == municipio.upper()]
        if(colegio!=None):
            df = df[df['COLE_NOMBRE_ESTABLECIMIENTO'] == colegio.upper()]

    return df
def newdf(periodo,tpuntaje):
    d1 = get_dataframe_for_year(periodo)
    d1 = mantener_columnas(d1, tpuntaje)
    return d1