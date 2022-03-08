from ex115.lib2.interface import *
from ex115.lib2.Arquivo import *
from time import sleep

arq = 'cursoemvídeo.txt'
if not arquivoExiste(arq):
      criarArquivo(arq)

while True:
      resposta = menu(['Ver pessoas cadastradas',
                       'Cadastrar nova Pessoa',
                       'Sair do Sistema'])
      if resposta == 1:
            #Listar cadastro
            lerArquivo(arq)
      elif resposta == 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
      elif resposta == 3:
            cabecalho('Saindo do sistema... Até logo!')
            break
      else:
            print('\033[31mDigite uma opção válida!\033[m')
      sleep(2)
