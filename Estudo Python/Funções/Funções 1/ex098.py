from time import sleep


def contador(ini, fim, passo):
    if passo < 0:
        passo = -passo
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if ini < fim:
        while ini <= fim:
            print(f'{ini}', end=' ')
            ini += passo
            sleep(0.5)
        print('FIM!')
    else:
        while fim <= ini:
            print(f'{ini}', end=' ')
            ini -= passo
            sleep(0.5)
        print('FIM!')


# Início
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
