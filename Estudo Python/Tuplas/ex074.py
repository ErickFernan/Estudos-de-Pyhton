from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram:', end=' ')
for cada in num:
    print(cada, end=' ')
print(f'\nO maior valor sorteado foi: {sorted(num)[-1]}')
print(f'O menor valor sorteado foi: {sorted(num)[0]}')
print(f'\nO maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')