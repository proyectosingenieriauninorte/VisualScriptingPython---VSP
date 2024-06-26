from PyQt6.QtWidgets import QGraphicsTextItem, QGraphicsEllipseItem
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtCore import Qt

class Point():

    # Inicializador del punto del bloque con sus diferentes atributos
    def __init__(self, x, y, label, block_item, inout, validate=False):
        self.x = x
        self.y = y
        self.label = label
        self.block_item = block_item
        self.inout = inout
        self.validate = validate
        self.connections = []
        self.line = None
        self.block_connect = None
        self.point_connect = None
        self.add_connection_point()

    # Agregar un punto de conexión al bloque
    def add_connection_point(self):
        self.circle = QGraphicsEllipseItem(self.x - 4, self.y - 4, 8, 8, self.block_item)
        self.circle.setPen(QPen(Qt.GlobalColor.red))
        self.circle.setBrush(QBrush(Qt.GlobalColor.blue))
        #self.scene.addItem(circle)

        text = QGraphicsTextItem(self.label, self.block_item)
        text.setDefaultTextColor(Qt.GlobalColor.white)
        text.setPos(self.x + 5, self.y - 8)
        #self.scene.addItem(text)

        if self.inout:
            text.setPos(self.x - text.boundingRect().width() - 5, self.y - 8)
        else:
            text.setPos(self.x + 5, self.y - 8)

    # Agregar un bloque de conexión al punto (Con que bloque se conecta y con cual punto de dicho bloque)
    def add_conection_block(self, block, point):
        self.block_connect = block
        self.point_connect = point