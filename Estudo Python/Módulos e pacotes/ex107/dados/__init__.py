def leiaDinheiro(msg):
    v = str(input(msg).strip()).replace(',', '.')
    while v.isalpha():
        print(f'\033[0;30;41mERRO! "{v}" é um preço inválido.\033[m')
        v = input(msg).strip()
    return float(v)
