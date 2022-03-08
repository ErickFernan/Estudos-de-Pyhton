from time import sleep


def intro():
    print('\033[0;30;41m~' * 40)
    print(f'{"SISTEMA DE AJUDA PyHELP":^40}')
    print('~' * 40)
    print('\033[m',end='')

def ajuda(txt):
    print('\033[0;30;46m~' * 40)
    texto = (f'Acessando o manual do comando {txt}')
    print(f'{texto:^40}')
    print('~' * 40)
    print('\033[m', end='')
    sleep(1)
    print('\033[0;30;43m', end='')
    print(help(txt))
    print('\033[m', end='')


while True:
    intro()
    cmd = input('Função ou Biblioteca > ')
    if cmd.upper() == 'FIM':
        print('\033[0;30;46mATÉ LOGO!')
        break
    ajuda(cmd)

