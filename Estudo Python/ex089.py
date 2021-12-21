lista = []
cont = flag = 0
notas = []
while True:
    lista.append([])
    lista[cont].append(input('Nome: '))
    lista[cont].append(float(input('Nota 1: ')))
    lista[cont].append(float(input('Nota 2: ')))
    continuar = input('Quer continuar? [S/N] ').lower()
    cont += 1
    if continuar == 'n':
        print('-='*30)
        break
print(f'{"Nº.":<4}{"NOME":<15}{"MÉDIA":<8}')
print('-'*27)
for c in range(0, len(lista)):
    print(f'{c:<4}{lista[c][0]:<15}{((lista[c][1])+(lista[c][2]))/2:<8}')
print('-'*27)
while flag != 999:
    aluno = input('Mostrar notas de qual aluno? (999 interrompe): ')
    if aluno == '999':
        break
    else:
        for c in range(0,len(lista)):
            if aluno == lista[c][0]:
                notas = [lista[c][1], lista[c][2]]
                break
    print(f'Notas de {aluno} são: {notas}')
    print('-' * 27)
print('FINALIZANDO...\n <<< VOLTE SEMPRE >>>')
