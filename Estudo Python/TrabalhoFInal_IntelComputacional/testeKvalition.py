import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn import neural_network
from sklearn.metrics import confusion_matrix

# IMPORTANDO O DATASET
BD = pd.read_csv('C:/Users/erick/Documents/Estudo Python/trabfinalIC/fertility_Diagnosis.csv', header=None)
saida = pd.read_csv('C:/Users/erick/Documents/Estudo Python/trabfinalIC/saidas.csv', header=None)
saida = saida.values
saida.shape = (100,)
del BD[9]


new_BD = BD.values
print(new_BD)
print(saida)

# Técnica Houldout
x_train, x_test, y_train, y_test = train_test_split(new_BD, saida, test_size=0.3)

# Classificador 1 - SVM
clf = svm.SVC(gamma='auto')

# TREINO SVM
clf.fit(x_train, y_train)

# ATIVA O MODELO


print(clf.score(x_test, y_test)) # me retorna a acuracia?????d

print(clf.decision_function_shape)
# Cross Validation com 10 folds

scores = cross_val_score(clf, new_BD, saida, cv=10, scoring='accuracy')
scores2 = cross_val_score(clf, new_BD, saida, cv=10, scoring='average_precision')

print(scores)
print(scores2)

# Média dos resultados
print(scores.mean())


print(confusion_matrix(y_test, y_test))
