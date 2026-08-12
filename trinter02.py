from tkinter  import *  
from tkinter import messagebox

janela = Tk() # define o nome da variavel janela
janela.title("Minha primeira janela") # titulo da janela
janela.geometry("400x300") # tamanho da janela

Label(janela,text="Nome do Aluno").pack()
entrada_nome = Entry(janela)
entrada_nome.pack()

Label(janela,text="idade do aluno").pack()
entrada_idade = Entry(janela)
entrada_idade.pack()

Label(janela,text="Nome do curso do aluno").pack()
entrada_curso = Entry(janela)
entrada_curso.pack()

def cadastro():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    curso = entrada_curso.get()
    messagebox.showinfo("cadastro",f"Alunos: {nome}\n idade{idade}\ncurso:{curso}")

Button(janela,text="cadastrar",command=cadastro).pack()

janela.mainloop()
