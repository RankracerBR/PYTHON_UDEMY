from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty
from variables import BIG_FONT_SIZE, MINIMUN_WIDTH, TEXT_MARGIN
from PySide6.QtCore import Qt, Signal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from buttons import Button
    from info import Info

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configstyle()

    def configstyle(self):
        margin = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margin)
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip() # .strip() remove os espaços da direita e da esquerda
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape]

        if isEnter:
            print('Enter pressionado, sinal emitido', type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()      

        if isDelete:
            print('Delete pressionado, sinal emitido', type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()       

        if isEsc:
            print('Esc pressionado, sinal emitido', type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()        
        # Não passar daqui
        if isEmpty(text):
            return event.ignore()
        
        print('Texto', text)