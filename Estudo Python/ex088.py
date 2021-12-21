from random import randint
from time import sleep
jogos = []
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f"SORTEANDO {njogos} JOGOS":-^30}')
for c in range(0, njogos):
    jogos.append([])
    while len(jogos[c]) < 6:
        n = randint(1, 60)
        if n not in jogos[c]:
            jogos[c].append(n)
    jogos[c].sort()
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
print(f'{"BOA SORTE!":-^30}')