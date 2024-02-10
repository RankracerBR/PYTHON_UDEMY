from PySide6.QtWidgets import (QApplication,QLabel)
from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from PySide6.QtGui import QIcon
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
    window = MainWindow()

    # Define o icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()