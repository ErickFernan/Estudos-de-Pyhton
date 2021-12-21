n = int(input('Digite um nº inteiro: '))
print('\033[0;30;41mPar\033[m' if n % 2 == 0 else '\033[0;30;41mÍmpar\033[m' )