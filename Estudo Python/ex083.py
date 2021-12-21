pilha = []
expressao = str(input('Digite sua expressão: '))
for c in range(0, len(expressao)):
   if expressao[c] == '(':
       pilha.append('(')
   elif expressao[c] == ')':
       if len(pilha) > 0:
           pilha.pop()
       else:
           pilha.append(')')
           break
if len(pilha) == 0:
    print('Td certo')
else:
    print('Errouuu')