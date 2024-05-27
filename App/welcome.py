import sys
from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QFont

class WelcomeMessage(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        self.setWindowTitle('Bienvenido')
        self.setGeometry(100, 100, 350, 250)
        self.generar_mensaje()
        self.show()

    def generar_mensaje(self):
        mensaje_wl = QLabel('¡Bienvenido!', self)
        mensaje_wl.setFont(QFont('Arial', 20))
        mensaje_wl.move(100, 100)
        mensaje_description = QLabel('Esta es una app donde puedes hacer tu\ncodigo de manera visual!', self)
        mensaje_description.setFont(QFont('Arial', 12))
        mensaje_description.move(50, 150)