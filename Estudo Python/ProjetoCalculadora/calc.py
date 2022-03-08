# importando tkinter
from tkinter import *
from tkinter import ttk

# cores
preto = '#000000'
cinza = '#a3a3a3'
branco = '#ffffff'
azul = '#2c36c7'
laranja = '#ff5b03'

# Criando a janela
janela = Tk()
# janela['bg'] = preto
janela.config(bg=preto)
janela.title('Calculadora')
janela.geometry('240x240')
janela.wm_iconbitmap('icone.ico')

# Dividindo em visor e comandos
quadro_visor = Frame(janela, width=240, height=50, bg=cinza)  # janela pra onde será criado o frame
quadro_visor.grid(row=0, column=0)

quadro_comandos = Frame(janela, width=240, height=190)
quadro_comandos.grid(row=1, column=0)

todos_valores = str()  # Var todos os valores

valor_texto = StringVar()  # Var de inicialização


def entrar_valores(event):  # Fç para
    global todos_valores
    todos_valores += str(event)
    # print(todos_valores)

    valor_texto.set(todos_valores)  # Precisa usar o StringVar()


def resultado():
    mostra_resultado = eval(todos_valores)
    valor_texto.set(mostra_resultado)
    print(mostra_resultado)
    limpa_tela(1)


def limpa_tela(destino):
    global todos_valores
    todos_valores = ''
    if destino == 0:
        valor_texto.set(todos_valores)


# criando label para resultados
# label_visor = Label(quadro_visor, text='1234567890123456789', width=19, padx=7, relief=FLAT, anchor='e',
# justify=RIGHT, height=2,bg=azul, font='Ivi 16', fg=branco)

label_visor = Label(quadro_visor, textvariable=valor_texto, width=19, padx=7, relief=FLAT, anchor='e', justify=RIGHT,
                    height=2, bg=azul, font='Ivi 16', fg=branco)
label_visor.place(x=0, y=0)

# criando botões
b_C = Button(quadro_comandos, command=lambda: limpa_tela(0), text='C', width=16, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)  # Não usar () na função chamada? Descobrir motivo
b_C.place(x=0, y=0)
b_res = Button(quadro_comandos, command=lambda: entrar_valores('%'), text='%', width=8, height=2, font='Ivi 8 bold',
               relief=RAISED, overrelief=RIDGE)
b_res.place(x=120, y=0)
b_div = Button(quadro_comandos, command=lambda: entrar_valores('/'), text='/', width=8, height=2, bg=laranja, fg=branco,
               font='Ivi 8 bold', relief=RAISED, overrelief=RIDGE)
b_div.place(x=180, y=0)

b_7 = Button(quadro_comandos, command=lambda: entrar_valores('7'), text='7', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=38)
b_8 = Button(quadro_comandos, command=lambda: entrar_valores('8'), text='8', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_8.place(x=60, y=38)
b_9 = Button(quadro_comandos, command=lambda: entrar_valores('9'), text='9', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_9.place(x=120, y=38)
b_mul = Button(quadro_comandos, command=lambda: entrar_valores('*'), text='*', width=8, height=2, bg=laranja, fg=branco,
               font='Ivi 8 bold', relief=RAISED, overrelief=RIDGE)
b_mul.place(x=180, y=38)

b_4 = Button(quadro_comandos, command=lambda: entrar_valores('4'), text='4', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=76)
b_5 = Button(quadro_comandos, command=lambda: entrar_valores('5'), text='5', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=76)
b_6 = Button(quadro_comandos, command=lambda: entrar_valores('6'), text='6', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=76)
b_men = Button(quadro_comandos, command=lambda: entrar_valores('-'), text='-', width=8, height=2, bg=laranja, fg=branco,
               font='Ivi 8 bold', relief=RAISED, overrelief=RIDGE)
b_men.place(x=180, y=76)

b_4 = Button(quadro_comandos, command=lambda: entrar_valores('1'), text='1', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=114)
b_5 = Button(quadro_comandos, command=lambda: entrar_valores('2'), text='2', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=114)
b_6 = Button(quadro_comandos, command=lambda: entrar_valores('3'), text='3', width=8, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=114)
b_mai = Button(quadro_comandos, command=lambda: entrar_valores('+'), text='+', width=8, height=2, bg=laranja, fg=branco,
               font='Ivi 8 bold', relief=RAISED, overrelief=RIDGE)
b_mai.place(x=180, y=114)

b_0 = Button(quadro_comandos, command=lambda: entrar_valores('0'), text='0', width=16, height=2, font='Ivi 8 bold',
             relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=152)
b_pont = Button(quadro_comandos, command=lambda: entrar_valores('.'), text='.', width=8, height=2, font='Ivi 8 bold',
                relief=RAISED, overrelief=RIDGE)
b_pont.place(x=120, y=152)
b_igual = Button(quadro_comandos, command=lambda: resultado(), text='=', width=8, height=2, bg=laranja, fg=branco,
                 font='Ivi 8 bold', relief=RAISED, overrelief=RIDGE)
b_igual.place(x=180, y=152)

# inicializar
# calcular()
janela.mainloop()
