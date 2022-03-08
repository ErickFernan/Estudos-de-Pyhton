frase = input('Digite uma frase: ').upper()
frase = frase.replace(' ','')
inverso = frase[::-1]
cont = 0
print('O inverso de {} é {}'.format(frase,inverso))
for c in range(0, len(frase)):
    if frase[c] == inverso[c]:
        cont += 1
if cont == len(frase):
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
