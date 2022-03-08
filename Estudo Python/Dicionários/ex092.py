from datetime import datetime
cadastro = dict()
cadastro['nome'] = input('Nome: ')
nascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35 - nascimento
print('-=' * 30)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')