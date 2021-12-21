def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    if idade < 16:
        resposta = f'Com {idade} anos = Negado'
    elif 16 <= idade < 18 or idade >= 60:
        resposta = f'Com {idade} anos = Opicional'
    else:
        resposta = f'Com {idade} anos = Obrigatório'
    return resposta


# Início
anonasc = int(input('Qual seu ano de nascimento? '))
print(voto(anonasc))
