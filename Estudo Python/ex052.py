soma = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    resto = n % c
    if resto == 0:
        soma += 1
        print('\033[33m{}\033[m'.format(c), end=" ")
    else:
        print('\033[31m{}\033[m'.format(c), end=" ")
print('\nO número {} foi divisível {} vezes'.format(n, soma))
print('E por isso ele ', end='')
if soma > 2:
    print('NÃO É PRIMO!')
else:
    print('É PRIMO!')
