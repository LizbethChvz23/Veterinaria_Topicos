# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Personal\Documents\Topicos\Proyecto_v2\crudVeterinarios.ui'
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 781, 471))
        self.tabWidget.setMinimumSize(QtCore.QSize(771, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.label_2 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 411, 61))
        self.label_2.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_2.setObjectName("label_2")
        self.btnAgregaV = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.btnAgregaV.setGeometry(QtCore.QRect(370, 370, 75, 23))
        self.btnAgregaV.setObjectName("btnAgregaV")
        self.layoutWidget = QtWidgets.QWidget(self.tabWidgetPage1)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 110, 225, 178))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.txtNomV = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNomV.setObjectName("txtNomV")
        self.gridLayout.addWidget(self.txtNomV, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.txtApPatV = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtApPatV.setObjectName("txtApPatV")
        self.gridLayout.addWidget(self.txtApPatV, 1, 1, 1, 1)
        self.txtApMatV = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtApMatV.setObjectName("txtApMatV")
        self.gridLayout.addWidget(self.txtApMatV, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.txtEspV = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtEspV.setObjectName("txtEspV")
        self.gridLayout.addWidget(self.txtEspV, 3, 1, 1, 1)
        self.txtTelV = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtTelV.setObjectName("txtTelV")
        self.gridLayout.addWidget(self.txtTelV, 4, 1, 1, 1)
        self.txtCorreoV = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtCorreoV.setObjectName("txtCorreoV")
        self.gridLayout.addWidget(self.txtCorreoV, 5, 1, 1, 1)
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
        self.btnEliminarV = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.btnEliminarV.setGeometry(QtCore.QRect(490, 400, 75, 23))
        self.btnEliminarV.setObjectName("btnEliminarV")
        self.label_9 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_9.setGeometry(QtCore.QRect(210, 10, 411, 71))
        self.label_9.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_9.setObjectName("label_9")
        self.tblEliminaV = QtWidgets.QTableWidget(self.tabWidgetPage2)
        self.tblEliminaV.setGeometry(QtCore.QRect(0, 80, 761, 301))
        self.tblEliminaV.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblEliminaV.setObjectName("tblEliminaV")
        self.tblEliminaV.setColumnCount(7)
        self.tblEliminaV.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminaV.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminaV.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminaV.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminaV.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminaV.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminaV.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEliminaV.setHorizontalHeaderItem(6, item)
        self.label_3 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_3.setGeometry(QtCore.QRect(160, 400, 191, 16))
        self.label_3.setObjectName("label_3")
        self.txtIDEliminaV = QtWidgets.QLineEdit(self.tabWidgetPage2)
        self.txtIDEliminaV.setGeometry(QtCore.QRect(350, 400, 113, 20))
        self.txtIDEliminaV.setObjectName("txtIDEliminaV")
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
        self.txtIDBuscaUpV = QtWidgets.QLineEdit(self.tabWidgetPage3)
        self.txtIDBuscaUpV.setGeometry(QtCore.QRect(350, 90, 113, 20))
        self.txtIDBuscaUpV.setObjectName("txtIDBuscaUpV")
        self.btnBuscaUpV = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.btnBuscaUpV.setGeometry(QtCore.QRect(490, 90, 75, 23))
        self.btnBuscaUpV.setObjectName("btnBuscaUpV")
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
        self.txtNomUV = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtNomUV.setObjectName("txtNomUV")
        self.gridLayout_2.addWidget(self.txtNomUV, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.txtApPatUV = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtApPatUV.setObjectName("txtApPatUV")
        self.gridLayout_2.addWidget(self.txtApPatUV, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.txtApMatUV = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtApMatUV.setObjectName("txtApMatUV")
        self.gridLayout_2.addWidget(self.txtApMatUV, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.txtEspUV = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtEspUV.setObjectName("txtEspUV")
        self.gridLayout_2.addWidget(self.txtEspUV, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.txtTelUV = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtTelUV.setObjectName("txtTelUV")
        self.gridLayout_2.addWidget(self.txtTelUV, 4, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 5, 0, 1, 1)
        self.txtCorreoUV = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtCorreoUV.setObjectName("txtCorreoUV")
        self.gridLayout_2.addWidget(self.txtCorreoUV, 5, 1, 1, 1)
        self.btnActualizaV = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.btnActualizaV.setGeometry(QtCore.QRect(360, 350, 75, 23))
        self.btnActualizaV.setObjectName("btnActualizaV")
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.label_13 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.label_13.setGeometry(QtCore.QRect(290, 0, 271, 71))
        self.label_13.setStyleSheet("font: 75 36pt \"Comic Sans\";")
        self.label_13.setObjectName("label_13")
        self.tblConsultarV = QtWidgets.QTableWidget(self.tabWidgetPage4)
        self.tblConsultarV.setGeometry(QtCore.QRect(10, 120, 761, 301))
        self.tblConsultarV.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblConsultarV.setObjectName("tblConsultarV")
        self.tblConsultarV.setColumnCount(7)
        self.tblConsultarV.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarV.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarV.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarV.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarV.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarV.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarV.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarV.setHorizontalHeaderItem(6, item)
        self.txtBuscaConV = QtWidgets.QLineEdit(self.tabWidgetPage4)
        self.txtBuscaConV.setGeometry(QtCore.QRect(300, 80, 113, 20))
        self.txtBuscaConV.setObjectName("txtBuscaConV")
        self.btnBuscaConsultarV = QtWidgets.QPushButton(self.tabWidgetPage4)
        self.btnBuscaConsultarV.setGeometry(QtCore.QRect(440, 80, 75, 23))
        self.btnBuscaConsultarV.setObjectName("btnBuscaConsultarV")
        self.label_21 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.label_21.setGeometry(QtCore.QRect(150, 80, 151, 16))
        self.label_21.setObjectName("label_21")
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
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Veterinarios"))
        self.label_2.setText(_translate("MainWindow", "Agregar veterinario"))
        self.btnAgregaV.setText(_translate("MainWindow", "Agregar"))
        self.label_4.setText(_translate("MainWindow", "Nombre:"))
        self.label_5.setText(_translate("MainWindow", "Apellido paterno:"))
        self.label_6.setText(_translate("MainWindow", "Apellido materno:"))
        self.label_19.setText(_translate("MainWindow", "Teléfono:"))
        self.label_7.setText(_translate("MainWindow", "Especialidad:"))
        self.label_20.setText(_translate("MainWindow", "Correo:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Añadir"))
        self.btnEliminarV.setText(_translate("MainWindow", "Eliminar"))
        self.label_9.setText(_translate("MainWindow", "Eliminar veterinario"))
        item = self.tblEliminaV.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID "))
        item = self.tblEliminaV.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblEliminaV.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tblEliminaV.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apellido materno"))
        item = self.tblEliminaV.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Especialidad"))
        item = self.tblEliminaV.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Teléfono"))
        item = self.tblEliminaV.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Correo"))
        self.label_3.setText(_translate("MainWindow", "Ingrese ID de veterinario a eliminar:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Eliminar"))
        self.label_10.setText(_translate("MainWindow", "Ingrese ID del veterinario a actualizar"))
        self.label_11.setText(_translate("MainWindow", "Actualizar veterinario"))
        self.btnBuscaUpV.setText(_translate("MainWindow", "Buscar"))
        self.label_12.setText(_translate("MainWindow", "ID"))
        self.label_8.setText(_translate("MainWindow", "Nombre:"))
        self.label_14.setText(_translate("MainWindow", "Apellido paterno:"))
        self.label_15.setText(_translate("MainWindow", "Apellido materno:"))
        self.label_16.setText(_translate("MainWindow", "Especialidad:"))
        self.label_17.setText(_translate("MainWindow", "Teléfono:"))
        self.label_18.setText(_translate("MainWindow", "Correo:"))
        self.btnActualizaV.setText(_translate("MainWindow", "Actualizar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Actualizar"))
        self.label_13.setText(_translate("MainWindow", "Veterinarios"))
        item = self.tblConsultarV.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID "))
        item = self.tblConsultarV.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblConsultarV.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tblConsultarV.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apellido materno"))
        item = self.tblConsultarV.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Especialidad"))
        item = self.tblConsultarV.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Teléfono"))
        item = self.tblConsultarV.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Correo"))
        self.btnBuscaConsultarV.setText(_translate("MainWindow", "Buscar"))
        self.label_21.setText(_translate("MainWindow", "IngreseID del veterinario:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("MainWindow", "Conultar"))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar"))