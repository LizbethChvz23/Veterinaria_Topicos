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
        pass

    def abrir_mascotas(self):
        pass

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Login()
    form.show()
    sys.exit(app.exec())
