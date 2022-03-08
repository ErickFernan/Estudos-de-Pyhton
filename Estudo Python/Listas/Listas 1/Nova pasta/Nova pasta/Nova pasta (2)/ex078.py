valores = []
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print('=-'*30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições',end=' ')
for c, val in enumerate(valores):
    if val == max(valores):
        print(f'{c}',end='...')
print(f'\nO menor valor digitado foi {min(valores)} nas posições',end=' ')
for c, val in enumerate(valores):
    if val == min(valores):
        print(f'{c}',end='...')