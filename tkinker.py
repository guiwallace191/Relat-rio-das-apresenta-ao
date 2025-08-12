from tkinter import *
from tkinter import messagebox

def entrada():
    Início = Tk() #mudar nome de janela para janela_início
    Início.geometry('310x350')
    Início.title("Início")
    Início.configure(bg="lightblue")
    mensagem = Label(Início, text="Bem-vindo à tela inicial!", font=("Arial", 16), bg="Skyblue")
    mensagem.pack(pady=(50, 0))
    Início.mainloop()

def cadastro():
    janela_cadastrar = Tk()
    janela_cadastrar.geometry('310x350')
    janela_cadastrar.title("Cadastro")
    janela_cadastrar.configure(bg="lightblue")
    titulo = Label(janela_cadastrar, text="CADASTRO", bg="lightblue", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    linha = Frame(janela_cadastrar, height=2, bg="blue")
    linha.pack(fill="x", padx=20, pady=10)

    frame_nome = Frame(janela_cadastrar)
    frame_nome.pack(fill="x", padx=20)
    nome = Label(frame_nome, text="Nome e sobrenome", font=("Arial", 12, "bold"))
    nome.pack(anchor="w")

    texto_nome = Entry(janela_cadastrar, width=50)
    texto_nome.pack(padx=20)

    frame_email = Frame(janela_cadastrar)
    frame_email.pack(fill="x", padx=20, pady=(20, 0))
    email = Label(frame_email, text="Email", font=("Arial", 12, "bold"))
    email.pack(anchor="w")

    texto_email = Entry(janela_cadastrar, width=50)
    texto_email.pack(padx=20)

    frame_senha = Frame(janela_cadastrar)
    frame_senha.pack(fill="x", padx=20, pady=(20, 0))
    senha = Label(frame_senha, text="Senha", font=("Arial", 12, "bold"))
    senha.pack(anchor="w")

    texto_senha = Entry(janela_cadastrar, width=50, show="*")
    texto_senha.pack(padx=20, anchor="w")

    def verificar_cadastro():
        nome = texto_nome.get()
        email = texto_email.get()
        senha = texto_senha.get()      
        if nome == "" or email == "" or senha == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            janela_cadastrar.destroy()
            login()

    login_botao = Button(janela_cadastrar, text= "Login", bg = "skyblue", command=verificar_cadastro)
    login_botao.pack(padx= 20, pady=(20, 0))
    
    janela_cadastrar.mainloop()

def login():
    janela = Tk() #mudar nome de janela para janela_login
    janela.title("login")
    janela.geometry('310x350')
    janela.configure(bg="lightblue")

    titulo = Label(janela, text="LOGIN", bg="lightblue", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    linha = Frame(janela, height=2, bd=0, bg="blue")
    linha.pack(fill="x", padx=20, pady=10)

    frame_email = Frame(janela)
    frame_email.pack(fill="x", padx=20)
    email = Label(frame_email, text="Email", font=("Arial", 12, "bold"))
    email.pack(anchor="w")

    texto_email = Entry(janela, width=50)
    texto_email.pack(padx=20, anchor="w")

    frame_senha = Frame(janela)
    frame_senha.pack(fill="x", padx=20, pady=(45, 0))
    senha = Label(frame_senha, text="Senha", font=("Arial", 12, "bold"))
    senha.pack(anchor="w")

    texto_senha = Entry(janela, width=50, show="*")
    texto_senha.pack(padx=20, anchor="w")

    def verificar_login():
        email = texto_email.get()
        senha = texto_senha.get()
        if email == "" or senha == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            janela.destroy()
            entrada()
        

    
    entrar = Button(janela, text="Entrar", bg="skyblue", command=verificar_login)
    entrar.pack(padx=20, pady=(30, 0))

    sem_cadastro = Button(janela, text="Não tenho cadastro", bg="blue", font=("Arial", 12), fg="skyblue", command=cadastro)
    sem_cadastro.pack(padx=20, pady=(12, 0))

    janela.mainloop()

login()