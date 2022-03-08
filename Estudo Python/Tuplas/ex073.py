times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-GO')
epç = '-=' * 15
print(epç)
print(f'Lista de times do Brasileirão: {times}')
print(epç)
print(f'Os 5 primeiros sã0: {times[:5]}')
print(epç)
print(f'Os 4 últimos são: {times[-4:]}')
print(epç)
print(f'Times em ordem alfabética: {sorted(times)}')
print(epç)
pos = times.index('Chapecoense') + 1
print(f'O Chepecoense está na {pos}ª posição')
