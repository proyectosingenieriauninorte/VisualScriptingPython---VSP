from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QApplication
from PyQt6.QtCore import Qt

class CustomBlock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(200, 100)

        # Crear los widgets
        self.label = QLabel("Etiqueta")
        self.button1 = QPushButton("Botón 1")
        self.button2 = QPushButton("Botón 2")

        # Crear los layouts
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)

        main_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        self.setStyleSheet("QWidget{background-color:Grey;}")

        self.setLayout(main_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear instancias de CustomBlock
        block1 = CustomBlock(self)

        # Crear el layout principal
        block1.move(200, 400)

        # Crear un widget central y establecer el layout principal

        self.setFixedSize(500, 1000)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
