# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CrudExpedientesWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Crear un TabWidget para gestionar las pestañas
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 800, 500))
        self.tabWidget.setObjectName("tabWidget")

        # Pestaña de Listado de Expedientes
        self.tabListar = QtWidgets.QWidget()
        self.tabListar.setObjectName("tabListar")
        self.labelListar = QtWidgets.QLabel(self.tabListar)
        self.labelListar.setGeometry(QtCore.QRect(270, 10, 261, 61))
        self.labelListar.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.labelListar.setObjectName("labelListar")
        self.tableWidget = QtWidgets.QTableWidget(self.tabListar)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 700, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)

        # Encabezado de la tabla de expedientes
        self.tableWidget.setHorizontalHeaderLabels(["ID Expediente", "Mascota", "Descripción", "Fecha Apertura", "Última Actualización"])

        # Pestaña de Crear/Actualizar Expediente
        self.tabCrear = QtWidgets.QWidget()
        self.tabCrear.setObjectName("tabCrear")
        self.labelCrear = QtWidgets.QLabel(self.tabCrear)
        self.labelCrear.setGeometry(QtCore.QRect(250, 10, 311, 61))
        self.labelCrear.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.labelCrear.setObjectName("labelCrear")

        # Campos para los datos del expediente
        self.labelMascota = QtWidgets.QLabel(self.tabCrear)
        self.labelMascota.setGeometry(QtCore.QRect(50, 100, 150, 20))
        self.labelMascota.setObjectName("labelMascota")
        self.comboBoxMascota = QtWidgets.QComboBox(self.tabCrear)
        self.comboBoxMascota.setGeometry(QtCore.QRect(200, 100, 200, 20))
        self.comboBoxMascota.setObjectName("comboBoxMascota")

        self.labelDescripcion = QtWidgets.QLabel(self.tabCrear)
        self.labelDescripcion.setGeometry(QtCore.QRect(50, 150, 150, 20))
        self.labelDescripcion.setObjectName("labelDescripcion")
        self.textEditDescripcion = QtWidgets.QTextEdit(self.tabCrear)
        self.textEditDescripcion.setGeometry(QtCore.QRect(200, 150, 500, 100))
        self.textEditDescripcion.setObjectName("textEditDescripcion")

        self.labelFechaApertura = QtWidgets.QLabel(self.tabCrear)
        self.labelFechaApertura.setGeometry(QtCore.QRect(50, 270, 150, 20))
        self.labelFechaApertura.setObjectName("labelFechaApertura")
        self.dateEditFechaApertura = QtWidgets.QDateEdit(self.tabCrear)
        self.dateEditFechaApertura.setGeometry(QtCore.QRect(200, 270, 200, 20))
        self.dateEditFechaApertura.setObjectName("dateEditFechaApertura")

        # Botón de Guardar
        self.btnGuardar = QtWidgets.QPushButton(self.tabCrear)
        self.btnGuardar.setGeometry(QtCore.QRect(350, 400, 100, 30))
        self.btnGuardar.setObjectName("btnGuardar")

        # Pestaña de Eliminar Expediente
        self.tabEliminar = QtWidgets.QWidget()
        self.tabEliminar.setObjectName("tabEliminar")
        self.labelEliminar = QtWidgets.QLabel(self.tabEliminar)
        self.labelEliminar.setGeometry(QtCore.QRect(270, 10, 261, 61))
        self.labelEliminar.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.labelEliminar.setObjectName("labelEliminar")

        # Campos para eliminar un expediente
        self.labelEliminarId = QtWidgets.QLabel(self.tabEliminar)
        self.labelEliminarId.setGeometry(QtCore.QRect(50, 100, 150, 20))
        self.labelEliminarId.setObjectName("labelEliminarId")
        self.lineEditEliminarId = QtWidgets.QLineEdit(self.tabEliminar)
        self.lineEditEliminarId.setGeometry(QtCore.QRect(200, 100, 200, 20))
        self.lineEditEliminarId.setObjectName("lineEditEliminarId")

        self.btnEliminar = QtWidgets.QPushButton(self.tabEliminar)
        self.btnEliminar.setGeometry(QtCore.QRect(350, 150, 100, 30))
        self.btnEliminar.setObjectName("btnEliminar")

        # Añadir las pestañas al TabWidget
        self.tabWidget.addTab(self.tabListar, "Listar Expedientes")
        self.tabWidget.addTab(self.tabCrear, "Crear/Actualizar Expediente")
        self.tabWidget.addTab(self.tabEliminar, "Eliminar Expediente")

        # Botón de Regresar
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(350, 560, 100, 30))
        self.btnRegresar.setObjectName("btnRegresar")

        # Layout principal
        MainWindow.setCentralWidget(self.centralwidget)

        # Menú y barra de estado
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestión de Expedientes"))
        self.labelListar.setText(_translate("MainWindow", "Listado de Expedientes"))
        self.labelCrear.setText(_translate("MainWindow", "Crear/Actualizar Expediente"))
        self.labelMascota.setText(_translate("MainWindow", "Mascota:"))
        self.labelDescripcion.setText(_translate("MainWindow", "Descripción:"))
        self.labelFechaApertura.setText(_translate("MainWindow", "Fecha de Apertura:"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar"))
        self.labelEliminar.setText(_translate("MainWindow", "Eliminar Expediente"))
        self.labelEliminarId.setText(_translate("MainWindow", "ID Expediente:"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnRegresar.setText(_translate("MainWindow", "Volver al Menú"))
