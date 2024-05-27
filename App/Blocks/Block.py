import App.Blocks.blocksDesing as blocksDesing
from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsEllipseItem
from PyQt6.QtGui import QBrush, QColor, QPen, QPainterPath
from PyQt6.QtCore import Qt, QRectF
from App.Blocks.point import Point
from App.Blocks.edge import Line

class BlockItem(QGraphicsRectItem):
    def __init__(self, scene, block_type, title, x, y, windows, width=180, height=100):
        super().__init__(x, y, width, height)
        self.windows = windows
        self.x = x
        self.y = y
        self.scene = scene  # Pasar la escena como argumento y asignarla a self.scene
        self.block_type = block_type
        self.is_dragging = False
        self.setPen(QPen(Qt.GlobalColor.black))
        self.setBrush(QBrush(QColor("#333333")))
        self.points = {}

        # Draw header
        self.header_height = 20
        self.header_rect = QRectF(x, y, width, self.header_height)
        self.header_brush = QBrush(self.get_header_color(block_type))
        
        # Title
        self.title_text = QGraphicsTextItem(title, self)
        self.title_text.setDefaultTextColor(Qt.GlobalColor.white)
        self.title_text.setPos(x + 5, y + 2)

        # Points of connection
        blocksDesing.drawPointsConnections(self, block_type, x, y, width)

    def get_header_color(self, block_type):
        colors = {
            "If": "#FF4500",          # OrangeRed
            "On_Start": "#FF6347",     # Tomato
            "On_Update": "#4682B4",    # SteelBlue
            "cycle": "#32CD32",        # LimeGreen
            "set_var": "#FFD700",      # Gold
            "set_arr": "#DAA520",      # GoldenRod
            "call_var": "#BA55D3",     # MediumOrchid
            "log": "#FF4500",          # OrangeRed
            "branch": "#2E8B57",       # SeaGreen
            "compare": "#8A2BE2",      # BlueViolet
            "for_iter": "#20B2AA",     # LightSeaGreen
            "add": "#00CED1",          # DarkTurquoise
            "sub": "#FF69B4",          # HotPink
            "mult": "#1E90FF",         # DodgerBlue
            "div": "#D2691E",          # Chocolate
            "div_int": "#FFB6C1",      # LightPink
            "mod": "#4B0082",          # Indigo
            "append_arr": "#7B68EE"    # MediumSlateBlue

        }
        return QColor(colors.get(block_type, "#FF4500")) 

    #Aun no funciona dibujar los puntos de conexion
    def add_connection_point(self, point_name, label, inout=False):
        point = self.connection_points[point_name]
        circle = Point(point.x(), point.y(), label, self, inout)
        self.points[point_name] = circle
        #self.scene.addItem(text)
    
    def paint(self, painter, option, widget):
        # Draw the main rounded rectangle
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 10, 10)
        painter.fillPath(path, QBrush(QColor("#333333")))
        painter.drawPath(path)

        header_path = QPainterPath()
        #header_path.addRoundedRect(self.header_rect, 10, 10)
        header_path.moveTo(self.header_rect.topLeft())
        header_path.lineTo(self.header_rect.topRight())
        header_path.lineTo(self.header_rect.bottomRight().x() , self.header_rect.bottomRight().y())
        header_path.lineTo(self.header_rect.bottomLeft().x() , self.header_rect.bottomLeft().y())
        
        header_path.closeSubpath()

        painter.fillPath(header_path, self.header_brush)
        painter.drawPath(header_path)

    # Override mouse press event
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.header_rect.contains(event.pos()):
                self.setCursor(Qt.CursorShape.ClosedHandCursor)
                self.is_dragging = True
            elif self.points:
                for point in self.points.values():
                    if point.circle.contains(event.pos()):
                        if len(self.windows.line_blocks) == 0:
                            self.windows.add_line_block((self, event.scenePos(), point))
                            point.circle.setBrush(QBrush(Qt.GlobalColor.green))
                        else:
                            if ((self.windows.line_blocks[0][0] != self) and (self.windows.line_blocks[0][2].inout != point.inout)) or self.windows.line_blocks[0][2] == point:
                                if self.windows.line_blocks[0][2] == point:
                                    print("Same point")
                                else: 
                                    print("Conection between blocks")
                                    self.windows.line_blocks[0][2].add_conection_block(self, point)
                                    point.add_conection_block(self.windows.line_blocks[0][0], self.windows.line_blocks[0][2])
                                    new_pos = event.scenePos()
                                    line_temp = Line(self.windows.line_blocks[0][1], new_pos)
                                    self.scene.addItem(line_temp)
                                self.windows.line_blocks[0][0].points[self.windows.line_blocks[0][2].label].circle.setBrush(QBrush(Qt.GlobalColor.blue))
                                self.windows.reset_line_blocks()

    # Override mouse move event
    def mouseMoveEvent(self, event):
        if self.is_dragging and event.buttons() & Qt.MouseButton.LeftButton:
            new_pos = event.scenePos()
            self.setPos(new_pos.x() - self.x, new_pos.y() - self.y)

    # Override mouse release event
    def mouseReleaseEvent(self, event):
        if self.header_rect.contains(event.pos()):
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)
        self.is_dragging = False