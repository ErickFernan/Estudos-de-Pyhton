jogadores = list()
dados = dict()
gols = list()

while True:
    gols.clear()
    dados['Nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    jogadores.append(dados.copy())
    continua = input('Quer continuar? [S/N] ').upper()
    if continua == 'N':
        print('-=' * 30)
        break
print(jogadores)
print(f'{"Cod ":<4}{"Nome":<15}{"Gols":<15}{"Total":<5}')
print('-' * 40)
for i, v in enumerate(jogadores):
    print(f'{i:>3}{" "}{v["Nome"]:<15}{str(v["Gols"]):<15}{v["Total"]:<5}')
print('-' * 40)
flag = 0
while flag != 999:
    flag = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if flag != 999:
        if flag < len(jogadores):
            print(f'LEVANTAMENTO DO JOGADOR {jogadores[flag]["Nome"]}')
            for i in range(0, len(jogadores[flag]["Gols"])):
                print(f'No jogo {i+1} fez {jogadores[flag]["Gols"][i]} gols')
        else:
            print(f'ERRO! Não existe jogador com código {flag}!')
            print('-=' * 30)
print('<<< VOLTE SEMPRE >>>')