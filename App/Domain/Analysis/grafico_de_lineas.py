from App.Domain.Analysis.utils import mantener_columnas
from App.Infrastructure.Repository.get_data import get_dataframe_for_year


def promedio_gen(calendario,tipoPuntaje):
    if(calendario < 1 or calendario > 2):
        dataframe1 = get_dataframe_for_year(20171)
        dataframe2 = get_dataframe_for_year(20181)
        dataframe3 = get_dataframe_for_year(20191)
        dataframe4 = get_dataframe_for_year(20201)
        dataframe5 = get_dataframe_for_year(20172)
        dataframe6 = get_dataframe_for_year(20182)
        dataframe7 = get_dataframe_for_year(20192)
        dataframe8 = get_dataframe_for_year(20202)
        x = ['2017', '2018', '2019', '2020']
        dataframe1 = mantener_columnas(dataframe1, tipoPuntaje)
        dataframe2 = mantener_columnas(dataframe2, tipoPuntaje)
        dataframe3 = mantener_columnas(dataframe3, tipoPuntaje)
        dataframe4 = mantener_columnas(dataframe4, tipoPuntaje)
        dataframe5= mantener_columnas(dataframe5, tipoPuntaje)
        dataframe6 = mantener_columnas(dataframe6, tipoPuntaje)
        dataframe7 = mantener_columnas(dataframe7, tipoPuntaje)
        dataframe8 = mantener_columnas(dataframe8, tipoPuntaje)
        dataframe1 = dataframe1.mean().to_dict()
        dataframe2 = dataframe2.mean().to_dict()
        dataframe3 = dataframe3.mean().to_dict()
        dataframe4 = dataframe4.mean().to_dict()
        dataframe5 = dataframe5.mean().to_dict()
        dataframe6 = dataframe6.mean().to_dict()
        dataframe7 = dataframe7.mean().to_dict()
        dataframe8 = dataframe8.mean().to_dict()
        result = []
        result.append({'ejex': x})
        result.append({'ejey1': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                dataframe4[tipoPuntaje]]})
        result.append({'ejey2': [dataframe5[tipoPuntaje], dataframe6[tipoPuntaje], dataframe7[tipoPuntaje],
                                 dataframe8[tipoPuntaje]]})
    if(calendario==1):
        dataframe1 = get_dataframe_for_year(20171)
        dataframe2 = get_dataframe_for_year(20181)
        dataframe3 = get_dataframe_for_year(20191)
        dataframe4 = get_dataframe_for_year(20201)
        x =['20171','20181','20191','20201']
        dataframe1 = mantener_columnas(dataframe1, tipoPuntaje)
        dataframe2 = mantener_columnas(dataframe2, tipoPuntaje)
        dataframe3 = mantener_columnas(dataframe3, tipoPuntaje)
        dataframe4 = mantener_columnas(dataframe4, tipoPuntaje)
        dataframe1 = dataframe1.mean().to_dict()
        dataframe2 = dataframe2.mean().to_dict()
        dataframe3 = dataframe3.mean().to_dict()
        dataframe4 = dataframe4.mean().to_dict()
        result = []
        result.append({'ejex': x})
        result.append({'ejey': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                dataframe4[tipoPuntaje]]})

    if (calendario==2):
        dataframe1 = get_dataframe_for_year(20172)
        dataframe2 = get_dataframe_for_year(20182)
        dataframe3 = get_dataframe_for_year(20192)
        dataframe4 = get_dataframe_for_year(20202)
        x = ['20172', '20182', '20192', '20202']
        dataframe1 = mantener_columnas(dataframe1, tipoPuntaje)
        dataframe2 = mantener_columnas(dataframe2, tipoPuntaje)
        dataframe3 = mantener_columnas(dataframe3, tipoPuntaje)
        dataframe4 = mantener_columnas(dataframe4, tipoPuntaje)
        dataframe1 = dataframe1.mean().to_dict()
        dataframe2 = dataframe2.mean().to_dict()
        dataframe3 = dataframe3.mean().to_dict()
        dataframe4 = dataframe4.mean().to_dict()
        result = []
        result.append({'ejex': x})
        result.append({'ejey': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje], dataframe4[tipoPuntaje]]})

    return result

def desviaciones_generales(calendario,tipoPuntaje):
    if (calendario < 1 or calendario > 2):
        dataframe1 = get_dataframe_for_year(20171)
        dataframe2 = get_dataframe_for_year(20181)
        dataframe3 = get_dataframe_for_year(20191)
        dataframe4 = get_dataframe_for_year(20201)
        dataframe5 = get_dataframe_for_year(20172)
        dataframe6 = get_dataframe_for_year(20182)
        dataframe7 = get_dataframe_for_year(20192)
        dataframe8 = get_dataframe_for_year(20202)
        x = ['2017', '2018', '2019', '2020']
        dataframe1 = mantener_columnas(dataframe1, tipoPuntaje)
        dataframe2 = mantener_columnas(dataframe2, tipoPuntaje)
        dataframe3 = mantener_columnas(dataframe3, tipoPuntaje)
        dataframe4 = mantener_columnas(dataframe4, tipoPuntaje)
        dataframe5 = mantener_columnas(dataframe5, tipoPuntaje)
        dataframe6 = mantener_columnas(dataframe6, tipoPuntaje)
        dataframe7 = mantener_columnas(dataframe7, tipoPuntaje)
        dataframe8 = mantener_columnas(dataframe8, tipoPuntaje)
        dataframe1 = dataframe1.std().to_dict()
        dataframe2 = dataframe2.std().to_dict()
        dataframe3 = dataframe3.std().to_dict()
        dataframe4 = dataframe4.std().to_dict()
        dataframe5 = dataframe5.std().to_dict()
        dataframe6 = dataframe6.std().to_dict()
        dataframe7 = dataframe7.std().to_dict()
        dataframe8 = dataframe8.std().to_dict()
        result = []
        result.append({'ejex': x})
        result.append({'ejey1': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                 dataframe4[tipoPuntaje]]})
        result.append({'ejey2': [dataframe5[tipoPuntaje], dataframe6[tipoPuntaje], dataframe7[tipoPuntaje],
                                 dataframe8[tipoPuntaje]]})
    if (calendario == 1):
        dataframe1 = get_dataframe_for_year(20171)
        dataframe2 = get_dataframe_for_year(20181)
        dataframe3 = get_dataframe_for_year(20191)
        dataframe4 = get_dataframe_for_year(20201)
        x = ['20171', '20181', '20191', '20201']
        dataframe1 = mantener_columnas(dataframe1, tipoPuntaje)
        dataframe2 = mantener_columnas(dataframe2, tipoPuntaje)
        dataframe3 = mantener_columnas(dataframe3, tipoPuntaje)
        dataframe4 = mantener_columnas(dataframe4, tipoPuntaje)
        dataframe1 = dataframe1.std().to_dict()
        dataframe2 = dataframe2.std().to_dict()
        dataframe3 = dataframe3.std().to_dict()
        dataframe4 = dataframe4.std().to_dict()
        result = []
        result.append({'ejex': x})
        result.append({'ejey': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                dataframe4[tipoPuntaje]]})

    if (calendario == 2):
        dataframe1 = get_dataframe_for_year(20172)
        dataframe2 = get_dataframe_for_year(20182)
        dataframe3 = get_dataframe_for_year(20192)
        dataframe4 = get_dataframe_for_year(20202)
        x = ['20172', '20182', '20192', '20202']
        dataframe1 = mantener_columnas(dataframe1, tipoPuntaje)
        dataframe2 = mantener_columnas(dataframe2, tipoPuntaje)
        dataframe3 = mantener_columnas(dataframe3, tipoPuntaje)
        dataframe4 = mantener_columnas(dataframe4, tipoPuntaje)
        dataframe1 = dataframe1.std().to_dict()
        dataframe2 = dataframe2.std().to_dict()
        dataframe3 = dataframe3.std().to_dict()
        dataframe4 = dataframe4.std().to_dict()
        result = []
        result.append({'ejex': x})
        result.append({'ejey': [dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                dataframe4[tipoPuntaje]]})

    return result

def variable_economica(calendario,tipoPuntaje,variableEconomica):
    result = []
    if(calendario > 0 and calendario < 3):

        columnasmantener = [tipoPuntaje, variableEconomica]
        if(calendario ==1):
            dataframe1 = get_dataframe_for_year(20171)
            dataframe2 = get_dataframe_for_year(20181)
            dataframe3 = get_dataframe_for_year(20191)
            dataframe4 = get_dataframe_for_year(20201)
        else:
            dataframe1 = get_dataframe_for_year(20172)
            dataframe2 = get_dataframe_for_year(20182)
            dataframe3 = get_dataframe_for_year(20192)
            dataframe4 = get_dataframe_for_year(20202)
        list = mantener_columnas(dataframe1,variableEconomica)
        list = list.drop_duplicates()
        list =list.sort_values(by=variableEconomica)
        dataframe1 = mantener_columnas(dataframe1, columnasmantener)
        dataframe2 = mantener_columnas(dataframe2, columnasmantener)
        dataframe3 = mantener_columnas(dataframe3, columnasmantener)
        dataframe4 = mantener_columnas(dataframe4, columnasmantener)
        dataframe1 = dataframe1.groupby(by=variableEconomica).mean()
        dataframe2 = dataframe2.groupby(by=variableEconomica).mean()
        dataframe3 = dataframe3.groupby(by=variableEconomica).mean()
        dataframe4 = dataframe4.groupby(by=variableEconomica).mean()
        for d1,d2,d3,d4,l1 in zip(dataframe1[tipoPuntaje],dataframe2[tipoPuntaje],dataframe3[tipoPuntaje],dataframe4[tipoPuntaje],list[variableEconomica]):
            v1=[d1,d2,d3,d4]
            result.append({l1:v1})
        result.append(promedio_gen(calendario,tipoPuntaje))
    return result


def desviacion_economica(calendario,tipoPuntaje,variableEconomica):
    result = []
    if (calendario > 0 and calendario < 3):

        columnasmantener = [tipoPuntaje, variableEconomica]
        if (calendario == 1):
            dataframe1 = get_dataframe_for_year(20171)
            dataframe2 = get_dataframe_for_year(20181)
            dataframe3 = get_dataframe_for_year(20191)
            dataframe4 = get_dataframe_for_year(20201)
        else:
            dataframe1 = get_dataframe_for_year(20172)
            dataframe2 = get_dataframe_for_year(20182)
            dataframe3 = get_dataframe_for_year(20192)
            dataframe4 = get_dataframe_for_year(20202)
        list = mantener_columnas(dataframe1, variableEconomica)
        list = list.drop_duplicates()
        list = list.sort_values(by=variableEconomica)
        dataframe1 = mantener_columnas(dataframe1, columnasmantener)
        dataframe2 = mantener_columnas(dataframe2, columnasmantener)
        dataframe3 = mantener_columnas(dataframe3, columnasmantener)
        dataframe4 = mantener_columnas(dataframe4, columnasmantener)
        dataframe1 = dataframe1.groupby(by=variableEconomica).std()
        dataframe2 = dataframe2.groupby(by=variableEconomica).std()
        dataframe3 = dataframe3.groupby(by=variableEconomica).std()
        dataframe4 = dataframe4.groupby(by=variableEconomica).std()
        for d1, d2, d3, d4, l1 in zip(dataframe1[tipoPuntaje], dataframe2[tipoPuntaje], dataframe3[tipoPuntaje],
                                      dataframe4[tipoPuntaje], list[variableEconomica]):
            v1 = [d1, d2, d3, d4]
            result.append({l1: v1})
        result.append(desviaciones_generales(calendario, tipoPuntaje))
    return result

