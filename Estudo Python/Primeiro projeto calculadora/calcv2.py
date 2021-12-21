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
janela.geometry('240x350')
janela.wm_iconbitmap('icone.ico')

# Dividindo em visor e comandos
quadro_visor = Frame(janela, width=240, height=50, bg=cinza)  # janela pra onde será criado o frame
quadro_visor.grid(row=0, column=0)

quadro_comandos = Frame(janela, width=240, height=300)
quadro_comandos.grid(row=1, column=0)

# criando botões
btn1 = Button(text='btn1')
btn2 = Button(text='btn2')
btn3 = Button(text='btn3')
btn4 = Button(text='btn4')
btn5 = Button(text='btn5')
quadro_comandos.rowconfigure((0,1), weight=1)  # make buttons stretch when
quadro_comandos.columnconfigure((0,2), weight=1)  # when window is resized
btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS')
btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
btn3.grid(row=1, column=0, columnspan=1, sticky='EWNS')
btn4.grid(row=1, column=1, columnspan=1, sticky='EWNS')
btn5.grid(row=1, column=2, columnspan=1, sticky='EWNS')

janela.mainloop()
