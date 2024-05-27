from PyQt6.QtWidgets import QGraphicsPathItem, QGraphicsPolygonItem
from PyQt6.QtGui import QPainter, QPen, QColor, QPainterPath, QPolygonF, QBrush
from PyQt6.QtCore import Qt, QLineF, QPointF
from math import cos, sin, atan2, radians, degrees

class Line(QGraphicsPathItem):
    def __init__(self, start_point, end_point, color=QColor(0, 255, 255), thickness=2,  style=Qt.PenStyle.DashLine):
        super().__init__()
        self.setPen(QPen(color, thickness, style))

        # Create a Bezier curve path
        path = QPainterPath(start_point)
        cp1 = QPointF((start_point.x() + end_point.x()) / 2, start_point.y())
        cp2 = QPointF((start_point.x() + end_point.x()) / 2, end_point.y())
        path.cubicTo(cp1, cp2, end_point)

        self.setPath(path)
        
        self.add_arrow(start_point,end_point)
    
    def add_arrow(self, start_point, end_point):
        arrow_size = 10
        angle = atan2(end_point.y() - start_point.y(), end_point.x() - start_point.x())

        p1 = end_point
        p2 = QPointF(p1.x() + arrow_size * cos(radians(angle - 150)), p1.y() + arrow_size * sin(radians(angle - 150)))
        p3 = QPointF(p1.x() + arrow_size * cos(radians(angle + 150)), p1.y() + arrow_size * sin(radians(angle + 150)))

        arrow_head = QPolygonF([p1, p2, p3])
        arrow_item = QGraphicsPolygonItem(arrow_head, self)
        arrow_item.setBrush(QBrush(QColor(0, 255, 255)))