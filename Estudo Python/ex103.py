def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato')


# início:
print('-' * 20)
n = input('Nome do jogador: ')
g = input('Total de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)