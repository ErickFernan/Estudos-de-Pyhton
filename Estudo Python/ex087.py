matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for j in range(0, 3):
        matriz[c][j] = int(input(f'Digite um valor para [{c}, {j}]: '))
print('-='*30)
#print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
for c in range(0, 3):
    for j in range(0,3):
        print(f'[{matriz[c][j]:^5}]',end='')
    print()
print('-='*30)
somatot = 0
for c in range(0, 3):
    for j in range(0,3):
        if matriz[c][j] % 2 == 0:
         somatot += matriz[c][j]
print(f'A soma do valores pares é {somatot}.')
soma3col = 0
for c in range(0, 3):
        soma3col += matriz[c][2]
print(f'A soma  dos valores da terceira coluna é {soma3col}.')
maior2l = 0
for c in range(0, 3):
    if matriz[1][c] > maior2l:
        maior2l = matriz[1][c]
print(f'O maior valor da segunda linha é {maior2l}.')