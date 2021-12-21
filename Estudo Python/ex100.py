from random import randint


def sorteia(lista):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for n in range(0, 5):
        sort = randint(0, 10)
        print(f'{sort}', end=' ')
        lista.append(sort)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    print(f'Somando os valores pares de {lista}, temos', end=' ')
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma)


numeros = list()
sorteia(numeros)
somapar(numeros)
