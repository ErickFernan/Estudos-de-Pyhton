frase = 'Curso em Vídeo Python'

# Fatiamento
print(frase)
print(frase[3]) #4 letra
print(frase[3:13]) #4-13 letra
print(frase[:13]) #ini-13 letra
print(frase[13:]) #ini-13 letra
print(frase[1:15:2])
print(frase[::2])
print('''ushdauishduihasuidh
asiojhaisjioajs
auisouajisjoi
asiajsoajiosjoajsj
akja]aiosjoa''')

#No python td é objeto então pode-se fazer
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))

dividido = frase.split() # Cria uma lista
print(dividido[0])
print(dividido[2][3])


