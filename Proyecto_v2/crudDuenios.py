# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crudDuenios.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(370, 530, 75, 23))
        self.btnRegresar.setObjectName("btnRegresar")
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 771, 481))
        self.tabWidget.setMinimumSize(QtCore.QSize(771, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.label_2 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 371, 61))
        self.label_2.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_2.setObjectName("label_2")
        self.btnAgrega = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.btnAgrega.setGeometry(QtCore.QRect(340, 350, 75, 23))
        self.btnAgrega.setObjectName("btnAgrega")
        self.layoutWidget = QtWidgets.QWidget(self.tabWidgetPage1)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 110, 271, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.txtApMat = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtApMat.setObjectName("txtApMat")
        self.gridLayout.addWidget(self.txtApMat, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.txtApPat = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtApPat.setObjectName("txtApPat")
        self.gridLayout.addWidget(self.txtApPat, 3, 1, 1, 1)
        self.txtNombre = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNombre.setObjectName("txtNombre")
        self.gridLayout.addWidget(self.txtNombre, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.txtCorreo = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtCorreo.setObjectName("txtCorreo")
        self.gridLayout.addWidget(self.txtCorreo, 6, 1, 1, 1)
        self.txtTel = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtTel.setObjectName("txtTel")
        self.gridLayout.addWidget(self.txtTel, 5, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.splitter = QtWidgets.QSplitter(self.tabWidgetPage2)
        self.splitter.setGeometry(QtCore.QRect(280, 140, 156, 35))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btnElimina = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.btnElimina.setGeometry(QtCore.QRect(470, 410, 75, 23))
        self.btnElimina.setObjectName("btnElimina")
        self.label_9 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_9.setGeometry(QtCore.QRect(220, 0, 391, 71))
        self.label_9.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_9.setObjectName("label_9")
        self.tblEliminar = QtWidgets.QTableWidget(self.tabWidgetPage2)
        self.tblEliminar.setGeometry(QtCore.QRect(70, 90, 641, 301))
        self.tblEliminar.setObjectName("tblEliminar")
        self.tblEliminar.setColumnCount(6)
        self.tblEliminar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminar.setHorizontalHeaderItem(5, item)
        self.label_19 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_19.setGeometry(QtCore.QRect(220, 410, 111, 16))
        self.label_19.setObjectName("label_19")
        self.txtIDEliminar = QtWidgets.QLineEdit(self.tabWidgetPage2)
        self.txtIDEliminar.setGeometry(QtCore.QRect(340, 410, 113, 20))
        self.txtIDEliminar.setObjectName("txtIDEliminar")
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.label_10 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_10.setGeometry(QtCore.QRect(270, 70, 191, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_11.setGeometry(QtCore.QRect(160, 10, 471, 51))
        self.label_11.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_11.setObjectName("label_11")
        self.txtIDUp = QtWidgets.QLineEdit(self.tabWidgetPage3)
        self.txtIDUp.setGeometry(QtCore.QRect(290, 100, 113, 20))
        self.txtIDUp.setObjectName("txtIDUp")
        self.btnBuscarUp = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.btnBuscarUp.setGeometry(QtCore.QRect(430, 100, 75, 23))
        self.btnBuscarUp.setObjectName("btnBuscarUp")
        self.label_12 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_12.setGeometry(QtCore.QRect(260, 100, 21, 21))
        self.label_12.setObjectName("label_12")
        self.btnActualizar = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.btnActualizar.setGeometry(QtCore.QRect(350, 350, 75, 23))
        self.btnActualizar.setObjectName("btnActualizar")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabWidgetPage3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(240, 150, 281, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.txtTelUp = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtTelUp.setObjectName("txtTelUp")
        self.gridLayout_2.addWidget(self.txtTelUp, 5, 1, 1, 1)
        self.txtApMatUp = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtApMatUp.setObjectName("txtApMatUp")
        self.gridLayout_2.addWidget(self.txtApMatUp, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)
        self.txtCorreoUp = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtCorreoUp.setObjectName("txtCorreoUp")
        self.gridLayout_2.addWidget(self.txtCorreoUp, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)
        self.txtApPatUp = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtApPatUp.setObjectName("txtApPatUp")
        self.gridLayout_2.addWidget(self.txtApPatUp, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.txtNombreUp = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtNombreUp.setObjectName("txtNombreUp")
        self.gridLayout_2.addWidget(self.txtNombreUp, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.label_13 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.label_13.setGeometry(QtCore.QRect(280, 10, 271, 71))
        self.label_13.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_13.setObjectName("label_13")
        self.tblConsultar = QtWidgets.QTableWidget(self.tabWidgetPage4)
        self.tblConsultar.setGeometry(QtCore.QRect(90, 140, 641, 301))
        self.tblConsultar.setObjectName("tblConsultar")
        self.tblConsultar.setColumnCount(6)
        self.tblConsultar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultar.setHorizontalHeaderItem(5, item)
        self.txtIDConsulta = QtWidgets.QLineEdit(self.tabWidgetPage4)
        self.txtIDConsulta.setGeometry(QtCore.QRect(210, 90, 113, 20))
        self.txtIDConsulta.setObjectName("txtIDConsulta")
        self.label_20 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.label_20.setGeometry(QtCore.QRect(140, 90, 61, 16))
        self.label_20.setObjectName("label_20")
        self.btnBuscar = QtWidgets.QPushButton(self.tabWidgetPage4)
        self.btnBuscar.setGeometry(QtCore.QRect(360, 90, 75, 23))
        self.btnBuscar.setObjectName("btnBuscar")
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar"))
        self.label.setText(_translate("MainWindow", "Dueños"))
        self.label_2.setText(_translate("MainWindow", "Agregar Dueño"))
        self.btnAgrega.setText(_translate("MainWindow", "Agregar"))
        self.label_7.setText(_translate("MainWindow", "Teléfono:"))
        self.label_5.setText(_translate("MainWindow", "Apellido paterno:"))
        self.label_4.setText(_translate("MainWindow", "Apellido materno:"))
        self.label_17.setText(_translate("MainWindow", "Correo:"))
        self.label_3.setText(_translate("MainWindow", "Nombre:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Añadir"))
        self.btnElimina.setText(_translate("MainWindow", "Eliminar"))
        self.label_9.setText(_translate("MainWindow", "Eliminar Dueño"))
        item = self.tblEliminar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Dueño"))
        item = self.tblEliminar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblEliminar.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido paterno"))
        item = self.tblEliminar.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apellido materno"))
        item = self.tblEliminar.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Teléfono"))
        item = self.tblEliminar.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Correo"))
        self.label_19.setText(_translate("MainWindow", "Ingrese ID a eliminar:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Eliminar"))
        self.label_10.setText(_translate("MainWindow", "Ingrese ID del dueño a actualizar:"))
        self.label_11.setText(_translate("MainWindow", "Actualizar Dueño"))
        self.btnBuscarUp.setText(_translate("MainWindow", "Buscar"))
        self.label_12.setText(_translate("MainWindow", "ID"))
        self.btnActualizar.setText(_translate("MainWindow", "Actualizar"))
        self.label_8.setText(_translate("MainWindow", "Teléfono:"))
        self.label_16.setText(_translate("MainWindow", "Apellido materno:"))
        self.label_15.setText(_translate("MainWindow", "Apellido paterno:"))
        self.label_14.setText(_translate("MainWindow", "Nombre:"))
        self.label_18.setText(_translate("MainWindow", "Correo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Actualizar"))
        self.label_13.setText(_translate("MainWindow", "Dueños"))
        item = self.tblConsultar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Dueño"))
        item = self.tblConsultar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblConsultar.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido paterno"))
        item = self.tblConsultar.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apellido materno"))
        item = self.tblConsultar.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Teléfono"))
        item = self.tblConsultar.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Correo"))
        self.label_20.setText(_translate("MainWindow", "Ingrese ID:"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("MainWindow", "Consultar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
