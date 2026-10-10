import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def funcao1():
    label.setText("botão 1 precionado")
    label.adjustSize()

def funcao2():
    label.setText("botão 2 precionado")
    label.adjustSize()
 
def funcao3():
    valor_lido = le.text()
    print(valor_lido)
app = QApplication(sys.argv)

#Configurando uma janela
janela = QWidget()
janela.resize(800,600)
janela.setWindowTitle("Controle orçamentario")

#Configurando um botão que ira aparecer na janela e criando uma função para alterar uma label
botao = QPushButton("Botão 1",janela)
botao.setGeometry(100,100,150,80)
botao.setStyleSheet("background-color:black;color:orange")
botao.clicked.connect(funcao1)

botao2 = QPushButton("Botão 2",janela)
botao2.setGeometry(100,300,150,80)
botao2.setStyleSheet("background-color:black;color:orange")
botao2.clicked.connect(funcao2)

botao3 = QPushButton("Botão 2",janela)
botao3.setGeometry(100,400,150,80)
botao3.clicked.connect(funcao3)

#Criando um campo de texto
le = QLineEdit("",janela)
le.setGeometry(500,300,150,40)

#Configurando uma label
label = QLabel("Texto",janela)
label.move(400,100)
label.setStyleSheet("font-size:30px")

#executa as configuração de interface
janela.show()

#Inicia a aplicação
app.exec()