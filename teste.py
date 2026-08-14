import tkinter as tk
from tkinter import messagebox

def tentar_cadastrar():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    senha = entry_senha.get().strip()
 
    # Validações simples
    if not nome or not email or not senha:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return  # Continua na mesma tela para tentar de novo

    if "@" not in email:
        messagebox.showerror("Erro", "E-mail inválido!")
        return

    if len(senha) < 6:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres!")
        return

    # Se chegou aqui, deu certo
    messagebox.showinfo("Sucesso", f"Matrícula realizada com sucesso!\nBem-vindo(a), {nome}!")
    # Aqui você pode fechar a janela ou limpar os campos
    # janela.destroy()  # se quiser fechar
    limpar_campos()     # ou limpar para um novo cadastro

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_nome.focus()  # volta o foco pro primeiro campo

# Janela principal
janela = tk.Tk()
janela.title("Matrícula / Cadastro")
janela.geometry("350x250")
janela.resizable(False, False)

# Labels e campos
tk.Label(janela, text="Nome:").pack(pady=(15, 0))
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

tk.Label(janela, text="E-mail:").pack(pady=(10, 0))
entry_email = tk.Entry(janela, width=30)
entry_email.pack()

tk.Label(janela, text="Senha:").pack(pady=(10, 0))
entry_senha = tk.Entry(janela, width=30, show="*")
entry_senha.pack()

# Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar", command=tentar_cadastrar, width=12)
btn_cadastrar.pack(side=tk.LEFT, padx=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar / Tentar de novo", command=limpar_campos, width=18)
btn_limpar.pack(side=tk.LEFT, padx=5)

# Tecla Enter também tenta cadastrar
janela.bind("<Return>", lambda event: tentar_cadastrar())

janela.mainloop()