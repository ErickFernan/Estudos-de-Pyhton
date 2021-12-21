import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

np.random.seed(5)

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
x_train, x_test, y_train, y_test = train_test_split(new_BD, saida, test_size=0.9)

clf = MLPClassifier(solver='sgd', hidden_layer_sizes=(3,), learning_rate_init=0.1, activation='logistic', max_iter=1500,
                    random_state=1)  # gradiente decrescente stocastico?
clf.fit(x_train, y_train)
y_pred = clf.predict_proba(x_test)
y_aux = np.argmax(y_pred, 1)
print(y_aux)
print(y_test)

teste = accuracy_score(y_test, y_aux)
print(teste)

print(confusion_matrix(y_test, y_aux))

scores = cross_val_score(clf, new_BD, saida, cv=5, scoring='accuracy')

print(scores)
print(scores.mean())