from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDockWidget, QListWidget, QWidget, 
    QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QMenu, QGraphicsEllipseItem,
    QLineEdit, QGraphicsProxyWidget
)
from PyQt6.QtGui import QBrush, QColor, QPen, QPainter, QAction, QFont, QIntValidator, QDoubleValidator
from PyQt6.QtCore import Qt, QPointF, QRectF

def drawPointsConnections(self, block_type, x, y,width):
    '''Bloques de flujo'''
    if block_type== 'On_Start' :
        # Points of connection
        #self.connection_points = {
        #    'condition': QPointF(x + 10, y + self.header_height + 10),
        #    'true': QPointF(x + width - 10, y + self.header_height + 5),
        #    'false': QPointF(x + width - 10, y + self.header_height + 25)
        #}
        self.connection_points = {
            'flow_out': QPointF(x + width - 10, y + self.header_height + 10),
        }
        # Draw connection points and labels
        self.add_connection_point('flow_out', "flow_out", True)

    if block_type== 'On_Update' :
        # Points of connection
        self.connection_points = {
            'flow': QPointF(x + 10, y + self.header_height + 10),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),

        }

        # Draw connection points and labels
        self.add_connection_point('flow', "flow")
        self.add_connection_point('flow_out', "flow_out", True)

    '''Bloques de Asigancion''' 
    if block_type == 'str_lit':
        # Points of connection
        self.connection_points = {
            'value': QPointF(x + width - 10, y + self.header_height + 5),
        }

        # Draw connection points and labels
        self.add_connection_point('value', "value", True)

        # Add QLineEdit for string literal's value
        self.str_input = QLineEdit()
        self.str_input.setPlaceholderText("Value")
        self.str_input.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.str_input.setMaximumSize(70, 20)
        self.str_input.textChanged.connect(self.LLNode.strHasChanged)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.str_input)
        proxy_name.setPos(x + 65, y + self.header_height + 20)
        
    if block_type == 'int_lit':
        # Points of connection
        self.connection_points = {
            'value': QPointF(x + width - 10, y + self.header_height + 5),
        }

        # Draw connection points and labels
        self.add_connection_point('value', "value", True)

        # Add QLineEdit for string literal's value
        self.int_input = QLineEdit()
        int_validator = QIntValidator()
        self.int_input.setValidator(int_validator) #Añadir un validador para que solo se puedan escribir numeros enteros
        self.int_input.setPlaceholderText("Value")
        self.int_input.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.int_input.setMaximumSize(70, 20)
        self.int_input.textChanged.connect(self.LLNode.intHasChanged)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.int_input)
        proxy_name.setPos(x + 65, y + self.header_height + 20)
        
    if block_type == 'float_lit':
        # Points of connection
        self.connection_points = {
            'value': QPointF(x + width - 10, y + self.header_height + 5),
        }

        # Draw connection points and labels
        self.add_connection_point('value', "value", True)

        # Add QLineEdit for string literal's value
        self.value_input = QLineEdit()
        double_validator = QDoubleValidator()
        self.float_input.setValidator(double_validator) #Añadir un validador para que solo se puedan escribir numeros de tipo double
        self.float_input.setPlaceholderText("Value")
        self.float_input.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.float_input.setMaximumSize(70, 20)
        self.float_input.textChanged.connect(self.LLNode.floatHasChanged)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.float_input)
        proxy_name.setPos(x + 65, y + self.header_height + 20)
        
    if block_type == 'bool_lit':
        # Points of connection
        self.connection_points = {
            'true': QPointF(x + width - 10, y + self.header_height + 5),
            'false': QPointF(x + width - 10, y + self.header_height + 25),
        }

        # Draw connection points and labels
        self.add_connection_point('true', "true", True)
        self.add_connection_point('false', "false", True)

    if block_type== 'set_var' :
        # Points of connection
        self.connection_points = {
            'flow': QPointF(x + 10, y + self.header_height + 10),
            'val_in': QPointF(x + 10, y + self.header_height + 30),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            'val': QPointF(x + width - 10, y + self.header_height + 25),
        }

        # Draw connection points and labels
        self.add_connection_point('flow', "flow")
        self.add_connection_point('val_in', "val_in")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('val', "val", True)

        # Add QLineEdit for variable name
        self.var_name_edit = QLineEdit()
        self.var_name_edit.setPlaceholderText("Var Name")
        self.var_name_edit.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.var_name_edit.setMaximumSize(70, 20)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.var_name_edit)
        proxy_name.setPos(x + 65, y + self.header_height + 20)

        # Add QLineEdit for variable value
        self.var_value_edit = QLineEdit()
        self.var_value_edit.setPlaceholderText("Value")
        self.var_value_edit.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.var_value_edit.setMaximumSize(70, 20)
        proxy_value = QGraphicsProxyWidget(self)
        proxy_value.setWidget(self.var_value_edit)
        proxy_value.setPos(x + 65, y + self.header_height + 50)

    if block_type== 'set_arr' :
        # Points of connection
        self.connection_points = {
            'flow': QPointF(x + 10, y + self.header_height + 10),
            'arr_in': QPointF(x + 10, y + self.header_height + 30),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            'arr': QPointF(x + width - 10, y + self.header_height + 25),
        }

        # Draw connection points and labels
        self.add_connection_point('flow', "flow")
        self.add_connection_point('arr_in', "arr_in")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('arr', "arr", True)

        # Add QLineEdit for variable name
        self.var_name_edit = QLineEdit()
        self.var_name_edit.setPlaceholderText("Arr Name")
        self.var_name_edit.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.var_name_edit.setMaximumSize(70, 20)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.var_name_edit)
        proxy_name.setPos(x + 65, y + self.header_height + 20)

        # Add QLineEdit for variable value
        self.var_value_edit = QLineEdit()
        self.var_value_edit.setPlaceholderText("a, b, c, ..")
        self.var_value_edit.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.var_value_edit.setMaximumSize(70, 20)
        proxy_value = QGraphicsProxyWidget(self)
        proxy_value.setWidget(self.var_value_edit)
        proxy_value.setPos(x + 65, y + self.header_height + 50)

    if block_type== 'call_var' :
        # Points of connection
        self.connection_points = {
            'flow': QPointF(x + 10, y + self.header_height + 10),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            'val': QPointF(x + width - 10, y + self.header_height + 25),
        }

        # Draw connection points and labels
        self.add_connection_point('flow', "flow")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('val', "val", True)   

        self.var_name_edit = QLineEdit()
        self.var_name_edit.setPlaceholderText("Var Name")
        self.var_name_edit.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.var_name_edit.setMaximumSize(70, 20)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.var_name_edit)
        proxy_name.setPos(x + 50, y + self.header_height + 30)

    '''Bloques de Ejecución''' 

    if block_type== 'log' :
        # Points of connection
        self.connection_points = {
            'flow_in': QPointF(x + 10, y + self.header_height + 10),
            'value': QPointF(x + 10, y + self.header_height + 30),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
        }

        # Draw connection points and labels
        self.add_connection_point('flow_in', "flow_in")
        self.add_connection_point('value', "value")
        self.add_connection_point('flow_out', "flow_out", True)   

        self.val_to_print = QLineEdit()
        self.val_to_print.setPlaceholderText("print")
        self.val_to_print.setMinimumSize(70, 20)  # Set the minimum size for the QLineEdit
        self.val_to_print.setMaximumSize(70, 20)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_to_print)
        proxy_name.setPos(x + 60, y + self.header_height + 30)

    if block_type== 'If' :
        # Points of connection
        self.connection_points = {
            'flow_in': QPointF(x + 10, y + self.header_height + 10),
            'condition': QPointF(x + 10, y + self.header_height + 30),
            'flow_true': QPointF(x + width - 10, y + self.header_height + 5),
            'flow_false': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('flow_in', "flow_in")
        self.add_connection_point('condition', "condition")
        self.add_connection_point('flow_true', "flow_true", True)
        self.add_connection_point('flow_false', "flow_false", True)

    if block_type== 'compare' :
        # Points of connection
        self.connection_points = {
            'flow_in': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            '>': QPointF(x + width - 10, y + self.header_height + 25),
            '<': QPointF(x + width - 10, y + self.header_height + 45),
            '=': QPointF(x + width - 10, y + self.header_height + 65),
            '!=': QPointF(x + width - 10, y + self.header_height + 85)
        }

        # Draw connection points and labels
        self.add_connection_point('flow_in', "flow_in")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('>', ">", True)
        self.add_connection_point('<', "<", True)
        self.add_connection_point('=', "=", True)
        self.add_connection_point('!=', "!=", True)

    '''Bloques operacionales'''
    if block_type== 'add' :
        # Points of connection
        self.connection_points = {
            'flow_in': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('flow_in', "flow_in")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('result', "result", True)
        
        #QLineEdit for arithmethic blocks, makes no sense when there is already literal blocks
        #self.val_a = QLineEdit()
        #self.val_a.setPlaceholderText("A")
        #self.val_a.setMinimumSize(30, 15)  
        #self.val_a.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_a)
        #proxy_name.setPos(x + 40, y + self.header_height + 20)

        #self.suma_simbol = QGraphicsTextItem("+", self)
        #self.suma_simbol.setDefaultTextColor(Qt.GlobalColor.white)
        #self.suma_simbol.setPos(x + 73, y+35 )

        #self.val_b = QLineEdit()
        #self.val_b.setPlaceholderText("B")
        #self.val_b.setMinimumSize(30, 15)  
        #self.val_b.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_b)
        #proxy_name.setPos(x + 90, y + self.header_height + 20)

    if block_type== 'sub' :
        # Points of connection
        self.connection_points = {
            'flow_in': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('flow_in', "flow_in")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('result', "result", True)
        
        #self.val_a = QLineEdit()
        #self.val_a.setPlaceholderText("A")
        #self.val_a.setMinimumSize(30, 15)  
        #self.val_a.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_a)
        #proxy_name.setPos(x + 40, y + self.header_height + 20)

        #self.sub_simbol = QGraphicsTextItem("-", self)
        #self.sub_simbol.setDefaultTextColor(Qt.GlobalColor.white)
        #self.sub_simbol.setPos(x + 73, y+35 )

        #self.val_b = QLineEdit()
        #self.val_b.setPlaceholderText("B")
        #self.val_b.setMinimumSize(30, 15)  
        #self.val_b.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_b)
        #proxy_name.setPos(x + 90, y + self.header_height + 20)

    if block_type== 'mult' :
        # Points of connection
        self.connection_points = {
            'flow_in': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('flow_in', "flow_in")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('result', "result", True)
        
        #self.val_a = QLineEdit()
        #self.val_a.setPlaceholderText("A")
        #self.val_a.setMinimumSize(30, 15)  
        #self.val_a.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_a)
        #proxy_name.setPos(x + 40, y + self.header_height + 20)

        #self.simbol = QGraphicsTextItem("*", self)
        #self.simbol.setDefaultTextColor(Qt.GlobalColor.white)
        #self.simbol.setPos(x + 73, y+35 )

        #self.val_b = QLineEdit()
        #self.val_b.setPlaceholderText("B")
        #self.val_b.setMinimumSize(30, 15)  
        #self.val_b.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_b)
        #proxy_name.setPos(x + 90, y + self.header_height + 20)

    if block_type== 'div' :
        # Points of connection
        self.connection_points = {
            'flow_in': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('flow_in', "flow_in")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point('flow_out', "flow_out", True)
        self.add_connection_point('result', "result", True)
        
        #self.val_a = QLineEdit()
        #self.val_a.setPlaceholderText("A")
        #self.val_a.setMinimumSize(30, 15)  
        #self.val_a.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_a)
        #proxy_name.setPos(x + 40, y + self.header_height + 20)

        #self.simbol = QGraphicsTextItem("/", self)
        #self.simbol.setDefaultTextColor(Qt.GlobalColor.white)
        #self.simbol.setPos(x + 73, y+35 )

        #self.val_b = QLineEdit()
        #self.val_b.setPlaceholderText("B")
        #self.val_b.setMinimumSize(30, 15)  
        #self.val_b.setMaximumSize(30, 15)
        #proxy_name = QGraphicsProxyWidget(self)
        #proxy_name.setWidget(self.val_b)
        #proxy_name.setPos(x + 90, y + self.header_height + 20)

    if block_type== 'div_int' :
        # Points of connection
        self.connection_points = {
            '': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            ' ': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('', "")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point(' ', " ")
        self.add_connection_point('result', "result", True)
        
        self.val_a = QLineEdit()
        self.val_a.setPlaceholderText("A")
        self.val_a.setMinimumSize(30, 15)  
        self.val_a.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_a)
        proxy_name.setPos(x + 40, y + self.header_height + 20)

        self.simbol = QGraphicsTextItem("//", self)
        self.simbol.setDefaultTextColor(Qt.GlobalColor.white)
        self.simbol.setPos(x + 73, y+35 )

        self.val_b = QLineEdit()
        self.val_b.setPlaceholderText("B")
        self.val_b.setMinimumSize(30, 15)  
        self.val_b.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_b)
        proxy_name.setPos(x + 90, y + self.header_height + 20)

    if block_type== 'mod' :
        # Points of connection
        self.connection_points = {
            '': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            ' ': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('', "")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point(' ', " ")
        self.add_connection_point('result', "result", True)
        
        self.val_a = QLineEdit()
        self.val_a.setPlaceholderText("A")
        self.val_a.setMinimumSize(30, 15)  
        self.val_a.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_a)
        proxy_name.setPos(x + 40, y + self.header_height + 20)

        self.simbol = QGraphicsTextItem("%", self)
        self.simbol.setDefaultTextColor(Qt.GlobalColor.white)
        self.simbol.setPos(x + 73, y+35 )

        self.val_b = QLineEdit()
        self.val_b.setPlaceholderText("B")
        self.val_b.setMinimumSize(30, 15)  
        self.val_b.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_b)
        proxy_name.setPos(x + 90, y + self.header_height + 20)

    if block_type== 'greater_equal' :
        # Points of connection
        self.connection_points = {
            '': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            ' ': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('', "")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point(' ', " ")
        self.add_connection_point('result', "result", True)
        
        self.val_a = QLineEdit()
        self.val_a.setPlaceholderText("A")
        self.val_a.setMinimumSize(30, 15)  
        self.val_a.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_a)
        proxy_name.setPos(x + 40, y + self.header_height + 20)

        self.simbol = QGraphicsTextItem(">=", self)
        self.simbol.setDefaultTextColor(Qt.GlobalColor.white)
        self.simbol.setPos(x + 65, y+35 )

        self.val_b = QLineEdit()
        self.val_b.setPlaceholderText("B")
        self.val_b.setMinimumSize(30, 15)  
        self.val_b.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_b)
        proxy_name.setPos(x + 90, y + self.header_height + 20)

    if block_type== 'less_equal' :
        # Points of connection
        self.connection_points = {
            '': QPointF(x + 10, y + self.header_height + 10),
            'A': QPointF(x + 10, y + self.header_height + 30),
            'B': QPointF(x + 10, y + self.header_height + 50),
            ' ': QPointF(x + width - 10, y + self.header_height + 5),
            'result': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('', "")
        self.add_connection_point('A', "A")
        self.add_connection_point('B', "B")
        self.add_connection_point(' ', " ")
        self.add_connection_point('result', "result", True)
        
        self.val_a = QLineEdit()
        self.val_a.setPlaceholderText("A")
        self.val_a.setMinimumSize(30, 15)  
        self.val_a.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_a)
        proxy_name.setPos(x + 40, y + self.header_height + 20)

        self.simbol = QGraphicsTextItem("<=", self)
        self.simbol.setDefaultTextColor(Qt.GlobalColor.white)
        self.simbol.setPos(x + 65, y+35 )

        self.val_b = QLineEdit()
        self.val_b.setPlaceholderText("B")
        self.val_b.setMinimumSize(30, 15)  
        self.val_b.setMaximumSize(30, 15)
        proxy_name = QGraphicsProxyWidget(self)
        proxy_name.setWidget(self.val_b)
        proxy_name.setPos(x + 90, y + self.header_height + 20)