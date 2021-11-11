
variables_socieconomicas = ['ESTU_GENERO', 'ESTU_TIENEETNIA', 'FAMI_ESTRATOVIVIENDA', 'FAMI_CUARTOSHOGAR',
                            'FAMI_PERSONASHOGAR', 'FAMI_TIENEINTERNET', 'FAMI_TIENESERVICIOTV', 'FAMI_TIENECOMPUTADOR',
                            'FAMI_TIENECONSOLAVIDEOJUEGOS', 'FAMI_TIENEAUTOMOVIL', 'FAMI_NUMLIBROS',
                            'FAMI_SITUACIONECONOMICA',
                            'FAMI_EDUCACIONPADRE', 'FAMI_EDUCACIONMADRE', 'FAMI_COMECARNEPESCADOHUEVO',
                            'ESTU_DEDICACIONLECTURADIARIA', 'ESTU_DEDICACIONINTERNET', 'ESTU_HORASSEMANATRABAJA']

puntajes = ["PUNT_LECTURA_CRITICA", "PUNT_MATEMATICAS", "PUNT_C_NATURALES",
            "PUNT_SOCIALES_CIUDADANAS", "PUNT_INGLES", "PUNT_GLOBAL"]

desempenos = ['DESEMP_LECTURA_CRITICA', 'DESEMP_MATEMATICAS', 'DESEMP_C_NATURALES',
                     'DESEMP_SOCIALES_CIUDADANAS', 'DESEMP_INGLES']

periodos = [20171, 20172, 20181, 20182, 20191, 20192, 20201, 20202, 20211]


def mantener_columnas(dataframe, columnas_permanecen):
    columnas = dataframe.columns.values
    eliminar = []
    for x in columnas:
        if x not in columnas_permanecen:
            eliminar.append(x)
    return dataframe.drop(columns=eliminar)