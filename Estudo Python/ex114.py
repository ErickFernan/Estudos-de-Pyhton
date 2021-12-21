# import webbrowser
# try:
#     webbrowser.open('http://pudim.com.br', new = 2)
#     print('tá suave')
# except:
#     print('não rolou')

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Deu erro')
else:
    print('Tudo certo')