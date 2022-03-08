mais18 = homens = mulheres = mais18 = 0
while True:
    print('-'*30,'\nCADASTRE UMA PESSOA','\n','-'*30)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()[0]
    print('-'*30)
    flag = input('Quer continuar? [S/N] ').upper()[0]
    print('-'*30)
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        mulheres += 1
    if flag == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {homens} homens cadastrados
E temos {mulheres} mulheres com menos de 20 anos''')