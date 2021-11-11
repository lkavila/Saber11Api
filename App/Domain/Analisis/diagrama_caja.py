from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analisis.utils import mantener_columnas, puntajes, variables_socieconomicas


def diagrama_caja(periodo, variable, puntaje):

    if variable in variables_socieconomicas:
        if puntaje in puntajes:
            dataframe = get_dataframe_for_year(periodo)
            dataframe = mantener_columnas(dataframe, [variable, puntaje])
            dataframe = dataframe.sample(n=10000)
            dataframe = dataframe.astype('object')
            categorias = dataframe[variable].value_counts()
            categorias = list(categorias.index)
            resultado = []
            resultado.append({"categorias": categorias})
            for categoria in categorias:
                df = dataframe[dataframe[variable] == categoria]
                resultado.append({"categoria": categoria, "x": list(df[puntaje].values)})
            return resultado
        else:
            return "Error: el puntaje no es valido"
    else:
        return "Error: la variable socieconomica no es valida"