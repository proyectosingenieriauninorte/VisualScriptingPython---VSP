from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsLineItem

from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QLineF

class Line(QGraphicsLineItem):
    def __init__(self, start_point, end_point, color=QColor(0, 255, 255), thickness=2):
        super().__init__(QLineF(start_point, end_point))
        self.setPen(QPen(color, thickness))