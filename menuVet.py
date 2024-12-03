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
        self.menu = Usuarios(self.tipo_usuario)
        self.menu.show()
        self.close()

    def abrir_duenios(self):
        self.menu = Duenios(self.tipo_usuario)
        self.menu.show()
        self.close()

    def abrir_mascotas(self):
        self.menu = Mascotas(self.tipo_usuario)
        self.menu.show()
        self.close()

    def abrir_veterinarios(self):
        self.menu = Veterinarios(self.tipo_usuario)
        self.menu.show()
        self.close()

    def abrir_expedientes(self):
        pass
    
    def abrir_citas(self):
        pass



class Usuarios(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Usuarios, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudUsuarios.ui")
        loadUi(arch, self)
        self.setWindowTitle('Usuarios')
        self.tabWidget.setCurrentIndex(0)
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.tipo_usuario = tipo_usuario
        self.btnAgregaU.clicked.connect(self.aniadirUsuario)    
        self.tabWidget.currentChanged.connect(self.tab_seleccionada)
        self.btnElimina.clicked.connect(self.eliminarUsuario)    
        self.btnBuscarUp.clicked.connect(self.rellenarCampos)   
        self.btnBuscarConsulta.clicked.connect(self.consultarUsuario)   
        self.cbxTipo.currentIndexChanged.connect(self.validar_campo_id_vinculado)
        self.cbxTipoUp.currentIndexChanged.connect(self.validar_campo_id_vinculadoUP)
    def validar_campo_id_vinculado(self):
        tipo_usuario = self.cbxTipo.currentText()        
        if tipo_usuario.lower() == "veterinario":
            self.txtIDVinculado.setEnabled(True)
            self.txtIDVinculado.setPlaceholderText("Ingrese el ID de vínculo")
        else:
            self.txtIDVinculado.setEnabled(False) 
            self.txtIDVinculado.clear()  
            self.txtIDVinculado.setPlaceholderText("")
    def validar_campo_id_vinculadoUP(self):        
        tipo_usuario = self.cbxTipoUp.currentText()

        if tipo_usuario.lower() == "veterinario":
            self.txtIDVincUp.setEnabled(True)
            self.txtIDVincUp.setPlaceholderText("Ingrese el ID de vínculo")
        else:
            self.txtIDVincUp.setEnabled(False)
            self.txtIDVincUp.clear()
            self.txtIDVincUp.setPlaceholderText("")
    def tab_seleccionada(self, index):        
        if index == 0:
            self.limpiar_etiquetas()        
        elif index == 1:
            self.inicializarTabla(self.tblElim)
            self.limpiar_etiquetas()
        elif index == 3:
            self.inicializarTabla(self.tblConsulta)
            self.limpiar_etiquetas()
        else:
            self.limpiar_etiquetas()
    
    def conectar_bd(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="veterinaria"
            )
            return conn
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error al conectar con la base de datos: {e}")
            return None
               
    def aniadirUsuario(self):
        nombre_usuario = self.txtNombre.text().strip()
        contrasena = self.txtContrasenia.text().strip()
        tipo_usuario = self.cbxTipo.currentText()
        id_vinculado = self.txtIDVinculado.text().strip()
        if not nombre_usuario or not contrasena:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete los campos de nombre de usuario y contraseña.")
            return
        if tipo_usuario == "veterinario":
            if not id_vinculado:
                QMessageBox.warning(self, "ID Vinculado vacío", "El campo ID Vinculado es obligatorio para usuarios de tipo veterinario.")
                return
            if not id_vinculado.isdigit():
                QMessageBox.warning(self, "ID Vinculado inválido", "El campo ID Vinculado debe contener solo números enteros.")
                return
        id_vinculado_int = None
        if id_vinculado:
            if id_vinculado.isdigit():
                id_vinculado_int = int(id_vinculado)
            else:
                QMessageBox.warning(self, "ID Vinculado inválido", "El campo ID Vinculado debe contener solo números enteros.")
                return

        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM USUARIOS WHERE nombre_usuario = %s", (nombre_usuario,))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Usuario duplicado", "El nombre de usuario ya está registrado. Por favor, elija otro.")
                conn.close()
                return
            if tipo_usuario == "veterinario":
                cursor.execute("SELECT COUNT(*) FROM VETERINARIOS")
                veterinarios_registrados = cursor.fetchone()[0]                
                if veterinarios_registrados == 0:
                    QMessageBox.warning(self, "Sin veterinarios", "No se puede registrar un usuario veterinario. No hay veterinarios registrados.")
                    conn.close()
                    return
                cursor.execute("SELECT COUNT(*) FROM VETERINARIOS WHERE id_veterinario = %s", (id_vinculado_int,))
                if cursor.fetchone()[0] == 0:
                    QMessageBox.warning(self, "ID Vinculado inválido", "El ID Vinculado no coincide con ningún veterinario registrado.")
                    conn.close()
                    return
            query = """INSERT INTO USUARIOS (nombre_usuario, contrasena, tipo_usuario, id_vinculado) 
                    VALUES (%s, %s, %s, %s)"""
            data = (nombre_usuario, contrasena, tipo_usuario, id_vinculado_int)

            cursor.execute(query, data)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente.")
            self.limpiar_etiquetas()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo registrar el usuario.\n{e}")

    def inicializarTabla(self, tbl):
        try:            
            conn = self.conectar_bd()
            cursor = conn.cursor()            
            query = "SELECT id_usuario, nombre_usuario, contrasena, tipo_usuario, id_vinculado FROM USUARIOS"
            cursor.execute(query)
            registros = cursor.fetchall()
            tbl.setColumnCount(5)
            tbl.setColumnCount(5)
            tbl.setRowCount(len(registros))                        
            for fila, registro in enumerate(registros):
                for columna, valor in enumerate(registro):
                    tbl.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(valor)))
            
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla.\n{e}")    
    
    def eliminarUsuario(self):        
        id_usuario = self.txtElimina.text()        
        
        if not id_usuario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de usuario que desea eliminar.")
            return
        
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            QMessageBox.warning(self, "Error", "El ID de usuario debe ser un número entero.")
            self.txtElimina.setText("")
            return        
        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()
            confirmacion = QMessageBox.question(
                self, "Confirmación", 
                f"¿Está seguro de que desea eliminar el usuario '{id_usuario}'?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            
            if confirmacion == QMessageBox.Yes:                
                query = "DELETE FROM usuarios WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario,))                
                conn.commit()

                if cursor.rowcount > 0:
                    QMessageBox.information(self, "Éxito", f"Usuario '{id_usuario}' eliminado exitosamente.")
                    self.inicializarTabla(self.tblElim)
                    self.txtElimina.setText("")
                else:
                    QMessageBox.warning(self, "Error", f"No se encontró el usuario '{id_usuario}'.")            
                    self.txtElimina.setText("")
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el usuario.\n{e}")


    def rellenarCampos(self):
        id_usuario = self.txtBuscaID.text().strip()
        if not id_usuario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del usuario que desea buscar.")
            return
        if not id_usuario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del usuario debe ser un número.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return 
            query = "SELECT nombre_usuario, contrasena, tipo_usuario, id_vinculado FROM usuarios WHERE id_usuario = %s"
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (int(id_usuario),))
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            if resultado:
                self.txtNombreUp.setText(resultado['nombre_usuario'])
                self.txtContraseniaUp.setText(resultado['contrasena'])
                self.cbxTipoUp.setCurrentText(resultado['tipo_usuario'])
                if resultado['id_vinculado'] is not None:
                    self.txtIDVincUp.setText(str(resultado['id_vinculado']))
                else:
                    self.txtIDVincUp.setText("")

                QMessageBox.information(self, "Éxito", "Datos del usuario cargados correctamente.")
                self.btnActualizar.clicked.connect(self.actualizarUsuario)
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró un usuario con el ID: {id_usuario}")

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")

    def actualizarUsuario(self):        
        id_usuario_original = self.txtBuscaID.text().strip() 
        nombre_usuario = self.txtNombreUp.text().strip()
        contrasena = self.txtContraseniaUp.text().strip()
        tipo_usuario = self.cbxTipoUp.currentText().strip()
        id_vinculado = self.txtIDVincUp.text().strip()
        if not id_usuario_original:
            QMessageBox.warning(self, "Error", "El campo ID no puede estar vacío.")
            return

        if not nombre_usuario or not contrasena or not tipo_usuario:
            QMessageBox.warning(self, "Error", "Todos los campos excepto 'ID' son obligatorios.")
            return

        if tipo_usuario == "veterinario":
            if not id_vinculado:
                QMessageBox.warning(self, "Error", "El campo ID Vinculado es obligatorio para usuarios de tipo veterinario.")
                return
            if not id_vinculado.isdigit():
                QMessageBox.warning(self, "Error", "El campo ID Vinculado debe ser un número entero.")
                return

        try:
            conn = self.conectar_bd()
            if not conn:
                return 

            cursor = conn.cursor()
            cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre_usuario = %s AND id_usuario != %s", 
                        (nombre_usuario, int(id_usuario_original)))
            usuario_duplicado = cursor.fetchone()
            if usuario_duplicado:
                QMessageBox.warning(self, "Error", "El nombre de usuario ya está en uso. Por favor, elija otro.")
                cursor.close()
                conn.close()
                return
            if tipo_usuario == "veterinario":
                cursor.execute("SELECT COUNT(*) FROM veterinarios WHERE id_veterinario = %s", (int(id_vinculado),))
                if cursor.fetchone()[0] == 0:
                    QMessageBox.warning(self, "Error", "El ID Vinculado no coincide con ningún veterinario registrado.")
                    cursor.close()
                    conn.close()
                    return
            query = """UPDATE usuarios 
                    SET nombre_usuario = %s, contrasena = %s, tipo_usuario = %s, id_vinculado = %s 
                    WHERE id_usuario = %s"""
            
            data = (nombre_usuario, contrasena, tipo_usuario, 
                    int(id_vinculado) if id_vinculado else None, int(id_usuario_original))
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()
            QMessageBox.information(self, "Éxito", "Usuario actualizado exitosamente.")
            self.limpiar_etiquetas()

        except ValueError as ve:
            QMessageBox.critical(self, "Error", f"Valor inválido: {ve}")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el usuario. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")

    def limpiar_etiquetas(self):
        self.txtBuscaID.setText("")
        self.txtNombreUp.setText("")
        self.txtContraseniaUp.setText("")
        self.cbxTipoUp.currentText()
        self.txtIDVincUp.setText("")
        self.txtNombre.setText("")
        self.txtContrasenia.setText("")
        self.cbxTipoUp.currentText()
        self.txtIDVinculado.setText("")
    
    def consultarUsuario(self):
        id_usuario = self.txtBuscaConsulta.text().strip()
        if not id_usuario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de usuario que desea consultar.")
            return
        if not id_usuario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del usuario debe ser un número.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return  
            cursor = conn.cursor()
            query = """SELECT id_usuario, nombre_usuario, contrasena, tipo_usuario, id_vinculado 
                    FROM usuarios 
                    WHERE id_usuario = %s"""
            cursor.execute(query, (int(id_usuario),))
            registro = cursor.fetchone()
            cursor.close()
            conn.close()

            if registro:
                self.tblConsulta.setRowCount(1)
                self.tblConsulta.setColumnCount(5)
                encabezados = ["ID Usuario", "Nombre Usuario", "Contraseña", "Tipo Usuario", "ID Vinculado"]
                self.tblConsulta.setHorizontalHeaderLabels(encabezados)
                for columna, valor in enumerate(registro):
                    self.tblConsulta.setItem(0, columna, QtWidgets.QTableWidgetItem(str(valor)))

                QMessageBox.information(self, "Éxito", "Usuario consultado correctamente.")
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró un usuario con el ID: {id_usuario}")

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")    
                                    
    def abrir_menu(self):
        self.menu = Menu(self.tipo_usuario) 
        self.menu.show()
        self.close()
   
class Veterinarios(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Veterinarios, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudVeterinarios.ui")
        loadUi(arch, self)
        self.setWindowTitle('Veterinarios')
        self.tipo_usuario = tipo_usuario
        self.configurar_permisos()        
        self.tabWidget.setCurrentIndex(0)
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.tabWidget.currentChanged.connect(self.tab_seleccionada)
        self.btnAgregaV.clicked.connect(self.aniadirVet)
        self.btnEliminarV.clicked.connect(self.eliminarVet)
        self.btnBuscaUpV.clicked.connect(self.rellenarCampos)
        self.btnBuscaConsultarV.clicked.connect(self.consultarUsuario)
                                
    def conectar_bd(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="veterinaria"
            )
            return conn
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error al conectar con la base de datos: {e}")
            return None        
    
    def tab_seleccionada(self, index):        
        if index == 0:
            self.limpiar_etiquetas()     
            self.txtBuscaConV.setText("")   
        elif index == 1:
            self.inicializarTabla(self.tblEliminaV)
            self.limpiar_etiquetas()
            self.txtBuscaConV.setText("")
        elif index == 3:
            self.inicializarTabla(self.tblConsultarV)
            self.limpiar_etiquetas()
            self.txtBuscaConV.setText("")
        else:
            self.limpiar_etiquetas()
    
    def inicializarTabla(self, tbl):
        try:            
            conn = self.conectar_bd()
            cursor = conn.cursor()            
            query = "SELECT id_veterinario, nombre, apellidoP, apellidoM, especialidad, telefono, correo FROM veterinarios"
            cursor.execute(query)
            registros = cursor.fetchall()
                
            tbl.setColumnCount(7)
            tbl.setColumnCount(7)
            tbl.setRowCount(len(registros))                        
            for fila, registro in enumerate(registros):
                for columna, valor in enumerate(registro):
                    tbl.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(valor)))
            
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla.\n{e}") 
    
    def limpiar_etiquetas(self):        
        self.txtIDBuscaUpV.setText("")
        self.txtIDEliminaV.setText("")            
        self.txtNomV.setText("")
        self.txtApPatV.setText("")
        self.txtApMatV.setText("")
        self.txtEspV.setText("")
        self.txtTelV.setText("")
        self.txtCorreoV.setText("")        
        self.txtNomUV.setText("")        
        self.txtApPatUV.setText("")
        self.txtApMatUV.setText("")
        self.txtEspUV.setText("")
        self.txtTelUV.setText("")
        self.txtCorreoUV.setText("")

    def configurar_permisos(self):
        if self.tipo_usuario.upper() == "RECEPCIONISTA":
            self.tabWidget.setTabEnabled(0, False) 
            self.tabWidget.setTabEnabled(1, False) 
            self.tabWidget.setTabEnabled(2, False) 
            self.tabWidget.setTabEnabled(3, True)  
        else:
            for i in range(self.tabWidget.count()):
                self.tabWidget.setTabEnabled(i, True)

    def aniadirVet(self):
        nombre = self.txtNomV.text()
        apellidoP = self.txtApPatV.text()
        apellidoM = self.txtApMatV.text()
        especialidad = self.txtEspV.text()
        telefono = self.txtTelV.text()
        correo = self.txtCorreoV.text()
        if not nombre or not apellidoP or not apellidoM or not correo:
            QMessageBox.warning(self, "Error", "Campos vacíos.")
            return
        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: usuario@ejemplo.com).")
            return
        if telefono and (not telefono.isdigit() or len(telefono) != 10):
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return

        try:
            conn = self.conectar_bd()
            query = """INSERT INTO veterinarios (nombre, apellidoP, apellidoM, especialidad, telefono, correo) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            data = (
                nombre, 
                apellidoP, 
                apellidoM, 
                especialidad if especialidad else None, 
                telefono if telefono else None, 
                correo
            )

            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Éxito", "Veterinario registrado exitosamente.")
            self.limpiar_etiquetas()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo registrar el Veterinario.\n{e}")

        
    def eliminarVet(self):
        id_veterinario = self.txtIDEliminaV.text().strip()
        if not id_veterinario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de veterinario que desea eliminar.")
            return
        if not id_veterinario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del veterinario debe ser un número entero.")
            return

        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()
            confirmacion = QMessageBox.question(
                self,
                "Confirmación",
                f"¿Está seguro de que desea eliminar al veterinario con ID '{id_veterinario}'?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if confirmacion == QMessageBox.Yes:
                query = "DELETE FROM veterinarios WHERE id_veterinario = %s"
                cursor.execute(query, (int(id_veterinario),))
                conn.commit()

                if cursor.rowcount > 0:
                    QMessageBox.information(self, "Éxito", f"Veterinario con ID '{id_veterinario}' eliminado exitosamente.")
                    self.inicializarTabla(self.tblEliminaV)
                    self.txtIDEliminaV.setText("")
                else:
                    QMessageBox.warning(self, "Error", f"No se encontró un veterinario con ID '{id_veterinario}'.")
                    self.txtIDEliminaV.setText("")

            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el usuario.\n{e}")

    def rellenarCampos(self):
        id_veterinario = self.txtIDBuscaUpV.text().strip()
        if not id_veterinario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del usuario que desea buscar.")
            return
        if not id_veterinario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del usuario debe ser un número.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return       
            query = """SELECT id_veterinario, nombre, apellidoP, apellidoM, especialidad, telefono, correo FROM veterinarios 
                        WHERE id_veterinario = %s"""
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (int(id_veterinario),))
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            if resultado:
                self.txtNomUV.setText(resultado['nombre'])
                self.txtApPatUV.setText(resultado['apellidoP'])
                self.txtApMatUV.setText(resultado['apellidoM'])                
                if resultado['especialidad'] is not None:
                    self.txtEspUV.setText(str(resultado['especialidad']))
                else:
                    self.txtEspUV.setText("")
                    
                if resultado['telefono'] is not None:
                    self.txtTelUV.setText(str(resultado['telefono']))
                else:
                    self.txtTelUV.setText("")
                    
                self.txtCorreoUV.setText(resultado['correo'])
                
                QMessageBox.information(self, "Éxito", "Datos del veterinario cargados correctamente.")
                self.btnActualizaV.clicked.connect(self.actualizarVet)
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró el veterinario con el ID: {id_veterinario}")

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")

    def actualizarVet(self):
        id_veterinario = self.txtIDBuscaUpV.text().strip()
        nombre = self.txtNomUV.text().strip()
        apellidoP = self.txtApPatUV.text().strip()
        apellidoM = self.txtApMatUV.text().strip()
        especialidad = self.txtEspUV.text().strip()
        telefono = self.txtTelUV.text().strip()
        correo = self.txtCorreoUV.text().strip()

        if not id_veterinario or not nombre or not apellidoP or not apellidoM or not especialidad or not telefono or not correo:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        if not id_veterinario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del veterinario debe ser un número entero.")
            return
        if not (telefono.isdigit() and len(telefono) == 10):
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return
        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: pepe@ejemplo.com).")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return 
            check_query = "SELECT id_veterinario FROM veterinarios WHERE correo = %s AND id_veterinario != %s"
            cursor = conn.cursor()
            cursor.execute(check_query, (correo, int(id_veterinario)))
            existing = cursor.fetchone()

            if existing:
                QMessageBox.warning(self, "Error", "El correo ingresado ya está en uso por otro veterinario.")
                cursor.close()
                conn.close()
                return
            query = """UPDATE veterinarios 
                    SET nombre = %s, apellidoP = %s, apellidoM = %s, especialidad = %s, telefono = %s, correo = %s 
                    WHERE id_veterinario = %s"""
            data = (
                nombre,
                apellidoP,
                apellidoM,
                especialidad,
                telefono,
                correo,
                int(id_veterinario),
            )
            cursor.execute(query, data)
            conn.commit() 

            if cursor.rowcount > 0:
                QMessageBox.information(self, "Éxito", "Usuario actualizado exitosamente.")
                self.limpiar_etiquetas()
            else:
                QMessageBox.warning(self, "Error", f"No se encontró un veterinario con ID '{id_veterinario}'.")
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el usuario. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")
        
    def consultarUsuario(self):
        id_veterinario = self.txtBuscaConV.text().strip()
        if not id_veterinario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del veterinario que desea consultar.")
            return
        if not id_veterinario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del veterinario debe ser un número.")
            return
        try:
            conn = self.conectar_bd()
            if not conn:
                return  
            cursor = conn.cursor()            
            query = """SELECT id_veterinario, nombre, apellidoP, apellidoM, especialidad, telefono, correo 
                         FROM veterinarios
                        WHERE id_veterinario = %s"""
            cursor.execute(query, (int(id_veterinario),))
            registro = cursor.fetchone()
            cursor.close()
            conn.close()
            if registro:
                self.tblConsultarV.setRowCount(1)
                self.tblConsultarV.setColumnCount(7)
                encabezados = ["ID veterinario", "Nombre", "Apellido paterno","Apellido materno",
                               "Especialidad", "Teléfono", "Correo"]
                self.tblConsultarV.setHorizontalHeaderLabels(encabezados)
                for columna, valor in enumerate(registro):
                    self.tblConsultarV.setItem(0, columna, QtWidgets.QTableWidgetItem(str(valor)))
                QMessageBox.information(self, "Éxito", "Usuario consultado correctamente.")
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró un usuario con el ID: {id_veterinario}")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")    
    
    def abrir_menu(self):
        """Regresa al menú principal."""
        self.menu = Menu(self.tipo_usuario)
        self.menu.show()
        self.close()

  
class Duenios(QMainWindow):
    def __init__(self,tipo_usuario):
        super(Duenios, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudDuenios.ui")
        loadUi(arch, self)
        self.setWindowTitle('Dueños')
        self.tipo_usuario = tipo_usuario 
        self.configurar_permisos()
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.tab_seleccionada)
        self.btnAgrega.clicked.connect(self.aniadirDuenio)
        self.btnElimina.clicked.connect(self.eliminarDuenio)        
        self.btnBuscar.clicked.connect(self.consultarDuenio)
        self.btnBuscarUp.clicked.connect(self.rellenarCampos)

    def configurar_permisos(self):
        if self.tipo_usuario.upper() == "VETERINARIO":
            self.tabWidget.setTabEnabled(0, False)  
            self.tabWidget.setTabEnabled(1, False) 
            self.tabWidget.setTabEnabled(2, False) 
            self.tabWidget.setTabEnabled(3, True)   
        elif self.tipo_usuario.upper() == "RECEPCIONISTA":
            self.tabWidget.setTabEnabled(0, True) 
            self.tabWidget.setTabEnabled(1, True) 
            self.tabWidget.setTabEnabled(2, True)  
            self.tabWidget.setTabEnabled(3, True)  
        else:
            for i in range(self.tabWidget.count()):
                self.tabWidget.setTabEnabled(i, True)

    def tab_seleccionada(self, index):        
        if index == 0:
            self.limpiar_etiquetas()        
            self.txtIDConsulta.setText("")
        elif index == 1:
            self.inicializarTabla(self.tblEliminar)
            self.limpiar_etiquetas()
            self.txtIDConsulta.setText("")
        elif index == 3:
            self.inicializarTabla(self.tblConsultar)
            self.limpiar_etiquetas()
            self.txtIDConsulta.setText("")
        else:
            self.limpiar_etiquetas()
            self.txtIDConsulta.setText("")            
    
    def conectar_bd(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="veterinaria"
            )
            return conn
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error al conectar con la base de datos: {e}")
            return None
                   
    def aniadirDuenio(self):        
        nombre = self.txtNombre.text().strip()
        apellidoP = self.txtApPat.text().strip()
        apellidoM = self.txtApMat.text().strip()
        telefono = self.txtTel.text().strip()
        correo = self.txtCorreo.text().strip()

        if not nombre or not apellidoP or not apellidoM or not telefono or not correo:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: usuario@ejemplo.com).")
            return

        if not telefono.isdigit() or len(telefono) != 10:
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return

        try:
            conn = self.conectar_bd()
            query = """INSERT INTO dueños (nombre, apellidoP, apellidoM, telefono, correo) 
                        VALUES (%s, %s, %s, %s, %s)"""
            data = (nombre, apellidoP, apellidoM, telefono, correo)

            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Éxito", "Dueño registrado exitosamente.")
            self.limpiar_etiquetas()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo registrar el dueño. Error en la base de datos:\n{e}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")


    def inicializarTabla(self, tbl):
        try:            
            conn = self.conectar_bd()
            cursor = conn.cursor()            
            query = "SELECT id_dueño, nombre, apellidoP, apellidoM, telefono, correo FROM dueños"
            cursor.execute(query)
            registros = cursor.fetchall()            
            tbl.setColumnCount(6)
            tbl.setColumnCount(6)
            tbl.setRowCount(len(registros))                        
            for fila, registro in enumerate(registros):
                for columna, valor in enumerate(registro):
                    tbl.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(valor)))            
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla.\n{e}")    

    def eliminarDuenio(self):        
        id_dueño = self.txtIDEliminar.text().strip() 
        if not id_dueño:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del dueño que desea eliminar.")
            return
        if not id_dueño.isdigit():
            QMessageBox.warning(self, "Error", "El ID del dueño debe ser un número entero.")
            return

        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()
            query_check_mascotas = "SELECT COUNT(*) FROM mascotas WHERE id_dueño = %s"
            cursor.execute(query_check_mascotas, (int(id_dueño),))
            mascotas_asociadas = cursor.fetchone()[0]

            if mascotas_asociadas > 0:
                QMessageBox.warning(self, "Error", f"No se puede eliminar al dueño con ID '{id_dueño}' porque tiene {mascotas_asociadas} mascota(s) asociada(s).")
                cursor.close()
                conn.close()
                return
            confirmacion = QMessageBox.question(
                self,
                "Confirmación",
                f"¿Está seguro de que desea eliminar el dueño con ID '{id_dueño}'?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if confirmacion == QMessageBox.Yes:
                query_delete = "DELETE FROM dueños WHERE id_dueño = %s"
                cursor.execute(query_delete, (int(id_dueño),))
                conn.commit()

                if cursor.rowcount > 0:
                    QMessageBox.information(self, "Éxito", f"Dueño con ID '{id_dueño}' eliminado exitosamente.")
                    self.inicializarTabla(self.tblEliminar)
                    self.txtIDEliminar.setText("")
                else:
                    QMessageBox.warning(self, "Error", f"No se encontró un dueño con ID '{id_dueño}'.")
                    self.txtIDEliminar.setText("")

            conn.close()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar al dueño. Error en la base de datos:\n{e}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")



    def rellenarCampos(self):
        id_dueño = self.txtIDUp.text().strip()
        if not id_dueño:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del dueño que desea buscar.")
            return
        if not id_dueño.isdigit():
            QMessageBox.warning(self, "Error", "El ID del dueño debe ser un número.")
            return
        try:
            conn = self.conectar_bd()
            if not conn:
                return            
            query = """SELECT nombre, apellidoP, apellidoM, telefono, correo 
                        FROM dueños
                       WHERE id_dueño = %s"""
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (int(id_dueño),))
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            if resultado:
                self.txtNombreUp.setText(resultado['nombre'])
                self.txtApPatUp.setText(resultado['apellidoP'])
                self.txtApMatUp.setText(resultado['apellidoM'])
                self.txtTelUp.setText(resultado['telefono'])
                self.txtCorreoUp.setText(resultado['correo'])                                
                QMessageBox.information(self, "Éxito", "Datos del dueño cargados correctamente.")
                self.btnActualizar.clicked.connect(self.actualizarDuenio)
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró un dueño con el ID: {id_dueño}")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")
      
    def actualizarDuenio(self):        
        id_dueño = self.txtIDUp.text().strip()
        nombre = self.txtNombreUp.text().strip()
        apellidoP = self.txtApPatUp.text().strip()
        apellidoM = self.txtApMatUp.text().strip()
        telefono = self.txtTelUp.text().strip()
        correo = self.txtCorreoUp.text().strip()
        
        if not nombre or not apellidoP or not apellidoM or not telefono or not correo:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return
        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: usuario@ejemplo.com).")
            return
        if not telefono.isdigit() or len(telefono) != 10:
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return

            cursor = conn.cursor()
            query_verificar = "SELECT id_dueño FROM dueños WHERE correo = %s AND id_dueño != %s"
            cursor.execute(query_verificar, (correo, int(id_dueño)))
            resultado = cursor.fetchone()

            if resultado:
                QMessageBox.warning(self, "Error", "El correo ingresado ya está en uso por otro dueño.")
                cursor.close()
                conn.close()
                return
            query = """UPDATE dueños 
                    SET nombre = %s, apellidoP = %s, apellidoM = %s, telefono = %s, correo = %s 
                    WHERE id_dueño = %s"""
            data = (nombre, apellidoP, apellidoM, telefono, correo, int(id_dueño))
            cursor.execute(query, data)
            conn.commit() 
            cursor.close()
            conn.close()
            QMessageBox.information(self, "Éxito", "Dueño actualizado exitosamente.")
            self.limpiar_etiquetas()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el dueño. Error en la base de datos:\n{e}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")



    def limpiar_etiquetas(self):        
        self.txtIDUp.setText("")
        self.txtIDEliminar.setText("")
        self.txtIDUp.setText("")
        self.txtNombreUp.setText("")
        self.txtApPatUp.setText("")
        self.txtApMatUp.setText("")
        self.txtTelUp.setText("")
        self.txtCorreoUp.setText("")          
        self.txtNombre.setText("")
        self.txtApPat.setText("")
        self.txtApMat.setText("")
        self.txtTel.setText("")
        self.txtCorreo.setText("")   
                
    def consultarDuenio(self):
        id_dueño = self.txtIDConsulta.text()

        if not id_dueño:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del dueño que desea consultar.")
            return
        if not id_dueño.isdigit():
            QMessageBox.warning(self, "Error", "El ID del usuario debe ser un número.")
            return
        try:
            conn = self.conectar_bd()
            if not conn:
                return
            cursor = conn.cursor()
            query = """SELECT id_dueño, nombre, apellidoP, apellidoM, telefono, correo
                    FROM dueños 
                    WHERE id_dueño = %s"""                    
            cursor.execute(query, (int(id_dueño),))
            registro = cursor.fetchone()
            cursor.close()
            conn.close()

            if registro:
                self.tblConsultar.setRowCount(1)
                self.tblConsultar.setColumnCount(6)
                encabezados = ["ID Dueño", "Nombre", "Apellido Paterno", "Apellido Materno", "telefono","Correo"]
                self.tblConsultar.setHorizontalHeaderLabels(encabezados)
                for columna, valor in enumerate(registro):
                    self.tblConsultar.setItem(0, columna, QtWidgets.QTableWidgetItem(str(valor)))
                QMessageBox.information(self, "Éxito", "Dueño consultado correctamente.")
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró un dueño con el ID: {id_dueño}")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")    
                      
    def abrir_menu(self):
        """Regresa al menú principal."""
        self.menu = Menu(self.tipo_usuario)
        self.menu.show()
        self.close()

class Mascotas(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Mascotas, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudMascotas.ui")
        loadUi(arch, self)
        self.tipo_usuario = tipo_usuario
        self.configurar_permisos()
        self.tabWidget.setCurrentIndex(0)
        self.llenar_combobox_duenios() 
        self.btnAgregaA.clicked.connect(self.aniadir_mascota)
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.btnBuscarUp.clicked.connect(self.buscar_mascota)
        self.btnActualizar.clicked.connect(self.actualizar_mascota)
        self.btnEliminaE.clicked.connect(self.eliminarMascota)        
        self.btnBuscarCon.clicked.connect(self.consultarMascota) 
        self.tabWidget.currentChanged.connect(self.tab_seleccionada)
        
    def inicializarTabla(self, tbl):
        try:            
            conn = self.conectar_bd()
            cursor = conn.cursor()            
            query = """SELECT m.id_mascota, m.nombre, m.especie, m.raza, m.edad, m.estado, m.id_dueño, d.nombre 
                         FROM mascotas m
                        JOIN dueños d ON m.id_dueño = d.id_dueño
                         """
            cursor.execute(query)
            registros = cursor.fetchall()
            tbl.setColumnCount(8)
            tbl.setColumnCount(8)
            tbl.setRowCount(len(registros))                        
            for fila, registro in enumerate(registros):
                for columna, valor in enumerate(registro):
                    tbl.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(valor)))
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla.\n{e}")    
    
    def tab_seleccionada(self, index):        
        if index == 0:
            self.limpiar_etiquetas()        
            self.txtIDMascCon.setText("")            
        elif index == 1:
            self.inicializarTabla(self.tblEliminar)
            self.limpiar_etiquetas()
            self.txtIDMascCon.setText("")
        elif index == 3:
            self.inicializarTabla(self.tblConsultar)
            self.limpiar_etiquetas()
            self.txtIDMascCon.setText("")
        else:
            self.limpiar_etiquetas()
            self.txtIDMascCon.setText("")            
    

    def limpiar_etiquetas(self):        
        self.rdbAlta.setAutoExclusive(False)
        self.rdbRecuperacion.setAutoExclusive(False)
        self.rdbTratamiento.setAutoExclusive(False)
        self.rdbCritico.setAutoExclusive(False)
        self.txtIDMascUp.setText("")
        self.txtIDEliminar.setText("")
        self.txtNombreUp.setText("")
        self.txtEspecieUp.setText("")        
        self.txtRazaUp.setText("")
        self.txtEdadUp.setText("")
        self.rdbAltaUp.setChecked(False)
        self.rdbRecuperacionUp.setChecked(False)
        self.rdbTratamientoUp.setChecked(False)
        self.rdbCriticoUp.setChecked(False)
        self.cbxDuenioUp.currentText()    
        self.txtNombre.setText("")
        self.txtEspecie.setText("")
        self.txtRaza.setText("")
        self.txtEdad.setText("")
        self.rdbAlta.setChecked(False)
        self.rdbRecuperacion.setChecked(False)
        self.rdbTratamiento.setChecked(False)
        self.rdbCritico.setChecked(False)
        self.cbxDuenio.currentText()
    
    def configurar_permisos(self):
        if self.tipo_usuario.upper() == "VETERINARIO":
            self.tabWidget.setTabEnabled(0, False) 
            self.tabWidget.setTabEnabled(1, False) 
            self.tabWidget.setTabEnabled(2, True)  
            self.tabWidget.setTabEnabled(3, True) 
        elif self.tipo_usuario.upper() == "RECEPCIONISTA":
            self.tabWidget.setTabEnabled(0, True) 
            self.tabWidget.setTabEnabled(1, True)  
            self.tabWidget.setTabEnabled(2, True)   
            self.tabWidget.setTabEnabled(3, True) 
        else:
            for i in range(self.tabWidget.count()):
                self.tabWidget.setTabEnabled(i, True)

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

    def llenar_combobox_duenios(self):
        """Llena el combobox con los nombres de los dueños existentes en la base de datos."""
        try:
            conn = self.conectar_bd()
            if not conn:
                return
            cursor = conn.cursor()
            query = "SELECT id_dueño, CONCAT(id_dueño, ' - ', nombre, ' ', apellidoP, ' ', apellidoM) AS nombre_completo FROM Dueños"
            cursor.execute(query)
            resultados = cursor.fetchall()
            conn.close()

            self.cbxDuenio.clear()
            for id_dueño, nombre_completo in resultados:
                self.cbxDuenio.addItem(nombre_completo, id_dueño)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la lista de dueños: {e}")


    def aniadir_mascota(self):
        """Añade una nueva mascota a la base de datos."""
        nombre = self.txtNombre.text().strip()
        especie = self.txtEspecie.text().strip()
        raza = self.txtRaza.text().strip()
        edad = self.txtEdad.text().strip()
        estado = ""
        if self.rdbAlta.isChecked():
            estado = "alta"
        elif self.rdbRecuperacion.isChecked():
            estado = "recuperacion"
        elif self.rdbTratamiento.isChecked():
            estado = "tratamiento"
        elif self.rdbCritico.isChecked():
            estado = "critico"
        id_dueño = self.cbxDuenio.currentData()
        if not nombre or not especie or not estado or id_dueño is None:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos obligatorios.")
            return
        if edad and not edad.isdigit():
            QMessageBox.warning(self, "Error", "La edad debe ser un número entero.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return
            query = """
                INSERT INTO Mascotas (nombre, especie, raza, edad, estado, id_dueño) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            data = (nombre, especie, raza, int(edad) if edad else None, estado, id_dueño)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Éxito", "Mascota añadida exitosamente.")
            self.limpiar_campos()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo añadir la mascota. Error en la base de datos:\n{e}")

    def limpiar_campos(self):
        """Limpia los campos del formulario de añadir mascota."""
        self.txtNombre.clear()
        self.txtEspecie.clear()
        self.txtRaza.clear()
        self.txtEdad.clear()
        self.rdbAlta.setChecked(False)
        self.rdbRecuperacion.setChecked(False)
        self.rdbTratamiento.setChecked(False)
        self.rdbCritico.setChecked(False)
        self.cbxDuenio.setCurrentIndex(0)
    def buscar_mascota(self):
        """Busca una mascota en la base de datos por su ID, rellena los campos del formulario y selecciona el dueño en el ComboBox."""
        id_mascota = self.txtIDMascUp.text().strip()
        if not id_mascota:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la mascota a buscar.")
            return
        if not id_mascota.isdigit():
            QMessageBox.warning(self, "Error", "El ID de la mascota debe ser un número entero positivo.")
            self.txtIDMascCon.setText("")  
            return
        try:
            conn = self.conectar_bd()
            if not conn:
                return
            query_mascota = """
                SELECT nombre, especie, raza, edad, estado, id_dueño
                FROM Mascotas
                WHERE id_mascota = %s
            """
            cursor = conn.cursor()
            cursor.execute(query_mascota, (id_mascota,))
            resultado_mascota = cursor.fetchone()

            if not resultado_mascota:
                QMessageBox.warning(self, "Error", "No se encontró una mascota con el ID proporcionado.")
                conn.close()
                return
            nombre, especie, raza, edad, estado, id_dueño_actual = resultado_mascota
            self.txtNombreUp.setText(nombre)
            self.txtEspecieUp.setText(especie)
            self.txtRazaUp.setText(raza)
            self.txtEdadUp.setText(str(edad) if edad else "")
            self.rdbAltaUp.setChecked(estado == "alta")
            self.rdbRecuperacionUp.setChecked(estado == "recuperacion")
            self.rdbTratamientoUp.setChecked(estado == "tratamiento")
            self.rdbCriticoUp.setChecked(estado == "critico")
            query_duenios = """
                SELECT id_dueño, CONCAT(id_dueño, ' - ', nombre, ' ', apellidoP, ' ', apellidoM) AS nombre_completo
                FROM Dueños
            """
            cursor.execute(query_duenios)
            resultados_duenios = cursor.fetchall()
            self.cbxDuenioUp.clear()
            indice_actual = -1
            for index, (id_dueño, nombre_completo) in enumerate(resultados_duenios):
                self.cbxDuenioUp.addItem(nombre_completo, id_dueño)
                if id_dueño == id_dueño_actual:
                    indice_actual = index
            if indice_actual != -1:
                self.cbxDuenioUp.setCurrentIndex(indice_actual)

            conn.close()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda. Error en la base de datos:\n{e}")
    def actualizar_mascota(self):
        """Actualiza los datos de una mascota en la base de datos."""
        id_mascota = self.txtIDMascUp.text().strip()
        nombre = self.txtNombreUp.text().strip()
        especie = self.txtEspecieUp.text().strip()
        raza = self.txtRazaUp.text().strip()
        edad = self.txtEdadUp.text().strip()
        estado = ""
        if self.rdbAltaUp.isChecked():
            estado = "alta"
        elif self.rdbRecuperacionUp.isChecked():
            estado = "recuperacion"
        elif self.rdbTratamientoUp.isChecked():
            estado = "tratamiento"
        elif self.rdbCriticoUp.isChecked():
            estado = "critico"
        id_dueño = self.cbxDuenioUp.currentData()
        if not id_mascota:
            QMessageBox.warning(self, "Error", "El campo 'ID de la Mascota' es obligatorio.")
            return
        if not nombre:
            QMessageBox.warning(self, "Error", "El campo 'Nombre' es obligatorio.")
            return
        if not especie:
            QMessageBox.warning(self, "Error", "El campo 'Especie' es obligatorio.")
            return
        if not raza:
            QMessageBox.warning(self, "Error", "El campo 'Raza' es obligatorio.")
            return
        if not edad:
            QMessageBox.warning(self, "Error", "El campo 'Edad' es obligatorio.")
            return
        if not estado:
            QMessageBox.warning(self, "Error", "Debe seleccionar un estado de la mascota.")
            return
        if id_dueño is None:
            QMessageBox.warning(self, "Error", "Debe seleccionar un dueño para la mascota.")
            return
        if not edad.isdigit():
            QMessageBox.warning(self, "Error", "La edad debe ser un número entero.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return
            query = """
                UPDATE Mascotas
                SET nombre = %s, especie = %s, raza = %s, edad = %s, estado = %s, id_dueño = %s
                WHERE id_mascota = %s
            """
            data = (nombre, especie, raza, int(edad), estado, id_dueño, id_mascota)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Éxito", "Mascota actualizada exitosamente.")
            self.limpiar_campos_actualizacion()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar la mascota. Error en la base de datos:\n{e}")

    def eliminarMascota(self):        
        id_mascota = self.txtIDEliminar.text().strip()
        
        if not id_mascota:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la mascota que desea eliminar.")
            return
        if not id_mascota.isdigit():
            QMessageBox.warning(self, "Error", "El ID de la mascota debe ser un número entero válido.")
            self.txtIDEliminar.setText("")
            return
        
        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()
            confirmacion = QMessageBox.question(
                self,
                "Confirmación",
                f"¿Está seguro de que desea eliminar a la mascota con ID '{id_mascota}'?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if confirmacion == QMessageBox.Yes:                
                query = "DELETE FROM mascotas WHERE id_mascota = %s"
                cursor.execute(query, (id_mascota,))                
                conn.commit()
                if cursor.rowcount > 0:
                    QMessageBox.information(self, "Éxito", f"Mascota con ID '{id_mascota}' eliminada exitosamente.")
                    self.inicializarTabla(self.tblEliminar)
                    self.txtIDEliminar.setText("")
                else:
                    QMessageBox.warning(self, "Error", f"No se encontró la mascota con ID: '{id_mascota}'.")
                    self.txtIDEliminar.setText("")
            
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar la mascota.\n{e}")

    
    def consultarMascota(self):
        id_mascota = self.txtIDMascCon.text().strip()
        if not id_mascota:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la mascota que desea consultar.")
            return
        if not id_mascota.isdigit():
            QMessageBox.warning(self, "Error", "El ID de la mascota debe ser un número entero positivo.")
            self.txtIDMascCon.setText("")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return  
            cursor = conn.cursor()
            query = """
                SELECT m.id_mascota, m.nombre, m.especie, m.raza, m.edad, m.estado, m.id_dueño,
                    CONCAT(d.nombre, ' ', d.apellidoP, ' ', d.apellidoM) AS nombre_dueño
                FROM mascotas m
                JOIN dueños d ON m.id_dueño = d.id_dueño
                WHERE m.id_mascota = %s
            """
            cursor.execute(query, (int(id_mascota),))
            registro = cursor.fetchone()
            cursor.close()
            conn.close()
            if registro:
                self.tblConsultar.setRowCount(1)
                self.tblConsultar.setColumnCount(8)
                headers = ["ID Mascota", "Nombre", "Especie", "Raza", "Edad", "Estado", "ID Dueño", "Nombre Dueño"]
                self.tblConsultar.setHorizontalHeaderLabels(headers)
                for columna, valor in enumerate(registro):
                    self.tblConsultar.setItem(0, columna, QtWidgets.QTableWidgetItem(str(valor)))

                QMessageBox.information(self, "Éxito", "Mascota consultada correctamente.")
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró una mascota con el ID: {id_mascota}")
                self.txtIDMascCon.setText("")
                self.inicializarTabla(self.tblConsultar)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")

    def limpiar_campos_actualizacion(self):
        """Limpia los campos del formulario de actualización."""
        self.txtIDMascUp.clear()
        self.txtNombreUp.clear()
        self.txtEspecieUp.clear()
        self.txtRazaUp.clear()
        self.txtEdadUp.clear()
        self.rdbAltaUp.setChecked(False)
        self.rdbRecuperacionUp.setChecked(False)
        self.rdbTratamientoUp.setChecked(False)
        self.rdbCriticoUp.setChecked(False)
        self.cbxDuenioUp.setCurrentIndex(0)

    def abrir_menu(self):
        """Regresa al menú principal."""
        self.menu = Menu(self.tipo_usuario)
        self.menu.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Login()
    form.show()
    sys.exit(app.exec())
