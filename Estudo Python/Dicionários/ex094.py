lista = list()
cadastro = dict()
while True:
    cadastro['Nome'] = input('Nome: ').upper()
    while True:
        cadastro['Sexo'] = input('Sexo: [M/F] ').upper()
        if cadastro['Sexo'][0] not in 'MF':
            print('Por favor, digite apenas M ou F.')
        else:
            break
    cadastro['Idade'] = int(input('Idade: ').upper())
    while True:
        continua = input('Quer continuar? [S/N] ').upper()
        if continua[0] not in 'NS':
            print('ERRO! Responda apenas S ou N.')
        else:
            break
    lista.append(cadastro.copy())
    if continua in 'Nn':
        break
print(lista)
soma = 0
for i in range(0, len(lista)):
    soma += lista[i]['Idade']
media = soma/len(lista)
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos')
print('C) Lista das pessoas que estão acima da media:')
for i in lista:
    if i['Idade'] > media:
        print('    ', end='')
    for k, v in i.items():
        if i['Idade'] > media:
            print(f'{k} = {v}', end='; ')
    if i['Idade'] > media:
        print()
print('<<< ENCERRADO >>>')
