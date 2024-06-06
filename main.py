from App import WindowsMain
import sys
from PyQt6.QtWidgets import QApplication

# Main function
# Crear la ventana principal y mostrarla
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowsMain.MainWindow()
    window.show()
    sys.exit(app.exec())