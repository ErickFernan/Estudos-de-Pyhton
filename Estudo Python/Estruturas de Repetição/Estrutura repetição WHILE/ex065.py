continua = 'S'
cont = 1
n = int(input('Digite um número: '))
maior = menor = dividendomedia = n
continua = input('Quer contiuar? [S/N] ').upper().strip()[0]
while continua == 'S':
    n = int(input('Digite um número: '))
    continua = input('Quer contiuar? [S/N] ').upper().strip()[0]
    cont += 1
    dividendomedia += n
    if (maior - n) < 0:
        maior = n
    if (menor - n) > 0:
        menor = n
print('''Você digitou {} números e a média foi {}
O maior valor foi {} e o menor foi {}'''.format(cont, dividendomedia/cont, maior, menor))
