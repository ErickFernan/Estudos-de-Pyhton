futebol = dict()
futebol['nome'] = input('Nome do jogador: ')
njogos = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
gols = list()
for n in range(0, njogos):
    ngols = int(input(f'Quantos gols na partida {n}? '))
    gols.append(ngols)
futebol['gols'] = gols
futebol['total'] = sum(gols)
print('=-' * 30)
print(futebol)
print('=-' * 30)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 30)
print(f'O jogador {futebol["nome"]} jogou {len(futebol["gols"])} partidas.')
for i, v in enumerate(futebol["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {futebol["total"]} gols.')
