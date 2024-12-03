import sys
import os
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "loginV.ui")
        loadUi(arch, self)
        self.setWindowTitle('Login')
        self.btnIngresar.clicked.connect(self.abrir_menu)
        self.txtContrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnSalir.clicked.connect(self.salir_aplicacion)
        
    def salir_aplicacion(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar salida",
            "¿Estás seguro de que deseas salir?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            QApplication.quit() 
    def abrir_menu(self):
        usuario = self.txtUsuario.text().strip()
        contrasena = self.txtContrasenia.text().strip()
        tipo_usuario = self.validar_login(usuario, contrasena)
        if tipo_usuario:
            QMessageBox.information(self, "Login", f"Bienvenido {tipo_usuario.upper()}")
            self.menu = Menu(tipo_usuario)  
            self.menu.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def conectar_bd(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Veterinaria"
            )
            return conn
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error al conectar con la base de datos: {e}")
            return None

    def validar_login(self, usuario, contrasena):
        conn = self.conectar_bd()
        if not conn:
            return None

        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT tipo_usuario FROM Usuarios WHERE nombre_usuario = %s AND contrasena = %s"
            cursor.execute(query, (usuario, contrasena))
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            return resultado['tipo_usuario'] if resultado else None
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error al realizar la consulta: {e}")
            return None        

class Menu(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Menu, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "menu.ui")
        loadUi(arch, self)
        self.setWindowTitle('Menú')
        self.tipo_usuario = tipo_usuario
        self.configurar_botones()
        self.btnUsuarios.clicked.connect(self.abrir_usuarios)
        self.btnDuenios.clicked.connect(self.abrir_duenios)
        self.btnMascotas.clicked.connect(self.abrir_mascotas)
        self.btnVeterinarios.clicked.connect(self.abrir_veterinarios)
        self.btnExpedientes.clicked.connect(self.abrir_expedientes)
        self.btnCitas.clicked.connect(self.abrir_citas)
        self.btnSesion.clicked.connect(self.cerrar_sesion)
    def configurar_botones(self):
        if self.tipo_usuario.upper() == "ADMINISTRADOR":
            self.btnUsuarios.setEnabled(True)
            self.btnDuenios.setEnabled(True)
            self.btnMascotas.setEnabled(True)
            self.btnVeterinarios.setEnabled(True)
            self.btnExpedientes.clicked.connect(self.abrir_expedientes)
            self.btnCitas.clicked.connect(self.abrir_citas)
        elif self.tipo_usuario.upper() == "VETERINARIO":
            self.btnUsuarios.setEnabled(False)
            self.btnDuenios.setEnabled(True)
            self.btnMascotas.setEnabled(True)
            self.btnVeterinarios.setEnabled(False)
            self.btnExpedientes.clicked.connect(self.abrir_expedientes)
        elif self.tipo_usuario.upper() == "RECEPCIONISTA":
            self.btnUsuarios.setEnabled(False)
            self.btnDuenios.setEnabled(True)
            self.btnMascotas.setEnabled(True)
            self.btnVeterinarios.setEnabled(True)
            self.btnCitas.clicked.connect(self.abrir_citas)
        else:
            self.btnUsuarios.setEnabled(False)
            self.btnDuenios.setEnabled(False)
            self.btnMascotas.setEnabled(False)
            self.btnVeterinarios.setEnabled(False)

    def cerrar_sesion(self):
        self.login = Login() 
        self.login.show() 
        self.close() 

    def abrir_usuarios(self):
        pass

    def abrir_duenios(self):
        pass

    def abrir_mascotas(self):
        pass

    def abrir_veterinarios(self):
        pass

    def abrir_expedientes(self):
        pass
    
    def abrir_citas(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Login()
    form.show()
    sys.exit(app.exec())
