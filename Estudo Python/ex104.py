def leiaInt(msg):
    n = input(msg).strip()
    while n.isnumeric() is False:
        print('\033[0;30;41mERRO! Digite um número inteiro válido.\033[m')
        n = input(msg)
    return n


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
