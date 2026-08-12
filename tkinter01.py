from tkinter  import *  
from tkinter import messagebox

janela = Tk() # define o nome da variavel janela
janela.title("Minha primeira janela") # titulo da janela
janela.geometry("400x300") # tamanho da janela

texto = Label(janela, text="bem-vindo ao Senai") # escrever algo na janela
texto.pack() # setar dentro da janela

texto2 = Label(janela, text="Pedro Henriqeu Ferras")
texto2.pack()

def saudacao():
    messagebox.showinfo("Aviso ","olá aluno")

Button(janela,text="clique aqui",command=saudacao).pack() # criar o botão

meu_nome = Entry(janela)
meu_nome.pack()

def  exibir_nome():
    nome = meu_nome.get()
    messagebox.showinfo("cadastro ",f"aluno {nome}")

Button(janela,text="exibir nome",command=exibir_nome).pack()

janela.mainloop()


