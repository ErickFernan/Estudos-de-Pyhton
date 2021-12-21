lista = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    lista.append([nome, [n1, n2], media])
    resposta = input('Quer continuar? [S/N] ')
    if resposta in 'Nn':
        print('-=' * 30)
        break
print(f'{"Nº.":<4}{"NOME":<15}{"MÉDIA":<8}')
print('-'*27)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<15}{a[2]:<8.1f}')
print('-' * 27)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
        print('-' * 27)