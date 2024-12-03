from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.GroupedDragging)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("background-color:rgb(0, 49, 97);\n"
"font: 75 16pt \"Verdana\";\n"
"color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 799, 39))
        self.label_2.setStyleSheet("background-color: rgb(0, 106, 103);\n"
"font: 75 16pt \"Verdana\";\n"
"color: white;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 781, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/pepe1/OneDrive/Documentos/Jose/Proyecto_v2/imgenes/owners_icon_256px.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/pepe1/OneDrive/Documentos/Jose/Proyecto_v2/imgenes/minimal_vet_icon_256px.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.btnDuenios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDuenios.setObjectName("btnDuenios")
        self.gridLayout.addWidget(self.btnDuenios, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/pepe1/OneDrive/Documentos/Jose/Proyecto_v2/imgenes/pets_icon_256px.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.btnMascotas = QtWidgets.QPushButton(self.layoutWidget)
        self.btnMascotas.setObjectName("btnMascotas")
        self.gridLayout.addWidget(self.btnMascotas, 1, 2, 1, 1)
        self.btnUsuarios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnUsuarios.setObjectName("btnUsuarios")
        self.gridLayout.addWidget(self.btnUsuarios, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/pepe1/OneDrive/Documentos/Jose/Proyecto_v2/imgenes/simple_appointments_icon_256px.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.btnVeterinarios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnVeterinarios.setObjectName("btnVeterinarios")
        self.gridLayout.addWidget(self.btnVeterinarios, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:/Users/pepe1/OneDrive/Documentos/Jose/Proyecto_v2/imgenes/medical_records_icon_256px.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.btnCitas = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCitas.setObjectName("btnCitas")
        self.gridLayout.addWidget(self.btnCitas, 3, 1, 1, 1)
        self.btnExpedientes = QtWidgets.QPushButton(self.layoutWidget)
        self.btnExpedientes.setObjectName("btnExpedientes")
        self.gridLayout.addWidget(self.btnExpedientes, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("background-color: rgb(0,0,0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/pepe1/OneDrive/Documentos/Jose/Proyecto_v2/imgenes/user_icon_256px.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.btnSesion = QtWidgets.QPushButton(self.centralwidget)
        self.btnSesion.setGeometry(QtCore.QRect(690, 80, 101, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/pepe1/OneDrive/Documentos/Jose/Proyecto_v2/imgenes/endS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSesion.setIcon(icon)
        self.btnSesion.setObjectName("btnSesion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Menú"))
        self.btnDuenios.setText(_translate("MainWindow", "Dueños"))
        self.btnMascotas.setText(_translate("MainWindow", "Mascotas"))
        self.btnUsuarios.setText(_translate("MainWindow", "Usuarios"))
        self.btnVeterinarios.setText(_translate("MainWindow", "Veterinarios"))
        self.btnCitas.setText(_translate("MainWindow", "Citas"))
        self.btnExpedientes.setText(_translate("MainWindow", "Expedientes"))
        self.btnSesion.setText(_translate("MainWindow", "Cerrar sesión"))
