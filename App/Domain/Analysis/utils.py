

def mantener_columnas(dataframe, columnas_permanecen):
    columnas = dataframe.columns.values
    eliminar = []
    for x in columnas:
        if x not in columnas_permanecen:
            eliminar.append(x)
    return dataframe.drop(columns=eliminar)