import App.Blocks.blocksDesing as blocksDesing
from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsSceneMouseEvent, QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsItem
from PyQt6.QtGui import QBrush, QColor, QPen, QPainterPath
from PyQt6.QtCore import Qt, QRectF, QPointF
from App.Blocks.point import Point
from App.Blocks.edge import Line

class BlockItem(QGraphicsRectItem):
    def __init__(self, scene, block_type, title, x, y, windows, LLNode, width=180, height=120):
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
        self.lines = []
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        #Linked List Node
        self.LLNode = LLNode
        
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

    # Método para agregar puntos de conexión al bloque
    def add_connection_point(self, point_name, label, inout=False):
        point = self.connection_points[point_name]
        circle = Point(point.x(), point.y(), label, self, inout)
        self.points[point_name] = circle
        #self.scene.addItem(text)
    
    # Sobreescribir el método de pintura
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
                            print(point)
                            self.windows.add_line_block((self, event.scenePos(), point))
                            point.circle.setBrush(QBrush(Qt.GlobalColor.green))
                        else:
                            if ((self.windows.line_blocks[0][0] != self) and (self.windows.line_blocks[0][2].inout != point.inout)) or (self.windows.line_blocks[0][2] == point):
                                if self.windows.line_blocks[0][2] == point:
                                    print("Same point")
                                else:
                                    if (point.validate == False) and (self.windows.line_blocks[0][2].validate == False):
                                        if (self.windows.line_blocks[0][2].inout == True):
                                            if (("flow" in self.windows.line_blocks[0][2].label) and ("flow" in point.label)):
                                                self.windows.line_blocks[0][0].LLNode.outs[self.windows.line_blocks[0][2].label][0] = self.LLNode
                                                self.LLNode.ins[point.label][0] = self.windows.line_blocks[0][0].LLNode
                                                print("Conection between blocks")
                                                self.windows.line_blocks[0][2].add_conection_block(self, point)
                                                point.add_conection_block(self.windows.line_blocks[0][0], self.windows.line_blocks[0][2])
                                                new_pos = event.scenePos()
                                                point.validate = True
                                                self.windows.line_blocks[0][2].validate = True
                                                line_temp = Line(self.windows.line_blocks[0][1], new_pos, True)
                                                self.windows.line_blocks[0][0].lines.append((line_temp, not point.inout, self.windows.line_blocks[0][2]))
                                                self.lines.append((line_temp, point.inout, point))
                                                self.scene.addItem(line_temp)
                                                
                                            elif (("flow" in self.windows.line_blocks[0][2].label) or ("flow" in point.label)):
                                                print("flow con no flow")
                                            else:
                                                self.LLNode.ins[point.label][0] = self.windows.line_blocks[0][0].LLNode.outs[self.windows.line_blocks[0][2].label][0]
                                                self.LLNode.ins[point.label][1] = self.windows.line_blocks[0][0].LLNode
                                                self.LLNode.ins[point.label][2] = self.windows.line_blocks[0][2].label
                                                
                                                self.windows.line_blocks[0][0].LLNode.outs[self.windows.line_blocks[0][2].label][1] = self.LLNode
                                                self.windows.line_blocks[0][0].LLNode.outs[self.windows.line_blocks[0][2].label][2] = point.label
                                                print("Conection between blocks")
                                                self.windows.line_blocks[0][2].add_conection_block(self, point)
                                                point.add_conection_block(self.windows.line_blocks[0][0], self.windows.line_blocks[0][2])
                                                new_pos = event.scenePos()
                                                point.validate = True
                                                self.windows.line_blocks[0][2].validate = True
                                                line_temp = Line(new_pos, self.windows.line_blocks[0][1], False)
                                                self.windows.line_blocks[0][0].lines.append((line_temp, not point.inout, self.windows.line_blocks[0][2]))
                                                self.lines.append((line_temp, point.inout, point))
                                                self.scene.addItem(line_temp)
                                        else:
                                            if (("flow" in self.windows.line_blocks[0][2].label) and ("flow" in point.label)):
                                                self.LLNode.outs[point.label][0] = self.windows.line_blocks[0][0].LLNode
                                                self.windows.line_blocks[0][0].LLNode.ins[self.windows.line_blocks[0][2].label][0] = self.LLNode
                                                print("Conection between blocks")
                                                self.windows.line_blocks[0][2].add_conection_block(self, point)
                                                point.add_conection_block(self.windows.line_blocks[0][0], self.windows.line_blocks[0][2])
                                                new_pos = event.scenePos()
                                                point.validate = True
                                                self.windows.line_blocks[0][2].validate = True
                                                line_temp = Line(new_pos, self.windows.line_blocks[0][1], True)
                                                self.windows.line_blocks[0][0].lines.append((line_temp, not point.inout, self.windows.line_blocks[0][2]))
                                                self.lines.append((line_temp, point.inout, point))
                                                self.scene.addItem(line_temp)
                                            elif (("flow" in self.windows.line_blocks[0][2].label) or ("flow" in point.label)):
                                                print("flow con no flow")    
                                            else:
                                                self.windows.line_blocks[0][0].LLNode.ins[self.windows.line_blocks[0][2].label][0] = self.LLNode.outs[point.label][0]
                                                self.windows.line_blocks[0][0].LLNode.ins[self.windows.line_blocks[0][2].label][1] = self.LLNode
                                                self.windows.line_blocks[0][0].LLNode.ins[self.windows.line_blocks[0][2].label][2] = point.label
                                                
                                                self.LLNode.outs[point.label][1] = self.windows.line_blocks[0][0].LLNode
                                                self.LLNode.outs[point.label][2] = self.windows.line_blocks[0][2].label
                                                print("Conection between blocks")
                                                self.windows.line_blocks[0][2].add_conection_block(self, point)
                                                point.add_conection_block(self.windows.line_blocks[0][0], self.windows.line_blocks[0][2])
                                                new_pos = event.scenePos()
                                                point.validate = True
                                                self.windows.line_blocks[0][2].validate = True
                                                line_temp = Line(self.windows.line_blocks[0][1], new_pos, False)
                                                self.windows.line_blocks[0][0].lines.append((line_temp, not point.inout, self.windows.line_blocks[0][2]))
                                                self.lines.append((line_temp, point.inout, point))
                                                self.scene.addItem(line_temp)
                                        #print(f"Bloque 1 creo... es {self.windows.line_blocks[0][0].block_type} y el point es {self.windows.line_blocks[0][2].label}")
                                        #print(self.windows.line_blocks[0][0].LLNode.ins)
                                        #print(self.windows.line_blocks[0][0].LLNode.outs)
                                        #print(f"Bloque 2 creo... es {self.block_type} y el point es {point.label}")
                                        #print(self.LLNode.ins)
                                        #print(self.LLNode.outs)
                                    else:
                                        print("Error")
                                self.windows.line_blocks[0][0].points[self.windows.line_blocks[0][2].label].circle.setBrush(QBrush(Qt.GlobalColor.blue))
                                self.windows.reset_line_blocks()

    # Evento de movimiento del mouse para arrastrar el bloque en la escena
    def mouseMoveEvent(self, event):
        # Si se está arrastrando el bloque y el botón izquierdo del mouse está presionado
        if self.is_dragging and event.buttons() & Qt.MouseButton.LeftButton:
            # Obtener la nueva posición del bloque
            new_pos = event.scenePos()
            self.setPos(new_pos.x() - self.x - 90, new_pos.y() - self.y - 10)   
            # Actualizar la posición de la linea de conexión con referencia a la nueva posicion del centro del circulo (punto) asociado al bloque
            for line in self.lines:
                circle_center_scene = line[2].circle.sceneBoundingRect().center()
                circle_center_view = self.scene.views()[0].mapFromScene(circle_center_scene)
                circle_center_square = self.scene.views()[0].mapToScene(circle_center_view)
                # Actualizar la posición del punto de inicio o fin de la linea dependiendo si es in u out
                if line[1]:
                    line[0].start_point = QPointF(circle_center_square.x(), circle_center_square.y())
                else:
                    line[0].end_point = QPointF(circle_center_square.x(), circle_center_square.y())
                # Actualizar la posición de la linea
                line[0].update_path()

    # Cambiar el cursor cuando el mouse se encuentra sobre el bloque
    def mouseReleaseEvent(self, event):
        if self.header_rect.contains(event.pos()):
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)
        self.is_dragging = False

    # Evento de doble click en el bloque para eliminarlo
    def mouseDoubleClickEvent(self, event):
        # Si el botón izquierdo del mouse es presionado
        if event.button() == Qt.MouseButton.LeftButton:
            if self:
                # Eliminar el bloque de la escena con sus respectivas conexiones tanto de el mismo como de sus bloques adyacentes
                current = self.LLNode
                for key in current.outs:
                    if key != "flow_out":
                        try:
                            current.outs[key][1].ins[current.outs[key][2]] = [None, None, None]
                        except:
                            pass
                    else:
                        try:
                            current.outs["flow_out"][0].ins["flow_in"] = [None]
                        except:
                            pass
                try:
                    current.ins['flow_in'][0].outs["flow_out"] = [None]
                except:
                    pass
                
                for point in self.points.values():
                    if point.point_connect != None:
                        point.point_connect.validate = False
                self.scene.removeItem(self)
                for line in self.lines:
                    self.scene.removeItem(line[0])