import sys
from PyQt6.QtCore import QPointF, Qt, QEvent
from PyQt6.QtGui import QPainterPath, QPen, QColor, QBrush, QPolygonF
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsPathItem, QGraphicsPolygonItem, QVBoxLayout, QWidget, QGraphicsItem, QGraphicsEllipseItem
from math import atan2, cos, sin, radians, degrees

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        # Crear un cuadrado
        self.square = QGraphicsRectItem(50, 50, 200, 200)
        self.square.setPen(QPen(Qt.GlobalColor.blue))
        self.scene.addItem(self.square)

        # Crear un círculo dentro del cuadrado
        self.circle = QGraphicsEllipseItem(100, 100, 100, 100)
        self.circle.setPen(QPen(Qt.GlobalColor.red))
        self.scene.addItem(self.circle)

        # Habilitar la detección de eventos de mouse en la vista
        self.view.setMouseTracking(True)
        self.view.viewport().installEventFilter(self)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.setWindowTitle("Círculo Dentro de un Cuadrado")
        self.resize(400, 400)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            # Obtener la posición del clic en la escena
            click_pos = self.view.mapToScene(event.pos())
            print(f"Posición del clic en la escena: {click_pos}")

            # Verificar si el clic está dentro del círculo
            if self.circle.contains(self.circle.mapFromScene(click_pos)):
                # Obtener la posición del centro del círculo relativa al cuadrado
                circle_center = self.circle.sceneBoundingRect().center()
                circle_center_in_square = self.square.mapFromScene(circle_center)
                print(f"Posición del centro del círculo dentro del cuadrado: {circle_center_in_square}")

        return super().eventFilter(source, event)

# Crear la aplicación
app = QApplication(sys.argv)

# Crear una instancia de la ventana principal
window = MainWindow()
window.show()

# Ejecutar la aplicación
sys.exit(app.exec())