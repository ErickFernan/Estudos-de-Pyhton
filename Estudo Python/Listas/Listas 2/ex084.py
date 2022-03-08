pessoas = []
npess = maior = 0
while True:
    cadastro = [input('Nome: '), float(input('Peso: '))]
    pessoas.append(cadastro)
    cont = input('Quer continar? [S/N] ').upper()
    if cont != 'S':
        break
print(pessoas)
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
menor = pessoas[0][1]
#PEGAR O MAIOR  E MENOR PESO
for n in range(1, len(pessoas)):
    if maior < pessoas[n][1]:
        maior = pessoas[n][1]
    if menor > pessoas[n][1]:
        menor = pessoas[n][1]
print(f'O maior peso foi de {maior} Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor} Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')