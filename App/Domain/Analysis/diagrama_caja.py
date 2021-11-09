from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analysis.utils import mantener_columnas


def diagrama_caja(periodo, variable, puntaje):
    variables_socieconomicas = ['ESTU_GENERO', 'ESTU_TIENEETNIA', 'FAMI_ESTRATOVIVIENDA', 'FAMI_CUARTOSHOGAR',
                                'FAMI_PERSONASHOGAR','FAMI_TIENEINTERNET','FAMI_TIENESERVICIOTV','FAMI_TIENECOMPUTADOR',
                                'FAMI_TIENECONSOLAVIDEOJUEGOS','FAMI_TIENEAUTOMOVIL','FAMI_NUMLIBROS','FAMI_SITUACIONECONOMICA',
                                'FAMI_EDUCACIONPADRE','FAMI_EDUCACIONMADRE','FAMI_COMECARNEPESCADOHUEVO',
                                'ESTU_DEDICACIONLECTURADIARIA','ESTU_DEDICACIONINTERNET','ESTU_HORASSEMANATRABAJA']

    puntajes = ['PUNT_LECTURA_CRITICA','PUNT_MATEMATICAS','PUNT_C_NATURALES',
                'PUNT_SOCIALES_CIUDADANAS','PUNT_INGLES','PUNT_GLOBAL',]

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