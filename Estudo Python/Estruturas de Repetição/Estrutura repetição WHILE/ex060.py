cont = 1
fat = 1

n = int(input('Digite um número para'
              'calcular seu Fatorial: '))
print('Calculando {}! = '.format(n),end=' ')

while cont < n+1:
    fat = fat * cont
    cont += 1
    if cont < n+1:
        print(cont-1 , 'x', end=' ')
    else:
        print(cont-1 , '=', end=' ')
print(fat)
