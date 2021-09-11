from App.Infrastructure.Repository.get_data import get_dataframe_for_year
from App.Domain.Analysis.utils import mantener_columnas


def transformar_estrato(x):
    if x == 'Estrato 1':
        return 1
    if x == 'Estrato 2':
        return 2
    if x == 'Estrato 3':
        return 3
    if x == 'Estrato 4':
        return 4
    if x == 'Estrato 5':
        return 5
    if x == 'Estrato 6':
        return 6
    else:
        return 0


def mejores_colegios(periodo, departamento, municipio, puntajes, top, num_estudiantes):

    dataframe = get_dataframe_for_year(periodo)
    top = top is None and 10 or top
    num_estudiantes = num_estudiantes is None and 1 or num_estudiantes
    columnas_mantener = ['COLE_NOMBRE_ESTABLECIMIENTO', 'COLE_DEPTO_UBICACION', 'COLE_MCPIO_UBICACION',
                         'COLE_BILINGUE', 'COLE_CARACTER', 'COLE_AREA_UBICACION',
                         'COLE_NATURALEZA', 'FAMI_ESTRATOVIVIENDA'] + puntajes
    dataframe = mantener_columnas(dataframe, columnas_mantener)
    if departamento is not None:
        dataframe = dataframe[dataframe['COLE_DEPTO_UBICACION'] == departamento.upper()]
    if municipio is not None:
        dataframe = dataframe[dataframe['COLE_MCPIO_UBICACION'] == municipio.upper()]

    dataframe['NUM_ESTUDIANTES'] = dataframe.groupby(by='COLE_NOMBRE_ESTABLECIMIENTO')['COLE_DEPTO_UBICACION'].transform(len)
    dataframe = dataframe[dataframe['NUM_ESTUDIANTES'] >= num_estudiantes]
    dataframe['FAMI_ESTRATOVIVIENDA'] = dataframe['FAMI_ESTRATOVIVIENDA'].apply(transformar_estrato)
    dataframe = dataframe.groupby(['COLE_NOMBRE_ESTABLECIMIENTO', 'COLE_DEPTO_UBICACION','COLE_MCPIO_UBICACION', 'COLE_NATURALEZA','COLE_BILINGUE', 'COLE_CARACTER', 'COLE_AREA_UBICACION',]).mean().reset_index()
    df = dataframe.sort_values(by=puntajes, ascending=False).head(top)

    pos = 1
    respuesta = []
    for i in df.index:
        colegio = {
                   "nombre": df['COLE_NOMBRE_ESTABLECIMIENTO'][i],
                   "numero estudiantes": df['NUM_ESTUDIANTES'][i],
                   "posición": pos,
                   "departamento": df['COLE_DEPTO_UBICACION'][i],
                   "municipio": df['COLE_MCPIO_UBICACION'][i],
                   "bilingue": df['COLE_BILINGUE'][i],
                   "naturaleza": df['COLE_NATURALEZA'][i],
                   "cáracter": df['COLE_CARACTER'][i],
                   "area": df['COLE_AREA_UBICACION'][i],
                   "promedio estrato familia estudiante": df['FAMI_ESTRATOVIVIENDA'][i],
                   "puntaje promedio": df['PUNT_GLOBAL'][i]
                   }
        respuesta.append(colegio)
        pos = pos + 1

    return respuesta




