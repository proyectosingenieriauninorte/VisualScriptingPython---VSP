from App.Blocks.Block import BlockItem
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QMenu, QLineEdit, QTextEdit, QMenuBar, QGraphicsScene, QGraphicsView
from PyQt6 import QtCore, QtGui
from App.Blocks.LinkedList import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_blocks = []
        self.setWindowTitle("Visual Scripting")
        self.resize(1280, 720)
        self.setStyleSheet("Background-color: rgb(43, 48, 77);")
        self.centralwidget = QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.icon_only_widget = QWidget(parent=self.centralwidget)
        self.icon_only_widget.setGeometry(QtCore.QRect(20, 10, 171, 671))
        font = QtGui.QFont()
        font.setFamily("Futura Medium")
        self.icon_only_widget.setFont(font)
        self.icon_only_widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(63, 67, 103);\n"
"    border-radius: 25;\n"
"}\n"
"\n"
"QPushButton {\n"
"  min-width: 70px;\n"
"  height: 40px;\n"
"  color: #fff;\n"
"  padding: 5px 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"  transition: all 0.3s ease;\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  outline: none;\n"
"  border-radius: 10px;\n"
"  border: 2px solid #55C590;\n"
"  background: #55C590;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #fff;\n"
"  color: #adb5bd\n"
"}\n"
"\n"
"QLineEdit {\n"
"\n"
"}\n"
"QLabel {\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.add_script = QPushButton(parent=self.icon_only_widget)
        self.add_script.clicked.connect(self.run)
        self.add_script.setGeometry(QtCore.QRect(30, 630, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Futura Medium")
        font.setBold(True)
        self.add_script.setFont(font)
        self.add_script.setObjectName("add_script")
        self.label_script = QLabel(parent=self.icon_only_widget)
        self.label_script.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Futura Medium")
        font.setPointSize(18)
        font.setBold(False)
        self.label_script.setFont(font)
        self.label_script.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_script.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_script.setObjectName("label_script")
        self.text_script_add = QLineEdit(parent=self.icon_only_widget)
        self.text_script_add.setGeometry(QtCore.QRect(20, 600, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.text_script_add.setFont(font)
        self.text_script_add.setAutoFillBackground(False)
        self.text_script_add.setStyleSheet("border: 2px solid #636B97;\n"
"background-color: #636B97;    \n"
"border-radius: 10;")
        self.text_script_add.setObjectName("text_script_add")
        self.WorkspaceWidget = QWidget(parent=self.centralwidget)
        self.WorkspaceWidget.setGeometry(QtCore.QRect(210, 10, 881, 401))
        self.WorkspaceWidget.setStyleSheet("QWidget {\n"
"    background-color: rgb(21, 29, 47);\n"
"    border-radius: 25;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    \n"
"    border-color: rgb(118, 171, 174);\n"
"}")
        self.WorkspaceWidget.setObjectName("WorkspaceWidget")
        self.work_area = QGraphicsView(parent=self.WorkspaceWidget)
        self.work_area.setGeometry(QtCore.QRect(0, 0, 881, 401))
        self.work_area.setObjectName("work_area")
        self.graphics_scene = QGraphicsScene()
        self.work_area.setScene(self.graphics_scene)
        self.icon_only_widget_2 = QWidget(parent=self.centralwidget)
        self.icon_only_widget_2.setGeometry(QtCore.QRect(1110, 10, 151, 671))
        self.icon_only_widget_2.setStyleSheet("QWidget {\n"
"    background-color: rgb(63, 67, 103);\n"
"    border-radius: 25;\n"
"}\n"
"\n"
"QPushButton {\n"
"  min-width: 70px;\n"
"  height: 40px;\n"
"  color: #fff;\n"
"  padding: 5px 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"  transition: all 0.3s ease;\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  outline: none;\n"
"  border-radius: 10px;\n"
"  border: 2px solid #55C590;\n"
"  background: #55C590;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #fff;\n"
"  color: #adb5bd\n"
"}\n"
"QLabel {\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.icon_only_widget_2.setObjectName("icon_only_widget_2")
        self.add_variable = QPushButton(parent=self.icon_only_widget_2)
        self.add_variable.setGeometry(QtCore.QRect(20, 630, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Futura Medium")
        font.setBold(True)
        self.add_variable.setFont(font)
        self.add_variable.setObjectName("add_variable")
        self.label_variable = QLabel(parent=self.icon_only_widget_2)
        self.label_variable.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Futura Medium")
        font.setPointSize(18)
        font.setBold(False)
        self.label_variable.setFont(font)
        self.label_variable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_variable.setObjectName("label_variable")
        self.text_variable_add = QLineEdit(parent=self.icon_only_widget_2)
        self.text_variable_add.setGeometry(QtCore.QRect(10, 600, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.text_variable_add.setFont(font)
        self.text_variable_add.setStyleSheet("border: 2px solid #636B97;\n"
"background-color: #636B97;    \n"
"border-radius: 10\n"
";")
        self.text_variable_add.setObjectName("text_variable_add")
        self.LogWidget = QWidget(parent=self.centralwidget)
        self.LogWidget.setGeometry(QtCore.QRect(210, 430, 881, 251))
        self.LogWidget.setStyleSheet("QWidget {\n"
"    background-color: rgb(99, 107, 151);\n"
"    border-radius: 25;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    \n"
"    border-color: rgb(118, 171, 174);\n"
"}")
        self.LogWidget.setObjectName("LogWidget")
        self.cmd = QTextEdit(parent=self.LogWidget)
        self.cmd.setGeometry(QtCore.QRect(23, 20, 831, 211))
        self.cmd.setReadOnly(True)
        self.cmd.setObjectName("cmd")
        self.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(parent=self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1112, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuBlock = QMenu(parent=self.menuBar)
        self.menuBlock.setObjectName("menuBlock")
        self.setMenuBar(self.menuBar)
        self.actionImport = QtGui.QAction(parent=self)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(parent=self)
        self.actionExport.setObjectName("actionExport")
        self.actionSearch = QtGui.QAction(parent=self)
        self.actionSearch.setObjectName("actionSearch")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuBlock.addAction(self.actionSearch)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuBlock.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.work_area.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.work_area.customContextMenuRequested.connect(self.show_context_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_script.setText(_translate("MainWindow", "Add"))
        self.label_script.setText(_translate("MainWindow", "Scripts"))
        self.add_variable.setText(_translate("MainWindow", "Add"))
        self.label_variable.setText(_translate("MainWindow", "Variable"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuBlock.setTitle(_translate("MainWindow", "Block"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))

    def show_context_menu(self, pos):
        context_menu = QMenu(self)

        # Lista de bloques a añadir
        block_types = ["If", "On_Start", "On_Update", "str_lit", "int_lit", "float_lit", "bool_lit", "cycle", "set_var", "set_arr", "call_var", "log", "branch", "compare", "for_iter", "add", "sub", "mult", "div", "div_int", "mod", "append_arr"]
        
        # Crear acciones para cada bloque
        for block_type in block_types:
            action = QtGui.QAction(block_type, self)
            action.triggered.connect(lambda checked, bt=block_type: self.add_block(bt, pos))
            context_menu.addAction(action)

        context_menu.exec(self.work_area.mapToGlobal(pos))

    def add_block(self, block_type, pos):
        # Convertir la posición del clic a coordenadas de la escena
        
        if block_type == "On_Start":
            Node = On_Start_Node(block_type, {}, {})
            self.Sequence = LinkedList(Node, self.cmd)
        elif block_type == "log":
            Node = log_Node(block_type, {}, {})
        elif block_type == "str_lit":
            Node = str_literal(block_type, {}, {})
        elif block_type == "int_lit":
            Node = int_literal(block_type, {}, {})
        elif block_type == "float_lit":
            Node = float_literal(block_type, {}, {})
        elif block_type == "bool_lit":
            Node = bool_literal(block_type, {}, {})
        elif block_type == "If":
            Node = if_Node(block_type, {}, {})
        elif block_type == "compare":
            Node = compare_Node(block_type, {}, {})
        elif block_type == "add":
            Node = add_Node(block_type, {}, {})
        elif block_type == "sub":
            Node = sub_Node(block_type, {}, {})
        elif block_type == "mult":
            Node = mult_Node(block_type, {}, {})
        elif block_type == "div":
            Node = div_Node(block_type, {}, {})
        
        scene_pos = self.work_area.mapToScene(pos)
        block = BlockItem(self.graphics_scene, block_type, block_type, scene_pos.x(), scene_pos.y(), self, Node)  # Pasar self.graphics_scene como argumento
        self.graphics_scene.addItem(block)
        
        

    def add_line_block(self, block):
        self.line_blocks.append(block)
    
    def reset_line_blocks(self):
        self.line_blocks = []
        
    def run(self):
        self.Sequence.run()