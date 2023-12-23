import random
from tkinter import *
from tkinter import font




def jogar():
    escolha = escolha_jog.get()
    jogador = Label(frame_baixo, text="Qual a sua escolha? Pedra, Papel ou Tesoura?")
    jogador.grid(column =1, row=5)
    oponente = random.choice(['Pedra', 'Papel', 'Tesoura'])
    if jogador == oponente:
        return 'empate'
    
    if vitoria(jogador, oponente):
        return 'Você Venceu'
    else:
        return 'Você Perdeu'


def vitoria(jogador, oponente):
    if (jogador == 'pedra' and oponente == 'Tesoura') or (jogador == 'tesoura' and oponente == 'Papel') or (jogador == 'papel' and oponente == 'Pedra'):
        return True


janela = Tk()
frame_cima = Frame(janela)
frame_meio = Frame(janela)
frame_baixo = Frame(janela)
janela.geometry("400x400")
janela.title("Pedra, Papel e Tesoura")
janela.configure(background='black')
frame_baixo.configure(background='black')

texto1 = Label(frame_cima, text='Jogo Pedra, Papel, Tesoura')
texto1.configure(font=("Times New Roman", 16, "italic", "bold"), background=('white'), width=33,height=2)
texto1.grid(column=1, row=1)

texto2 = Label(frame_meio, text='Faça a sua escolha\n Pedra, Papel ou Tesoura?', background="black", foreground='white')
texto2.configure(font=("Arial", 15, 'bold'), pady=15)
texto2.grid(column=1, row=2)

escolha_jog = Entry(frame_baixo, width=40)
escolha_jog.grid(column=1, row=1, pady=40)

resultado = Button(frame_baixo, text="Enviar", width=20, command=jogar)
resultado.grid(column=1, row=2, pady= 2)

texto1.pack(side='top')
texto2.pack(side='top')

frame_cima.pack()
frame_meio.pack()
frame_baixo.pack()

janela.mainloop()