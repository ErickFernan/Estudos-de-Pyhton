n = int(input('Escreva um número inteiro: '))
base = input('Escreva a base para conversão: ')
if base == 'binário':
    print(bin(n))
elif base == 'octal':
    print(oct(n))
else:
    print(hex(n))