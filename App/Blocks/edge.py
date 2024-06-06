from PyQt6.QtWidgets import QGraphicsPathItem, QGraphicsPolygonItem
from PyQt6.QtGui import QPen, QColor, QPainterPath, QPolygonF, QBrush
from PyQt6.QtCore import QPointF, Qt
from math import atan2, cos, sin, radians

class Line(QGraphicsPathItem):
    def __init__(self, start_point, end_point, arrow, color=QColor(0, 255, 255), thickness=2, style=Qt.PenStyle.DashLine):
        super().__init__()
        self.start_point = start_point
        self.end_point = end_point
        self.arrow = arrow
        self.color = color
        self.thickness = thickness
        self.style = style
        self.arrow_item = None

        self.setPen(QPen(self.color, self.thickness, self.style))
        self.update_path()

    def update_path(self):
        # Create a Bezier curve path
        path = QPainterPath(self.start_point)
        cp1 = QPointF((self.start_point.x() + self.end_point.x()) / 2, self.start_point.y())
        cp2 = QPointF((self.start_point.x() + self.end_point.x()) / 2, self.end_point.y())
        path.cubicTo(cp1, cp2, self.end_point)

        self.setPath(path)
        #self.update_arrow()

    def update_arrow(self):
        if self.arrow_item != None:
            pass

        if self.arrow:
            self.add_arrow(self.start_point, self.end_point)
        else:
            self.add_arrow(self.end_point, self.start_point)
    
    def add_arrow(self, start_point, end_point):
        arrow_size = 10
        angle = atan2(end_point.y() - start_point.y(), end_point.x() - start_point.x())

        p1 = end_point
        p2 = QPointF(p1.x() + arrow_size * cos(radians(angle - 150)), p1.y() + arrow_size * sin(radians(angle - 150)))
        p3 = QPointF(p1.x() + arrow_size * cos(radians(angle + 150)), p1.y() + arrow_size * sin(radians(angle + 150)))

        arrow_head = QPolygonF([p1, p2, p3])
        arrow_item = QGraphicsPolygonItem(arrow_head, self)
        arrow_item.setBrush(QBrush(QColor(0, 255, 255)))