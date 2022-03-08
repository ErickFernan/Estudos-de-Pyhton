def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mErro! Por favor digite um número inteiro válido.\033[m')
            continue
        return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for l, v in enumerate(lista):
        print(f'\033[1;33m{l+1}\033[m - \033[1;34m{v}\033[m')
    print(linha())
    opc = leiaInt('\033[1;33mSua Opção: \033[m')
    return opc
