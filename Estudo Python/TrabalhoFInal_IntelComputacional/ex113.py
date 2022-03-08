def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mErro! Por favor digite um número inteiro válido.\033[m')
            continue
        return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[31mErro! Por favor digite um número real válido.\033[m')
            continue
        return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e  o real {n2}')
