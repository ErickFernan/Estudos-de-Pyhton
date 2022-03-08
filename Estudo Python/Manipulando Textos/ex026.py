frase = input('Digite uma frase: ').lower().strip(' ')
print('A letra "A" aparece {} vezes.'.format(frase.count('a')))
print('A letra "A" aparece a primeira vez em {}.'.format(frase.find('a')+1))
print('A última letra a aparece por ultimo em {}'.format(frase.rfind('a')+1))