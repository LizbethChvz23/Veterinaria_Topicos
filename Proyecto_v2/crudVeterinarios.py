# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crudveterinarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 799, 39))
        self.label.setStyleSheet("background-color:rgb(0, 49, 97);\n"
"font: 75 16pt \"Verdana\";\n"
"color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 771, 471))
        self.tabWidget.setMinimumSize(QtCore.QSize(771, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.label_2 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 411, 61))
        self.label_2.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_2.setObjectName("label_2")
        self.btnAgregaU = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.btnAgregaU.setGeometry(QtCore.QRect(370, 370, 75, 23))
        self.btnAgregaU.setObjectName("btnAgregaU")
        self.layoutWidget = QtWidgets.QWidget(self.tabWidgetPage1)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 110, 225, 178))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 4, 1, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 5, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.splitter = QtWidgets.QSplitter(self.tabWidgetPage2)
        self.splitter.setGeometry(QtCore.QRect(280, 140, 156, 35))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btnAgregaU_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.btnAgregaU_2.setGeometry(QtCore.QRect(360, 400, 75, 23))
        self.btnAgregaU_2.setObjectName("btnAgregaU_2")
        self.label_9 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_9.setGeometry(QtCore.QRect(210, 10, 411, 71))
        self.label_9.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_9.setObjectName("label_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tabWidgetPage2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 80, 761, 301))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.label_10 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_10.setGeometry(QtCore.QRect(280, 70, 191, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_11.setGeometry(QtCore.QRect(160, 10, 471, 51))
        self.label_11.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_11.setObjectName("label_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tabWidgetPage3)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 90, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.btnAgregaU_3 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.btnAgregaU_3.setGeometry(QtCore.QRect(490, 90, 75, 23))
        self.btnAgregaU_3.setObjectName("btnAgregaU_3")
        self.label_12 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_12.setGeometry(QtCore.QRect(280, 90, 31, 21))
        self.label_12.setObjectName("label_12")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabWidgetPage3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(240, 140, 281, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 4, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 5, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 5, 1, 1, 1)
        self.btnAgregaU_4 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.btnAgregaU_4.setGeometry(QtCore.QRect(360, 350, 75, 23))
        self.btnAgregaU_4.setObjectName("btnAgregaU_4")
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.tableWidget = QtWidgets.QTableWidget(self.tabWidgetPage4)
        self.tableWidget.setGeometry(QtCore.QRect(140, 90, 521, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label_13 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.label_13.setGeometry(QtCore.QRect(290, 0, 271, 71))
        self.label_13.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(380, 530, 75, 23))
        self.btnRegresar.setObjectName("btnRegresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Veterinarios"))
        self.label_2.setText(_translate("MainWindow", "Agregar veterinario"))
        self.btnAgregaU.setText(_translate("MainWindow", "Agregar"))
        self.label_4.setText(_translate("MainWindow", "Nombre:"))
        self.label_5.setText(_translate("MainWindow", "Apellido paterno:"))
        self.label_6.setText(_translate("MainWindow", "Apellido materno:"))
        self.label_19.setText(_translate("MainWindow", "Teléfono:"))
        self.label_7.setText(_translate("MainWindow", "Especialidad:"))
        self.label_20.setText(_translate("MainWindow", "Correo:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Añadir"))
        self.btnAgregaU_2.setText(_translate("MainWindow", "Eliminar"))
        self.label_9.setText(_translate("MainWindow", "Eliminar veterinario"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID "))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apellido materno"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Especialidad"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Teléfono"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Correo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Eliminar"))
        self.label_10.setText(_translate("MainWindow", "Ingrese ID del veterinario a actualizar"))
        self.label_11.setText(_translate("MainWindow", "Actualizar veterinario"))
        self.btnAgregaU_3.setText(_translate("MainWindow", "Buscar"))
        self.label_12.setText(_translate("MainWindow", "ID"))
        self.label_8.setText(_translate("MainWindow", "Nombre:"))
        self.label_14.setText(_translate("MainWindow", "Apellido paterno:"))
        self.label_15.setText(_translate("MainWindow", "Apellido materno:"))
        self.label_16.setText(_translate("MainWindow", "Especialidad:"))
        self.label_17.setText(_translate("MainWindow", "Teléfono:"))
        self.label_18.setText(_translate("MainWindow", "Correo:"))
        self.btnAgregaU_4.setText(_translate("MainWindow", "Actualizar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Actualizar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Usuario"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Correo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Contraseña"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rol"))
        self.label_13.setText(_translate("MainWindow", "Veterinarios"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("MainWindow", "Conultar"))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())