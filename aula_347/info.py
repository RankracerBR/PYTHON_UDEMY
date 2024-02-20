from PySide6.QtWidgets import QLabel, QWidget
from variables import SMALL_FONT_SIZE
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configstyle()

    def configstyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)