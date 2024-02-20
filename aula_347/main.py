from PySide6.QtWidgets import (QApplication,QLabel)
from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from PySide6.QtGui import QIcon
from display import Display
from info import Info
from styles import setuptheme
from buttons import Button, ButtonsGrid
import sys

def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size: 150px;')
    return label1

if __name__ == '__main__':
    # snake_case
    # PascalCase
    # camelCase

    # Cria a aplicação
    app = QApplication(sys.argv)
    setuptheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua Conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsgrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsgrid)
    
    # Exec
    window.adjustFixedSize()
    window.show()
    app.exec()