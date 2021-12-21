from random import randint
count = 1;
print('''Sou seu computador...
Acabei de pensar em um Nº entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
n = randint(0, 10)
#print(n)
tenta = int(input('Qual o seu palpite? '))
while tenta != n:
    count += 1
    if tenta < n:
        print('Mais... Tente mais uma vez.')
        tenta = int(input('Qual é seu palpite? '))
    elif tenta > n:
        print('Menos... Tente mais uma vez.')
        tenta = int(input('Qual é seu palpite? '))

print('Acertou com {} tentativas. Parabéns!'.format(count))
