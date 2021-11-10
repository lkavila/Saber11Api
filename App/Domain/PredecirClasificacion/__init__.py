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

parents_education = {
    "Ninguno": 0,
    "No sabe": 1,
    "No Aplica": 2,
    "Primaria incompleta": 3,
    "Primaria completa": 4,
    "Secundaria (Bachillerato) incompleta": 5,
    "Secundaria (Bachillerato) completa": 6,
    "Técnica o tecnológica incompleta": 7,
    "Técnica o tecnológica completa": 8,
    "Educación profesional incompleta": 9,
    "Educación profesional completa": 10,
    "Postgrado": 11,
}
ordinal_data = {
    "FAMI_PERSONASHOGAR": {"1 a 2": 0, "3 a 4": 1, "5 a 6": 2, "7 a 8": 3, "9 o más": 4},
    "FAMI_EDUCACIONPADRE": parents_education,
    "FAMI_EDUCACIONMADRE": parents_education,
    "FAMI_NUMLIBROS": {"0 A 10 LIBROS": 0, "11 A 25 LIBROS": 1, "26 A 100 LIBROS": 2, "MÁS DE 100 LIBROS": 3},
    "FAMI_COMECARNEPESCADOHUEVO": {"1 o 2 veces por semana": 0, "3 a 5 veces por semana": 1,
                                   "Nunca o rara vez comemos eso": 2, "Todos o casi todos los días": 3},
    "FAMI_SITUACIONECONOMICA": {"Peor": 0, "Igual": 1, "Mejor": 2},
    "ESTU_DEDICACIONLECTURADIARIA": {"No leo por entretenimiento": 0, "30 minutos o menos": 1,
                                     "Entre 30 y 60 minutos": 2, "Entre 1 y 2 horas": 3, "Más de 2 horas": 4},
    "ESTU_DEDICACIONINTERNET": {"No Navega Internet": 0, "30 minutos o menos": 1, "Entre 30 y 60 minutos": 2,
                                "Entre 1 y 3 horas": 3, "Más de 3 horas": 4},
    "ESTU_HORASSEMANATRABAJA": {"0": 0, "Menos de 10 horas": 1, "Entre 11 y 20 horas": 2,
                                "Entre 21 y 30 horas": 3, "Más de 30 horas": 4},
    "COLE_BILINGUE": {"N": 0, "SIN DATOS": 1, "S": 2},
    "FAMI_TIENECOMPUTADOR": {"No": 0, "Si": 1},
    "ESTU_GENERO": {"F": 1, "M": 0},
    "COLE_NATURALEZA": {"OFICIAL": 0, "NO OFICIAL": 1},
    "COLE_AREA_UBICACION": {"URBANO": 1, "RURAL": 0},
    "COLE_CARACTER": {"SIN DATOS": 0, "NO APLICA": 1, "ACADÉMICO": 2, "TÉCNICO": 3, "TÉCNICO/ACADÉMICO": 4},
    "COLE_JORNADA": {"COMPLETA": 5, "MAÑANA": 2, "NOCHE": 1, "SABATINA": 0, "TARDE": 3, "UNICA": 4}
}


def predecir(variables, calendario):
    load_rf_model = get_classification_model(calendario)
    df = pd.DataFrame(variables)
    df = df.replace(ordinal_data)
    df = df[obtener_orden_columnas()]
    return load_rf_model.predict(df)
