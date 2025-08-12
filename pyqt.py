from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
#----------------------------------------------------------------------------------------------
def login():
    janela = QWidget() #mudar nome de janela para janela_login
    janela.resize(310, 350)
    janela.setStyleSheet("background-color: lightblue;")
    janela.setWindowTitle("Login")
    #----------------------------------------------------------------------------------------------
    layout = QVBoxLayout()

    titulo = QLabel("LOGIN")
    titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
    layout.addWidget(titulo)
    #----------------------------------------------------------------------------------------------
    linha = QFrame()
    linha.setFrameShape(QFrame.Shape.HLine)
    linha.setStyleSheet("color: blue; background-color: blue; height: 2px;")
    layout.addWidget(linha)
    #----------------------------------------------------------------------------------------------
    layout.addSpacing(25)

    email = QLineEdit()
    email.setPlaceholderText("Email")
    email.setStyleSheet("background-color: white;")
    layout.addWidget(email)
    #----------------------------------------------------------------------------------------------
    layout.addSpacing(20)

    senha = QLineEdit()
    senha.setPlaceholderText("Senha")
    senha.setEchoMode(QLineEdit.EchoMode.Password)
    senha.setStyleSheet("background-color: white;")
    layout.addWidget(senha)
    #----------------------------------------------------------------------------------------------
    layout.addSpacing(120)


    def verificar(): # mudar nome de verificar para verificar_login
        if email.text() == "" or senha.text() == "":
            QMessageBox.warning(janela, "Erro", "O campo não pode estar vazio!")
        else:
            janela.close()
            entrada()

    botao_login = QPushButton("Entrar")
    botao_login.setStyleSheet("background-color: skyblue;")
    botao_login.clicked.connect(verificar)
    layout.addWidget(botao_login)

    botao_cadastro = QPushButton("Não tenho cadastro")
    botao_cadastro.setStyleSheet("background-color: skyblue;")
    botao_cadastro.clicked.connect(abrir_janela_cadastro)
    layout.addWidget(botao_cadastro)

    janelas_abertas.append(janela)
    #----------------------------------------------------------------------------------------------

    janela.setLayout(layout)
    janela.show()


def abrir_janela_cadastro():
    janela_cadastro = QWidget()
    janela_cadastro.setWindowTitle("Cadastro")
    janela_cadastro.resize(310, 350)
    janela_cadastro.setStyleSheet("background-color: lightblue;")
#----------------------------------------------------------------------------------------------
    layout_cadastro = QVBoxLayout()

    titulo = QLabel("CADASTRO")
    titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
    layout_cadastro.addWidget(titulo)
#----------------------------------------------------------------------------------------------

    linha = QFrame()
    linha.setFrameShape(QFrame.Shape.HLine)
    linha.setStyleSheet("color: blue; background-color: blue; height: 2px;")
    layout_cadastro.addWidget(linha)
#----------------------------------------------------------------------------------------------
    layout_cadastro.addSpacing(20)

    nome_completo = QLineEdit()
    nome_completo.setPlaceholderText("Nome completo")
    nome_completo.setStyleSheet("background-color: white;")
    layout_cadastro.addWidget(nome_completo)
#----------------------------------------------------------------------------------------------
    layout_cadastro.addSpacing(25)

    email = QLineEdit()
    email.setPlaceholderText("Email")
    email.setStyleSheet("background-color: white;")
    layout_cadastro.addWidget(email)
#----------------------------------------------------------------------------------------------
    layout_cadastro.addSpacing(25)

    senha = QLineEdit()
    senha.setPlaceholderText("Senha")
    senha.setEchoMode(QLineEdit.EchoMode.Password)
    senha.setStyleSheet("background-color: white;")
    layout_cadastro.addWidget(senha)
#----------------------------------------------------------------------------------------------
    
    def verificar_cadastro():
        if nome_completo.text() == "" or email.text() == "" or senha.text() == "":
            QMessageBox.warning(janela_cadastro, "Erro", "O campo não pode estar vazio!")
        else:
            janela_cadastro.close()
            login()
    
    layout_cadastro.addSpacing(25)


    botao_cadastrar = QPushButton("Cadastrar")
    botao_cadastrar.setStyleSheet("background-color: skyblue;")
    layout_cadastro.addWidget(botao_cadastrar)
    botao_cadastrar.clicked.connect(verificar_cadastro)
#----------------------------------------------------------------------------------------------

    janela_cadastro.setLayout(layout_cadastro)
    janela_cadastro.show()

    janelas_abertas.append(janela_cadastro)
#----------------------------------------------------------------------------------------------

def entrada():
    janela_entrada = QWidget()
    janela_entrada.setWindowTitle("Você entrou!!!")
    janela_entrada.resize(310, 350)
    janela_entrada.setStyleSheet("background-color: lightblue;")

    layout_entrada = QVBoxLayout()
#----------------------------------------------------------------------------------------------
    texto = QLabel("Você entrou com sucesso!")
    texto.setAlignment(Qt.AlignmentFlag.AlignCenter)
    texto.setStyleSheet("font-size: 18px; font-weight: bold;")
    layout_entrada.addWidget(texto)

    janela_entrada.setLayout(layout_entrada)
    janela_entrada.show()

    janelas_abertas.append(janela_entrada)
#----------------------------------------------------------------------------------------------



app = QApplication([])

janelas_abertas = []

login()

app.exec()
