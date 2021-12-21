matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for j in range(0, 3):
        matriz[c][j] = int(input(f'Digite um valor para [{c}, {j}]: '))
print('-='*30)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
for c in range(0, 3):
    for j in range(0,3):
        print(f'[{matriz[c][j]:^5}]',end='')
    print()
