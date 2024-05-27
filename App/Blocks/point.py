from PyQt6.QtWidgets import QGraphicsTextItem, QGraphicsEllipseItem
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtCore import Qt

class Point():

    def __init__(self, x, y, label, block_item, inout):
        self.x = x
        self.y = y
        self.label = label
        self.block_item = block_item
        self.inout = inout
        self.add_connection_point()

    def add_connection_point(self):
        self.circle = QGraphicsEllipseItem(self.x - 3, self.y - 3, 6, 6, self.block_item)
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

    def add_conection_block(self, block, point):
        self.block_connect = block
        self.point_connect = point