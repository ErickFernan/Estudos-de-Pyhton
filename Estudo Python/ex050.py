soma = 0
for c in range(0, 6):
    num = int(input('Digite um n: '))
    if num % 2 == 0:
        soma += num
print('A soma foi: \033[32m{}\033[m'.format(soma))
