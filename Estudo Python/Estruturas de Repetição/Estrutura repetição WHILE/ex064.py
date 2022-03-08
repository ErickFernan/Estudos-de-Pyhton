cont = num = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {} e a soma entre eles foi {}'.format(cont,soma))
