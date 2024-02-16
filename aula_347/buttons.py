from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setCheckable(True)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''

        self.equation = 'Qualquer coisa'
        self._makeGrid()
    
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation
        self.info.setText(value)

    def _makeGrid(self):
        for row_number , row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                #print('Linha', row_number, 'Coluna', column_number, button_text)
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertButtonTextToDisplay,button,)
                button.clicked.connect(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        print(f'Texto do botão especial: ', text)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self,button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return 

        self.display.insert(buttonText)
