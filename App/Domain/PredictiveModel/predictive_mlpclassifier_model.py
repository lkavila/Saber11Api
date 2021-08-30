from App.Infrastructure.Repository.get_data import df_20191
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy

df_20191 = df_20191()

ground_truth = df_20191[["PUNT_GLOBAL"]].values
lookupTable, ground_truth = numpy.unique(ground_truth, return_inverse=True)
y = ground_truth
resultados = ['PUNT_LECTURA_CRITICA',
'PERCENTIL_LECTURA_CRITICA',
'DESEMP_LECTURA_CRITICA',
'PUNT_MATEMATICAS',
'PERCENTIL_MATEMATICAS',
'DESEMP_MATEMATICAS',
'PUNT_C_NATURALES',
'PERCENTIL_C_NATURALES',
'DESEMP_C_NATURALES',
'PUNT_SOCIALES_CIUDADANAS',
'PERCENTIL_SOCIALES_CIUDADANAS',
'DESEMP_SOCIALES_CIUDADANAS',
'PUNT_INGLES',
'PERCENTIL_INGLES',
'DESEMP_INGLES',
'PUNT_GLOBAL',
'PERCENTIL_GLOBAL']
#col = df_20191.columns.delete(0)
#X = df_20191[col].values
X = df_20191.drop(resultados, axis=1)
X.shape

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=1970)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=[4, 16], random_state=1000, max_iter=400)
clf.fit(X_train, y_train)
y_predicho = clf.predict(X_test)
presicion = accuracy_score(y_test, y_predicho)
print("valores reales:   ", y_test)
print("valores predecidos", y_predicho)
print("porcentaje de presición", presicion)
