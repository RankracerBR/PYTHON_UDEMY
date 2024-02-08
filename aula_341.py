from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout, QMainWindow
import sys

def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita :3')

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')
botao.show() #adiciona o widget na Hierarquia e exibe a janela

botao2 = QPushButton('Botão 2')
botao.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1 , 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = primeiro_menu.addAction('Primeira Ação')
primeira_acao.triggered.connect(lambda sb: slot_example(status_bar))

window.show() 
app.exec() # Loop da aplicação