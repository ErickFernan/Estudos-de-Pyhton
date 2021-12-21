cidade = input('Digite o nome da sua cidade: ')
PNC = cidade.lower().split()
print(PNC[0])
print('Sua cidade começa com a palavra santo? {}'.format('santo' in PNC[0]))