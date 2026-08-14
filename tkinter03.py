from tkinter  import *  
from tkinter import messagebox

def tente_denovo():
    nome_copleto =  entry_nome.get().strip()
    data_nasimento = data.get().strip()
    cpf = cpf_pri.get().strip()

    if not nome_copleto or not data_nasimento or not cpf :
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return 
    if 9 > len(data_nasimento) or 11 < len(data_nasimento) :
         messagebox.showerror("Erro", "Preencha a data!")
         return 
    if 10 > len(cpf) or 12 < len(cpf):
        messagebox.showerror("Erro", "Preencha o cpf!")
        return

    messagebox.showinfo("Sucesso", f"Matrícula realizada com sucesso!\nBem-vindo(a), {nome_copleto}!")

    limpar_campos()


def limpar_campos():
    entry_nome.delete(0, END)
    data.delete(0, END)
    cpf_pri.delete(0, END)
    entry_nome.focus()

janela = Tk()
janela.title("matricula")
janela.geometry("300x500")
janela.resizable(False, False)

Label(janela, text="Nome complerto:").pack(pady=(15, 0))
entry_nome = Entry(janela, width=30)
entry_nome.pack()

Label(janela, text="data de nasimento").pack(pady=(10, 0))
data = Entry(janela, width=30)
data.pack()

Label(janela, text="CPF").pack(pady=(10, 0))
cpf_pri = Entry(janela, width=30)
cpf_pri.pack()

fleme_botao = Frame(janela)
fleme_botao.pack(pady=20)

cadastrar =Button(fleme_botao, text="Cadastrar", command=tente_denovo, width=12)
cadastrar.pack(side=LEFT , padx=5)

limpar = Button(fleme_botao, text="Limpar / Tentar de novo", command=limpar_campos, width=18)
limpar.pack(side=LEFT, padx=5)


janela.bind("<Return>", lambda event: tente_denovo())





janela.mainloop()


