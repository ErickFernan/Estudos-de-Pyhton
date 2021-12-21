media = 0
idade_ant = 0
idadefinal = 0
n = 0

for c in range(0, 4):
    print('_'*5 ,'{}ª PESSOA '.format(c+1), '_'*5)
    nome = input('Nome: ')
    idade = float(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower()
    media += idade/4
    if idade > idade_ant:
        maisvelho = nome
        idadefinal = idade
    idade_ant = idade
    if sexo == 'f' and idade < 20:
            n += 1

print("""A média de idade do grupo é de {} anos.
O homem mais velho tem {:.0f} anos e se chama {}.
Ao todo são {} mulheres com menos de 20 anos.
""".format(media,idadefinal,maisvelho,n))