from App.Infrastructure.Repository.get_data import get_classification_model
import pandas as pd


def obtener_orden_columnas():
    return ['ESTU_GENERO', 'FAMI_ESTRATOVIVIENDA', 'FAMI_PERSONASHOGAR',
       'FAMI_CUARTOSHOGAR', 'FAMI_EDUCACIONPADRE', 'FAMI_EDUCACIONMADRE',
       'FAMI_TIENECOMPUTADOR', 'FAMI_NUMLIBROS', 'FAMI_COMECARNEPESCADOHUEVO',
       'FAMI_SITUACIONECONOMICA', 'ESTU_DEDICACIONLECTURADIARIA',
       'ESTU_DEDICACIONINTERNET', 'ESTU_HORASSEMANATRABAJA', 'COLE_NATURALEZA',
       'COLE_BILINGUE', 'COLE_CARACTER', 'COLE_AREA_UBICACION', 'COLE_JORNADA',
       'ESTU_EDAD']


def predecir(variables, calendario):
    load_rf_model = get_classification_model(calendario)
    df = pd.DataFrame(variables)
    df = df[obtener_orden_columnas()]
    return load_rf_model.predict(df)
