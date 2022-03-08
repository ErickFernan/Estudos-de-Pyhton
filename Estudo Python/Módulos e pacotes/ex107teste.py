from ex107 import moeda, dados

#p = float(input('Digite um preço: R$ '))
# print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p, True))}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
# print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
# print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
p = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 80, 5)
