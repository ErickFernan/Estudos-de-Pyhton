pessoa = {}
pessoa['Nome'] = input('Nome: ')
pessoa['Média'] = float(input(f'Media de {pessoa["Nome"]}: '))
if pessoa['Média'] >= 7:
    pessoa['Situação'] = 'Aprovado'
elif 5 <= pessoa['Média'] < 7:
    pessoa['Situação'] = 'Recuperação'
else:
    pessoa['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in pessoa.items():
    print(f' - {k} é igual a {v}')

