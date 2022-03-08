print('Gerador de PA')
print('-='*10)
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
total = 10
PA = n
cont = 1
print(PA,'→',end=' ')
while cont < 10:
    PA += r
    print(PA,'→',end=' ')
    cont += 1
print('PAUSA')

while cont != 0:
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    cont = 0
    total += termos
    while cont < termos:
        PA += r
        print(PA,'→',end=' ')
        cont += 1
    if termos != 0:
        print('PAUSA')
print('Progressão finalizada com {} termos mostrados.'.format(total))