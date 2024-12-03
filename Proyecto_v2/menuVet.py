import sys
import os
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QTextCharFormat, QColor
from datetime import datetime
from PyQt5.QtCore import QDate






class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "loginV.ui")
        loadUi(arch, self)
        self.setWindowTitle('Login')
        self.btnIngresar.clicked.connect(self.abrir_menu)
        self.txtContrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        # Conexión del botón "Salir" para cerrar la aplicación
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
            QApplication.quit()  # Cierra la aplicación
    def abrir_menu(self):
        # Obtener credenciales del formulario
        usuario = self.txtUsuario.text().strip()
        contrasena = self.txtContrasenia.text().strip()
        # Validar credenciales
        tipo_usuario = self.validar_login(usuario, contrasena)
        if tipo_usuario:
            QMessageBox.information(self, "Login", f"Bienvenido {tipo_usuario.upper()}")
            self.menu = Menu(tipo_usuario)  # Pasar tipo de usuario al menú
            self.menu.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def conectar_bd(self):
        """Establece conexión con la base de datos."""
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
        
        # Guardar el tipo de usuario como atributo
        self.tipo_usuario = tipo_usuario

        # Configurar botones según el tipo de usuario
        self.configurar_botones()

        # Conexión de botones a funciones
        self.btnUsuarios.clicked.connect(self.abrir_usuarios)
        self.btnDuenios.clicked.connect(self.abrir_duenios)
        self.btnMascotas.clicked.connect(self.abrir_mascotas)
        self.btnVeterinarios.clicked.connect(self.abrir_veterinarios)
        self.btnExpedientes.clicked.connect(self.abrir_expedientes)
        self.btnCitas.clicked.connect(self.abrir_citas)
        
        # Conexión del botón de cerrar sesión
        self.btnSesion.clicked.connect(self.cerrar_sesion)  # <- Conecta al nuevo método
    def configurar_botones(self):
        """Configura la habilitación de botones dependiendo del tipo de usuario."""
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
        """Regresa a la pantalla de inicio de sesión."""
        self.login = Login()  # Crear instancia de la clase Login
        self.login.show()  # Mostrar la ventana de inicio de sesión
        self.close()  # Cerrar la ventana del menú

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
        self.menu = Expedientes(self.tipo_usuario)
        self.menu.show()
        self.close()
    
    def abrir_citas(self):
        self.menu = Citas(self.tipo_usuario)
        self.menu.show()
        self.close()


class Usuarios(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Usuarios, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudUsuarios.ui")
        loadUi(arch, self)
        self.setWindowTitle('Usuarios')
        self.tabWidget.setCurrentIndex(0)
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.tipo_usuario = tipo_usuario  # Guardar el tipo de usuario
        self.btnAgregaU.clicked.connect(self.aniadirUsuario)    
        self.tabWidget.currentChanged.connect(self.tab_seleccionada)
        self.btnElimina.clicked.connect(self.eliminarUsuario)    
        self.btnBuscarUp.clicked.connect(self.rellenarCampos)   
        self.btnBuscarConsulta.clicked.connect(self.consultarUsuario)   
        self.cbxTipo.currentIndexChanged.connect(self.validar_campo_id_vinculado)
        self.cbxTipoUp.currentIndexChanged.connect(self.validar_campo_id_vinculadoUP)
    def validar_campo_id_vinculado(self):
        """
        Activa el campo txtIDVinculado solo si el tipo de usuario es 'veterinario'.
        Para otros tipos de usuario, el campo estará desactivado.
        """
        tipo_usuario = self.cbxTipo.currentText()  # Obtiene el texto actual del ComboBox
        print(f"Tipo de usuario seleccionado: {tipo_usuario}")  # Depuración para ver el tipo seleccionado

        if tipo_usuario.lower() == "veterinario":
            self.txtIDVinculado.setEnabled(True)  # Activa el campo de texto
            self.txtIDVinculado.setPlaceholderText("Ingrese el ID de vínculo")  # Mensaje de ayuda opcional
        else:
            self.txtIDVinculado.setEnabled(False)  # Desactiva el campo de texto
            self.txtIDVinculado.clear()  # Limpia cualquier texto existente
            self.txtIDVinculado.setPlaceholderText("")  # Limpia el mensaje de ayuda opcional
    def validar_campo_id_vinculadoUP(self):
        """
        Activa el campo txtIDVinculado solo si el tipo de usuario es 'veterinario'.
        Para otros tipos de usuario, el campo estará desactivado.
        """
        tipo_usuario = self.cbxTipoUp.currentText()  # Obtiene el texto actual del ComboBox
        print(f"Tipo de usuario seleccionado: {tipo_usuario}")  # Depuración para ver el tipo seleccionado

        if tipo_usuario.lower() == "veterinario":
            self.txtIDVincUp.setEnabled(True)  # Activa el campo de texto
            self.txtIDVincUp.setPlaceholderText("Ingrese el ID de vínculo")  # Mensaje de ayuda opcional
        else:
            self.txtIDVincUp.setEnabled(False)  # Desactiva el campo de texto
            self.txtIDVincUp.clear()  # Limpia cualquier texto existente
            self.txtIDVincUp.setPlaceholderText("")  # Limpia el mensaje de ayuda opcional
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
        # Obtener los valores de los campos
        nombre_usuario = self.txtNombre.text().strip()
        contrasena = self.txtContrasenia.text().strip()
        tipo_usuario = self.cbxTipo.currentText()
        id_vinculado = self.txtIDVinculado.text().strip()
        
        # Validar que los campos obligatorios no estén vacíos
        if not nombre_usuario or not contrasena:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete los campos de nombre de usuario y contraseña.")
            return

        # Validar que el campo id_vinculado sea obligatorio si el tipo de usuario es "veterinario"
        if tipo_usuario == "veterinario":
            if not id_vinculado:
                QMessageBox.warning(self, "ID Vinculado vacío", "El campo ID Vinculado es obligatorio para usuarios de tipo veterinario.")
                return
            
            # Validar que id_vinculado sea un número entero
            if not id_vinculado.isdigit():
                QMessageBox.warning(self, "ID Vinculado inválido", "El campo ID Vinculado debe contener solo números enteros.")
                return

        # Validar que id_vinculado sea un número válido
        id_vinculado_int = None
        if id_vinculado:
            if id_vinculado.isdigit():
                id_vinculado_int = int(id_vinculado)
            else:
                QMessageBox.warning(self, "ID Vinculado inválido", "El campo ID Vinculado debe contener solo números enteros.")
                return

        try:
            # Conexión a la base de datos
            conn = self.conectar_bd()
            cursor = conn.cursor()

            # Verificar si el nombre de usuario ya existe
            cursor.execute("SELECT COUNT(*) FROM USUARIOS WHERE nombre_usuario = %s", (nombre_usuario,))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Usuario duplicado", "El nombre de usuario ya está registrado. Por favor, elija otro.")
                conn.close()
                return

            # Validar que existe al menos un veterinario registrado
            if tipo_usuario == "veterinario":
                cursor.execute("SELECT COUNT(*) FROM VETERINARIOS")
                veterinarios_registrados = cursor.fetchone()[0]
                
                if veterinarios_registrados == 0:
                    QMessageBox.warning(self, "Sin veterinarios", "No se puede registrar un usuario veterinario. No hay veterinarios registrados.")
                    conn.close()
                    return

                # Validar que el id_vinculado coincida con un veterinario registrado
                cursor.execute("SELECT COUNT(*) FROM VETERINARIOS WHERE id_veterinario = %s", (id_vinculado_int,))
                if cursor.fetchone()[0] == 0:
                    QMessageBox.warning(self, "ID Vinculado inválido", "El ID Vinculado no coincide con ningún veterinario registrado.")
                    conn.close()
                    return

            # Preparar la consulta para registrar el usuario
            query = """INSERT INTO USUARIOS (nombre_usuario, contrasena, tipo_usuario, id_vinculado) 
                    VALUES (%s, %s, %s, %s)"""
            data = (nombre_usuario, contrasena, tipo_usuario, id_vinculado_int)
            
            # Ejecutar la consulta
            cursor.execute(query, data)
            conn.commit()
            conn.close()
            
            # Mostrar mensaje de éxito y limpiar los campos
            QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente.")
            self.limpiar_etiquetas()

        except Exception as e:
            # Manejar errores de base de datos o generales
            QMessageBox.critical(self, "Error", f"No se pudo registrar el usuario.\n{e}")




    def inicializarTabla(self, tbl):
        try:            
            conn = self.conectar_bd()
            cursor = conn.cursor()            
            query = "SELECT id_usuario, nombre_usuario, contrasena, tipo_usuario, id_vinculado FROM USUARIOS"
            cursor.execute(query)
            registros = cursor.fetchall()
    
            #self.tblElim.setRowCount(len(registros))
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
            id_usuario = int(id_usuario)  # Validar que sea un número entero
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
        # Obtener el ID del usuario ingresado en el campo de texto
        id_usuario = self.txtBuscaID.text().strip()

        # Validar que el ID del usuario esté proporcionado
        if not id_usuario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del usuario que desea buscar.")
            return

        # Verificar si el ID proporcionado es un número
        if not id_usuario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del usuario debe ser un número.")
            return

        try:
            # Conectar a la base de datos
            conn = self.conectar_bd()
            if not conn:
                return  # Si la conexión falla, salir del método

            # Crear la consulta SQL para buscar al usuario por el ID
            query = "SELECT nombre_usuario, contrasena, tipo_usuario, id_vinculado FROM usuarios WHERE id_usuario = %s"
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (int(id_usuario),))
            resultado = cursor.fetchone()

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Verificar si se encontró el usuario
            if resultado:
                # Rellenar los campos con los datos obtenidos de la base de datos
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
            # Manejar error de conexión a la base de datos
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar cualquier otro error
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")

    def actualizarUsuario(self):        
        id_usuario_original = self.txtBuscaID.text().strip()  # ID original buscado
        nombre_usuario = self.txtNombreUp.text().strip()
        contrasena = self.txtContraseniaUp.text().strip()
        tipo_usuario = self.cbxTipoUp.currentText().strip()
        id_vinculado = self.txtIDVincUp.text().strip()
        
        # Validar que el ID original no esté vacío
        if not id_usuario_original:
            QMessageBox.warning(self, "Error", "El campo ID no puede estar vacío.")
            return

        # Validar que todos los campos obligatorios estén completos
        if not nombre_usuario or not contrasena or not tipo_usuario:
            QMessageBox.warning(self, "Error", "Todos los campos excepto 'ID' son obligatorios.")
            return

        # Validación específica para el campo `id_vinculado` si es veterinario
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
                return  # Si la conexión falla, salir del método

            cursor = conn.cursor()

            # Verificar que el nombre de usuario no esté duplicado
            cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre_usuario = %s AND id_usuario != %s", 
                        (nombre_usuario, int(id_usuario_original)))
            usuario_duplicado = cursor.fetchone()
            if usuario_duplicado:
                QMessageBox.warning(self, "Error", "El nombre de usuario ya está en uso. Por favor, elija otro.")
                cursor.close()
                conn.close()
                return

            # Validar que el ID vinculado existe en la tabla veterinarios si es veterinario
            if tipo_usuario == "veterinario":
                cursor.execute("SELECT COUNT(*) FROM veterinarios WHERE id_veterinario = %s", (int(id_vinculado),))
                if cursor.fetchone()[0] == 0:
                    QMessageBox.warning(self, "Error", "El ID Vinculado no coincide con ningún veterinario registrado.")
                    cursor.close()
                    conn.close()
                    return

            # Definir la consulta SQL de actualización
            query = """UPDATE usuarios 
                    SET nombre_usuario = %s, contrasena = %s, tipo_usuario = %s, id_vinculado = %s 
                    WHERE id_usuario = %s"""
            
            # Preparar los datos para la actualización
            data = (nombre_usuario, contrasena, tipo_usuario, 
                    int(id_vinculado) if id_vinculado else None, int(id_usuario_original))

            # Ejecutar la consulta
            cursor.execute(query, data)
            conn.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Mostrar mensaje de éxito
            QMessageBox.information(self, "Éxito", "Usuario actualizado exitosamente.")
            # Limpiar los campos
            self.limpiar_etiquetas()

        except ValueError as ve:
            QMessageBox.critical(self, "Error", f"Valor inválido: {ve}")
        except mysql.connector.Error as e:
            # Manejar errores de la base de datos
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el usuario. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar errores generales
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")

    def limpiar_etiquetas(self):
        #up
        self.txtBuscaID.setText("")
        self.txtNombreUp.setText("")
        self.txtContraseniaUp.setText("")
        self.cbxTipoUp.currentText()
        self.txtIDVincUp.setText("")
        #ag        
        self.txtNombre.setText("")
        self.txtContrasenia.setText("")
        self.cbxTipoUp.currentText()
        self.txtIDVinculado.setText("")
    
    def consultarUsuario(self):
        # Obtener el ID del usuario ingresado en el campo de búsqueda
        id_usuario = self.txtBuscaConsulta.text().strip()

        # Validar que se haya proporcionado el ID del usuario
        if not id_usuario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de usuario que desea consultar.")
            return
        # Validar que el ID del usuario sea un número
        if not id_usuario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del usuario debe ser un número.")
            return

        try:
            # Establecer la conexión a la base de datos
            conn = self.conectar_bd()
            if not conn:
                return  # Si no se pudo establecer la conexión, salir del método

            # Crear el cursor y la consulta SQL para buscar al usuario por el ID
            cursor = conn.cursor()
            query = """SELECT id_usuario, nombre_usuario, contrasena, tipo_usuario, id_vinculado 
                    FROM usuarios 
                    WHERE id_usuario = %s"""
            cursor.execute(query, (int(id_usuario),))
            registro = cursor.fetchone()  # Obtener un solo registro

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Verificar si se encontró el usuario
            if registro:
                # Configurar la tabla para mostrar un solo registro
                self.tblConsulta.setRowCount(1)
                self.tblConsulta.setColumnCount(5)
                encabezados = ["ID Usuario", "Nombre Usuario", "Contraseña", "Tipo Usuario", "ID Vinculado"]
                self.tblConsulta.setHorizontalHeaderLabels(encabezados)

                # Agregar el registro encontrado a la tabla
                for columna, valor in enumerate(registro):
                    self.tblConsulta.setItem(0, columna, QtWidgets.QTableWidgetItem(str(valor)))

                QMessageBox.information(self, "Éxito", "Usuario consultado correctamente.")
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró un usuario con el ID: {id_usuario}")

        except mysql.connector.Error as e:
            # Mostrar mensaje de error si ocurre un problema durante la consulta
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar cualquier otro error que pueda ocurrir
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")    
                                    
    def abrir_menu(self):
        self.menu = Menu(self.tipo_usuario)  # Pasar el tipo de usuario al menú
        self.menu.show()
        self.close()
     
class Duenios(QMainWindow):
    def __init__(self,tipo_usuario):
        super(Duenios, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudDuenios.ui")
        loadUi(arch, self)
        self.setWindowTitle('Dueños')
        self.tipo_usuario = tipo_usuario  # Guardar el tipo de usuario
        # Configurar permisos según el tipo de usuario
        self.configurar_permisos()
        # Botón para regresar al menú principal
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.tabWidget.setCurrentIndex(0)#inicia la pantalla en la pestaña inicial
        self.tabWidget.currentChanged.connect(self.tab_seleccionada)
        self.btnAgrega.clicked.connect(self.aniadirDuenio)
        self.btnElimina.clicked.connect(self.eliminarDuenio)        
        self.btnBuscar.clicked.connect(self.consultarDuenio)
        self.btnBuscarUp.clicked.connect(self.rellenarCampos)

    def configurar_permisos(self):
        if self.tipo_usuario.upper() == "VETERINARIO":
            self.tabWidget.setTabEnabled(0, False)  # Añadir
            self.tabWidget.setTabEnabled(1, False)  # Eliminar
            self.tabWidget.setTabEnabled(2, False)   # Actualizar
            self.tabWidget.setTabEnabled(3, True)   # Consultar
        elif self.tipo_usuario.upper() == "RECEPCIONISTA":
            self.tabWidget.setTabEnabled(0, True)  # Añadir
            self.tabWidget.setTabEnabled(1, True)  # Eliminar
            self.tabWidget.setTabEnabled(2, True)   # Actualizar
            self.tabWidget.setTabEnabled(3, True)   # Consultar
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

        # Validación de campos vacíos
        if not nombre or not apellidoP or not apellidoM or not telefono or not correo:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        # Validación de formato de correo
        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: usuario@ejemplo.com).")
            return

        # Validación de formato de teléfono
        if not telefono.isdigit() or len(telefono) != 10:
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return

        try:
            # Conexión a la base de datos
            conn = self.conectar_bd()
            query = """INSERT INTO dueños (nombre, apellidoP, apellidoM, telefono, correo) 
                        VALUES (%s, %s, %s, %s, %s)"""
            data = (nombre, apellidoP, apellidoM, telefono, correo)

            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            # Mensaje de éxito
            QMessageBox.information(self, "Éxito", "Dueño registrado exitosamente.")
            self.limpiar_etiquetas()

        except mysql.connector.Error as e:
            # Manejo de errores de base de datos
            QMessageBox.critical(self, "Error", f"No se pudo registrar el dueño. Error en la base de datos:\n{e}")

        except Exception as e:
            # Manejo de errores generales
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
        id_dueño = self.txtIDEliminar.text().strip()  # Elimina espacios en blanco

        # Validar que el campo no esté vacío
        if not id_dueño:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del dueño que desea eliminar.")
            return

        # Validar que el ID sea un número entero
        if not id_dueño.isdigit():
            QMessageBox.warning(self, "Error", "El ID del dueño debe ser un número entero.")
            return

        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()

            # Verificar si el dueño tiene mascotas asociadas
            query_check_mascotas = "SELECT COUNT(*) FROM mascotas WHERE id_dueño = %s"
            cursor.execute(query_check_mascotas, (int(id_dueño),))
            mascotas_asociadas = cursor.fetchone()[0]

            if mascotas_asociadas > 0:
                QMessageBox.warning(self, "Error", f"No se puede eliminar al dueño con ID '{id_dueño}' porque tiene {mascotas_asociadas} mascota(s) asociada(s).")
                cursor.close()
                conn.close()
                return

            # Confirmación antes de eliminar
            confirmacion = QMessageBox.question(
                self,
                "Confirmación",
                f"¿Está seguro de que desea eliminar el dueño con ID '{id_dueño}'?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if confirmacion == QMessageBox.Yes:
                query_delete = "DELETE FROM dueños WHERE id_dueño = %s"
                cursor.execute(query_delete, (int(id_dueño),))  # Convertir a entero antes de usar
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
            # Manejo de errores de la base de datos
            QMessageBox.critical(self, "Error", f"No se pudo eliminar al dueño. Error en la base de datos:\n{e}")

        except Exception as e:
            # Manejo de errores generales
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")



    def rellenarCampos(self):
        # Obtener el ID del usuario ingresado en el campo de texto
        id_dueño = self.txtIDUp.text().strip()
        # Validar que el ID del usuario esté proporcionado
        if not id_dueño:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del dueño que desea buscar.")
            return
        # Verificar si el ID proporcionado es un número
        if not id_dueño.isdigit():
            QMessageBox.warning(self, "Error", "El ID del dueño debe ser un número.")
            return
        try:
            conn = self.conectar_bd()
            if not conn:
                return  # Si la conexión falla, salir del método            
            # Crear la consulta SQL para buscar al usuario por el ID            
            query = """SELECT nombre, apellidoP, apellidoM, telefono, correo 
                        FROM dueños
                       WHERE id_dueño = %s"""
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (int(id_dueño),))
            resultado = cursor.fetchone()
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
            # Verificar si se encontró el usuario
            if resultado:
                # Rellenar los campos con los datos obtenidos de la base de datos
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
            # Manejar error de conexión a la base de datos
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar cualquier otro error
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")
      
    def actualizarDuenio(self):        
        id_dueño = self.txtIDUp.text().strip()
        nombre = self.txtNombreUp.text().strip()
        apellidoP = self.txtApPatUp.text().strip()
        apellidoM = self.txtApMatUp.text().strip()
        telefono = self.txtTelUp.text().strip()
        correo = self.txtCorreoUp.text().strip()
        
        # Validar que los campos obligatorios no estén vacíos
        if not nombre or not apellidoP or not apellidoM or not telefono or not correo:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        # Validación de formato de correo
        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: usuario@ejemplo.com).")
            return

        # Validación de formato de teléfono
        if not telefono.isdigit() or len(telefono) != 10:
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return  # Si la conexión falla, salir del método

            cursor = conn.cursor()

            # Validar si el correo ya existe en otro registro
            query_verificar = "SELECT id_dueño FROM dueños WHERE correo = %s AND id_dueño != %s"
            cursor.execute(query_verificar, (correo, int(id_dueño)))
            resultado = cursor.fetchone()

            if resultado:
                QMessageBox.warning(self, "Error", "El correo ingresado ya está en uso por otro dueño.")
                cursor.close()
                conn.close()
                return

            # Definir la consulta SQL de actualización
            query = """UPDATE dueños 
                    SET nombre = %s, apellidoP = %s, apellidoM = %s, telefono = %s, correo = %s 
                    WHERE id_dueño = %s"""
            
            # Preparar los datos para la actualización
            data = (nombre, apellidoP, apellidoM, telefono, correo, int(id_dueño))

            # Ejecutar la consulta de actualización
            cursor.execute(query, data)
            conn.commit()  # Confirmar la transacción

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Mostrar mensaje de éxito
            QMessageBox.information(self, "Éxito", "Dueño actualizado exitosamente.")
            
            # Limpiar etiquetas
            self.limpiar_etiquetas()

        except mysql.connector.Error as e:
            # Mostrar mensaje de error si ocurre un problema durante la actualización
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el dueño. Error en la base de datos:\n{e}")

        except Exception as e:
            # Manejar cualquier otro error que pueda ocurrir
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")



    def limpiar_etiquetas(self):        
        self.txtIDUp.setText("")
        self.txtIDEliminar.setText("")
        #up
        self.txtIDUp.setText("")
        self.txtNombreUp.setText("")
        self.txtApPatUp.setText("")
        self.txtApMatUp.setText("")
        self.txtTelUp.setText("")
        self.txtCorreoUp.setText("")          
        #ag                
        self.txtNombre.setText("")
        self.txtApPat.setText("")
        self.txtApMat.setText("")
        self.txtTel.setText("")
        self.txtCorreo.setText("")   
                
    def consultarDuenio(self):
        # Obtener el ID del usuario ingresado en el campo de búsqueda
        id_dueño = self.txtIDConsulta.text()

        # Validar que se haya proporcionado el ID del usuario
        if not id_dueño:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del dueño que desea consultar.")
            return
        # Validar que el ID del usuario sea un número
        if not id_dueño.isdigit():
            QMessageBox.warning(self, "Error", "El ID del usuario debe ser un número.")
            return
        try:
            # Establecer la conexión a la base de datos
            conn = self.conectar_bd()
            if not conn:
                return  # Si no se pudo establecer la conexión, salir del método
            # Crear el cursor y la consulta SQL para buscar al usuario por el ID
            cursor = conn.cursor()
            query = """SELECT id_dueño, nombre, apellidoP, apellidoM, telefono, correo
                    FROM dueños 
                    WHERE id_dueño = %s"""                    
            cursor.execute(query, (int(id_dueño),))
            registro = cursor.fetchone()  # Obtener un solo registro

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Verificar si se encontró el usuario
            if registro:
                # Configurar la tabla para mostrar un solo registro
                self.tblConsultar.setRowCount(1)
                self.tblConsultar.setColumnCount(6)
                encabezados = ["ID Dueño", "Nombre", "Apellido Paterno", "Apellido Materno", "telefono","Correo"]
                self.tblConsultar.setHorizontalHeaderLabels(encabezados)
                # Agregar el registro encontrado a la tabla
                for columna, valor in enumerate(registro):
                    self.tblConsultar.setItem(0, columna, QtWidgets.QTableWidgetItem(str(valor)))
                QMessageBox.information(self, "Éxito", "Dueño consultado correctamente.")
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró un dueño con el ID: {id_dueño}")
        except mysql.connector.Error as e:
            # Mostrar mensaje de error si ocurre un problema durante la consulta
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar cualquier otro error que pueda ocurrir
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

        # Configurar permisos según el tipo de usuario
        self.configurar_permisos()
        self.tabWidget.setCurrentIndex(0)
        # Llenar el combobox con los dueños
        self.llenar_combobox_duenios() 
        # Botón para añadir mascota
        self.btnAgregaA.clicked.connect(self.aniadir_mascota)

        # Botón para regresar al menú principal
        self.btnRegresar.clicked.connect(self.abrir_menu)
        # Botón para buscar mascota
        self.btnBuscarUp.clicked.connect(self.buscar_mascota)
        # Botón para actualizar mascota
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
        #up
        self.txtNombreUp.setText("")
        self.txtEspecieUp.setText("")        
        self.txtRazaUp.setText("")
        self.txtEdadUp.setText("")
        self.rdbAltaUp.setChecked(False)
        self.rdbRecuperacionUp.setChecked(False)
        self.rdbTratamientoUp.setChecked(False)
        self.rdbCriticoUp.setChecked(False)
        self.cbxDuenioUp.currentText()
        #ag        
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
            self.tabWidget.setTabEnabled(0, False)  # Añadir
            self.tabWidget.setTabEnabled(1, False)  # Eliminar
            self.tabWidget.setTabEnabled(2, True)   # Actualizar
            self.tabWidget.setTabEnabled(3, True)   # Consultar
        elif self.tipo_usuario.upper() == "RECEPCIONISTA":
            self.tabWidget.setTabEnabled(0, True)  # Añadir
            self.tabWidget.setTabEnabled(1, True)  # Eliminar
            self.tabWidget.setTabEnabled(2, True)   # Actualizar
            self.tabWidget.setTabEnabled(3, True)   # Consultar
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
            # Agregar el ID al nombre para diferenciarlos
            query = "SELECT id_dueño, CONCAT(id_dueño, ' - ', nombre, ' ', apellidoP, ' ', apellidoM) AS nombre_completo FROM Dueños"
            cursor.execute(query)
            resultados = cursor.fetchall()
            conn.close()

            self.cbxDuenio.clear()
            for id_dueño, nombre_completo in resultados:
                # Agregar texto con ID al combobox para diferenciar dueños con nombres repetidos
                self.cbxDuenio.addItem(nombre_completo, id_dueño)  # Agrega el texto visible y el ID como datos asociados
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

        # Validar que los campos obligatorios estén completos
        if not nombre or not especie or not estado or id_dueño is None:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos obligatorios.")
            return

        # Validar que la edad sea un número entero
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

        # Validar que el ID no esté vacío
        if not id_mascota:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la mascota a buscar.")
            return
        if not id_mascota.isdigit():
            QMessageBox.warning(self, "Error", "El ID de la mascota debe ser un número entero positivo.")
            self.txtIDMascCon.setText("")  # Limpia el campo si la validación falla
            return
        try:
            conn = self.conectar_bd()
            if not conn:
                return

            # Consulta para buscar los datos de la mascota
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

            # Rellenar los campos con los datos de la mascota
            nombre, especie, raza, edad, estado, id_dueño_actual = resultado_mascota
            self.txtNombreUp.setText(nombre)
            self.txtEspecieUp.setText(especie)
            self.txtRazaUp.setText(raza)
            self.txtEdadUp.setText(str(edad) if edad else "")

            # Seleccionar el estado
            self.rdbAltaUp.setChecked(estado == "alta")
            self.rdbRecuperacionUp.setChecked(estado == "recuperacion")
            self.rdbTratamientoUp.setChecked(estado == "tratamiento")
            self.rdbCriticoUp.setChecked(estado == "critico")

            # Cargar todos los dueños en el ComboBox
            query_duenios = """
                SELECT id_dueño, CONCAT(id_dueño, ' - ', nombre, ' ', apellidoP, ' ', apellidoM) AS nombre_completo
                FROM Dueños
            """
            cursor.execute(query_duenios)
            resultados_duenios = cursor.fetchall()

            # Rellenar el ComboBox
            self.cbxDuenioUp.clear()
            indice_actual = -1
            for index, (id_dueño, nombre_completo) in enumerate(resultados_duenios):
                self.cbxDuenioUp.addItem(nombre_completo, id_dueño)
                if id_dueño == id_dueño_actual:
                    indice_actual = index

            # Seleccionar el dueño actual de la mascota
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

        # Validar que todos los campos obligatorios estén completos
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

        # Validar que la edad sea un número entero
        if not edad.isdigit():
            QMessageBox.warning(self, "Error", "La edad debe ser un número entero.")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return

            # Actualizar los datos en la base de datos
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
        id_mascota = self.txtIDEliminar.text().strip()  # Eliminar espacios en blanco
        
        # Validar que el campo no esté vacío
        if not id_mascota:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la mascota que desea eliminar.")
            return
        
        # Validar que el ID sea un número entero positivo
        if not id_mascota.isdigit():
            QMessageBox.warning(self, "Error", "El ID de la mascota debe ser un número entero válido.")
            self.txtIDEliminar.setText("")
            return
        
        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()

            # Confirmar eliminación
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
                
                # Verificar si se eliminó correctamente
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
        """Consulta los datos de una mascota en la base de datos por su ID."""
        # Obtener el ID de la mascota ingresado en el campo de búsqueda
        id_mascota = self.txtIDMascCon.text().strip()

        # Validar que se haya proporcionado el ID
        if not id_mascota:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la mascota que desea consultar.")
            return

        # Validar que el ID sea un número entero positivo
        if not id_mascota.isdigit():
            QMessageBox.warning(self, "Error", "El ID de la mascota debe ser un número entero positivo.")
            self.txtIDMascCon.setText("")  # Limpia el campo si la validación falla
            return

        try:
            # Establecer la conexión a la base de datos
            conn = self.conectar_bd()
            if not conn:
                return  # Si no se pudo establecer la conexión, salir del método

            # Crear el cursor y la consulta SQL para buscar a la mascota por el ID
            cursor = conn.cursor()
            query = """
                SELECT m.id_mascota, m.nombre, m.especie, m.raza, m.edad, m.estado, m.id_dueño,
                    CONCAT(d.nombre, ' ', d.apellidoP, ' ', d.apellidoM) AS nombre_dueño
                FROM mascotas m
                JOIN dueños d ON m.id_dueño = d.id_dueño
                WHERE m.id_mascota = %s
            """
            cursor.execute(query, (int(id_mascota),))
            registro = cursor.fetchone()  # Obtener un solo registro

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Verificar si se encontró la mascota
            if registro:
                # Configurar la tabla para mostrar un solo registro
                self.tblConsultar.setRowCount(1)
                self.tblConsultar.setColumnCount(8)
                headers = ["ID Mascota", "Nombre", "Especie", "Raza", "Edad", "Estado", "ID Dueño", "Nombre Dueño"]
                self.tblConsultar.setHorizontalHeaderLabels(headers)

                # Agregar el registro encontrado a la tabla
                for columna, valor in enumerate(registro):
                    self.tblConsultar.setItem(0, columna, QtWidgets.QTableWidgetItem(str(valor)))

                QMessageBox.information(self, "Éxito", "Mascota consultada correctamente.")
            else:
                QMessageBox.warning(self, "No encontrado", f"No se encontró una mascota con el ID: {id_mascota}")
                self.txtIDMascCon.setText("")
                self.inicializarTabla(self.tblConsultar)
        except mysql.connector.Error as e:
            # Mostrar mensaje de error si ocurre un problema durante la consulta
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar cualquier otro error que pueda ocurrir
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



class Veterinarios(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Veterinarios, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudVeterinarios.ui")
        loadUi(arch, self)
        self.setWindowTitle('Veterinarios')
        self.tipo_usuario = tipo_usuario  # Guardar el tipo de usuario
        # Configurar permisos según el tipo de usuario
        self.configurar_permisos()        
        self.tabWidget.setCurrentIndex(0)#inicia la pantalla en la pestaña inicial
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
            self.tabWidget.setTabEnabled(0, False)  # Añadir
            self.tabWidget.setTabEnabled(1, False)  # Eliminar
            self.tabWidget.setTabEnabled(2, False)   # Actualizar
            self.tabWidget.setTabEnabled(3, True)   # Consultar
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

        # Validación de campos vacíos
        if not nombre or not apellidoP or not apellidoM or not correo:
            QMessageBox.warning(self, "Error", "Campos vacíos.")
            return

        # Validación de formato de correo
        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: usuario@ejemplo.com).")
            return

        # Validación de longitud exacta del teléfono
        if telefono and (not telefono.isdigit() or len(telefono) != 10):
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return

        try:
            conn = self.conectar_bd()
            query = """INSERT INTO veterinarios (nombre, apellidoP, apellidoM, especialidad, telefono, correo) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""

            # Asignación de datos para la consulta SQL
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

        # Validación de campos vacíos
        if not id_veterinario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de veterinario que desea eliminar.")
            return

        # Validación de formato de ID (solo números enteros)
        if not id_veterinario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del veterinario debe ser un número entero.")
            return

        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()

            # Confirmación antes de eliminar
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

        # Validar que todos los campos sean llenos
        if not id_veterinario or not nombre or not apellidoP or not apellidoM or not especialidad or not telefono or not correo:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Validar que el ID sea un número entero
        if not id_veterinario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del veterinario debe ser un número entero.")
            return

        # Validar que el teléfono tenga exactamente 10 dígitos
        if not (telefono.isdigit() and len(telefono) == 10):
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener exactamente 10 dígitos.")
            return

        # Validar formato del correo
        if not ("@" in correo and correo.endswith(".com")):
            QMessageBox.warning(self, "Error", "El correo debe tener un formato válido (ejemplo: pepe@ejemplo.com).")
            return

        try:
            conn = self.conectar_bd()
            if not conn:
                return  # Si la conexión falla, salir del método

            # Verificar si el correo ya existe en otro registro
            check_query = "SELECT id_veterinario FROM veterinarios WHERE correo = %s AND id_veterinario != %s"
            cursor = conn.cursor()
            cursor.execute(check_query, (correo, int(id_veterinario)))
            existing = cursor.fetchone()

            if existing:
                QMessageBox.warning(self, "Error", "El correo ingresado ya está en uso por otro veterinario.")
                cursor.close()
                conn.close()
                return

            # Preparar la consulta de actualización
            query = """UPDATE veterinarios 
                    SET nombre = %s, apellidoP = %s, apellidoM = %s, especialidad = %s, telefono = %s, correo = %s 
                    WHERE id_veterinario = %s"""

            # Preparar los datos para la actualización
            data = (
                nombre,
                apellidoP,
                apellidoM,
                especialidad,
                telefono,
                correo,
                int(id_veterinario),
            )

            # Ejecutar la consulta de actualización
            cursor.execute(query, data)
            conn.commit()  # Confirmar la transacción

            if cursor.rowcount > 0:
                QMessageBox.information(self, "Éxito", "Usuario actualizado exitosamente.")
                self.limpiar_etiquetas()
            else:
                QMessageBox.warning(self, "Error", f"No se encontró un veterinario con ID '{id_veterinario}'.")

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            # Mostrar mensaje de error si ocurre un problema durante la actualización
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el usuario. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar cualquier otro error que pueda ocurrir
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")
        
    def consultarUsuario(self):
        # Obtener el ID del usuario ingresado en el campo de búsqueda
        id_veterinario = self.txtBuscaConV.text().strip()
        # Validar que se haya proporcionado el ID del usuario
        if not id_veterinario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del veterinario que desea consultar.")
            return
        # Validar que el ID del usuario sea un número
        if not id_veterinario.isdigit():
            QMessageBox.warning(self, "Error", "El ID del veterinario debe ser un número.")
            return
        try:
            # Establecer la conexión a la base de datos
            conn = self.conectar_bd()
            if not conn:
                return  # Si no se pudo establecer la conexión, salir del método

            # Crear el cursor y la consulta SQL para buscar al usuario por el ID
            cursor = conn.cursor()            
            query = """SELECT id_veterinario, nombre, apellidoP, apellidoM, especialidad, telefono, correo 
                         FROM veterinarios
                        WHERE id_veterinario = %s"""
            cursor.execute(query, (int(id_veterinario),))
            registro = cursor.fetchone()  # Obtener un solo registro

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Verificar si se encontró el usuario
            if registro:
                # Configurar la tabla para mostrar un solo registro
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
            # Mostrar mensaje de error si ocurre un problema durante la consulta
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla. Error en la base de datos:\n{e}")
        except Exception as e:
            # Manejar cualquier otro error que pueda ocurrir
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado:\n{e}")    
    
    def abrir_menu(self):
        """Regresa al menú principal."""
        self.menu = Menu(self.tipo_usuario)
        self.menu.show()
        self.close()

class Expedientes(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Expedientes, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crudExpedientes.ui")
        loadUi(arch, self)

        self.setWindowTitle('Expedientes')
        self.tipo_usuario = tipo_usuario

        # Configuración de botones
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.btnAgregaU.clicked.connect(self.aniadirExpediente)
        self.btnEliminarExpediente.clicked.connect(self.eliminarExpediente)
        self.buscarId.clicked.connect(self.consultarExpediente)
        self.btnActualizarE.clicked.connect(self.actualizarExpedientes)
        self.buscarE.clicked.connect(self.buscarExpediente)

        # Inicializar tablas
        self.inicializarTabla(self.tblExpedientes)
        self.inicializarTabla(self.tblExpedientes_2)
        self.inicializarTabla(self.tblExpedientes_3)

    def conectar_bd(self):
        """Establece la conexión a la base de datos."""
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Veterinaria"
            )
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"No se pudo conectar a la base de datos.\n{err}")
            return None

        # Agregar la función buscarExpediente
    def buscarExpediente(self):
        """Busca un expediente por ID y lo muestra en la tabla tblExpedientes_3."""
        id_expediente = self.txtIdExpediente.text().strip()  # Obtener el ID ingresado

        if not id_expediente:
            QMessageBox.warning(self, "Error", "Debe ingresar un ID de expediente.")
            return

        try:
            conn = self.conectar_bd()
            if conn is None:
                return

            cursor = conn.cursor()

            # Consulta para obtener los datos del expediente según el ID
            query = """
            SELECT id_expediente, id_mascota, descripcion, fecha_apertura, ultima_actualizacion
            FROM Expedientes
            WHERE id_expediente = %s
            """
            cursor.execute(query, (id_expediente,))
            resultados = cursor.fetchall()

            # Si se encuentran resultados
            if resultados:
                # Limpiar la tabla antes de llenarla con nuevos resultados
                self.tblExpedientes_3.setRowCount(len(resultados))
                self.tblExpedientes_3.setColumnCount(5)  # Número de columnas
                self.tblExpedientes_3.setHorizontalHeaderLabels(["ID Expediente", "ID Mascota", "Descripción", "Fecha Apertura", "Última Actualización"])

                # Llenar la tabla con los datos obtenidos
                for row_index, row_data in enumerate(resultados):
                    for col_index, col_data in enumerate(row_data):
                        self.tblExpedientes_3.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            else:
                QMessageBox.information(self, "Sin resultados", f"No se encontraron expedientes con ID '{id_expediente}'.")
                self.tblExpedientes_3.setRowCount(0)  # Limpiar la tabla si no se encuentran resultados

            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar el expediente.\n{e}")

    def aniadirExpediente(self):
        """Registra un nuevo expediente en la base de datos."""
        id_mascota = self.txtIdmascota.text()
        descripcion = self.txtDescripcion.text()

        if not id_mascota or not descripcion:
            QMessageBox.warning(self, "Error", "Debe llenar todos los campos.")
            return

        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            conn = self.conectar_bd()
            if conn is None:
                return

            query = """
            INSERT INTO Expedientes (id_mascota, descripcion, fecha_apertura, ultima_actualizacion)
            VALUES (%s, %s, %s, %s)
            """
            data = (int(id_mascota), descripcion, fecha_actual, fecha_actual)

            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()

            # Insertar en la tabla de ingresos
            query_ingreso = """
            INSERT INTO fechasingreso (id_expediente, fecha_ingreso, descripcion)
            VALUES (LAST_INSERT_ID(), %s, %s)
            """
            cursor.execute(query_ingreso, (fecha_actual, descripcion))
            conn.commit()

            QMessageBox.information(self, "Éxito", "Expediente registrado exitosamente.")
            self.txtIdmascota.clear()
            self.txtDescripcion.clear()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"No se pudo registrar el expediente.\n{err}")
        finally:
            if conn:
                conn.close()

    def inicializarTabla(self, tbl):
        """Carga los expedientes en la tabla de la interfaz."""
        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()
            query = "SELECT id_expediente, id_mascota, descripcion, fecha_apertura, ultima_actualizacion FROM Expedientes"
            cursor.execute(query)
            registros = cursor.fetchall()

            tbl.setColumnCount(5)
            tbl.setHorizontalHeaderLabels(["ID Expediente", "ID Mascota", "Descripción", "Fecha Apertura", "Última Actualización"])
            tbl.setRowCount(len(registros))

            for fila, registro in enumerate(registros):
                for columna, valor in enumerate(registro):
                    tbl.setItem(fila, columna, QTableWidgetItem(str(valor)))

            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla de expedientes.\n{e}")

    def eliminarExpediente(self):
        """Elimina un expediente y sus relaciones según el ID proporcionado."""
        id_expediente = self.txtElimina.text()
        if not id_expediente:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID del expediente que desea eliminar.")
            return

        try:
            conn = self.conectar_bd()
            cursor = conn.cursor()
            confirmacion = QMessageBox.question(
                self, "Confirmación", f"¿Está seguro de que desea eliminar el expediente '{id_expediente}' y sus registros relacionados?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if confirmacion == QMessageBox.Yes:
                # Eliminar primero los registros relacionados en `fechasingreso`
                query_fechas = "DELETE FROM fechasingreso WHERE id_expediente = %s"
                cursor.execute(query_fechas, (id_expediente,))

                # Luego eliminar el expediente de la tabla `expedientes`
                query_expedientes = "DELETE FROM expedientes WHERE id_expediente = %s"
                cursor.execute(query_expedientes, (id_expediente,))
                conn.commit()

                if cursor.rowcount > 0:
                    QMessageBox.information(self, "Éxito", f"Expediente '{id_expediente}' y sus registros relacionados fueron eliminados exitosamente.")
                    self.inicializarTabla(self.tblExpedientes)
                    self.txtElimina.clear()
                else:
                    QMessageBox.warning(self, "Error", f"No se encontró el expediente '{id_expediente}'.")
                    self.txtElimina.clear()

            conn.close()
        except Exception as e:
         QMessageBox.critical(self, "Error", f"No se pudo eliminar el expediente.\n{e}")

    def consultarExpediente(self):
        """Consulta expedientes según el ID de la mascota, incluyendo los ingresos relacionados y la información de la mascota."""
        try:
            id_mascota = self.txtid.text().strip()

            if not id_mascota:
                QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un ID de mascota.")
                return

            conn = self.conectar_bd()
            cursor = conn.cursor()

            # Consultar los expedientes, los ingresos relacionados y la información de la mascota
            query = """
            SELECT 
                E.id_expediente, 
                E.id_mascota, 
                M.id_dueño, 
                F.descripcion AS ingreso_descripcion, 
                M.especie, 
                M.raza, 
                M.edad, 
                M.estado, 
                F.fecha_ingreso
            FROM Expedientes E
            LEFT JOIN fechasingreso F ON E.id_expediente = F.id_expediente
            LEFT JOIN mascotas M ON E.id_mascota = M.id_mascota
            WHERE E.id_mascota = %s
            ORDER BY F.fecha_ingreso DESC
            """
            cursor.execute(query, (id_mascota,))
            resultados = cursor.fetchall()

            if resultados:
                # Configurar y llenar la tabla principal
                self.tblExpedientes_2.setRowCount(len(resultados))
                self.tblExpedientes_2.setColumnCount(9)
                self.tblExpedientes_2.setHorizontalHeaderLabels([
                    "ID Expediente", "ID Mascota", "ID Dueño", "Descripción Ingreso", 
                    "Especie", "Raza", "Edad", "Estado", "Fecha Ingreso"
             ])

                for row_index, row_data in enumerate(resultados):
                    for col_index, col_data in enumerate(row_data):
                        self.tblExpedientes_2.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            # Actualizar tablas secundarias
                self.fec_aper2.setRowCount(1)
                self.fec_aper2.setColumnCount(1)
                self.fec_aper2.setHorizontalHeaderLabels(["Fecha Apertura"])
                self.fec_act2.setRowCount(1)
                self.fec_act2.setColumnCount(1)
                self.fec_act2.setHorizontalHeaderLabels(["Última Actualización"])

# Usar la primera fila de `resultados` para llenar las tablas secundarias
                if resultados:
    # Primera fila contiene la fecha más reciente por el `ORDER BY` DESC
                    self.fec_aper2.setItem(0, 0, QTableWidgetItem(str(resultados[0][8])))  # Fecha de Ingreso (la más reciente)
                    self.fec_act2.setItem(0, 0, QTableWidgetItem(str(resultados[0][8])))  # Fecha de Ingreso (última actualización)

                    conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al consultar expedientes.\n{e}")

    def actualizarExpedientes(self):
        """Agrega un nuevo ingreso al expediente y actualiza la última fecha de actualización."""
        id_expediente = self.txtIdExpediente.text().strip()
        nueva_descripcion = self.txtNuevaDescripcion.text().strip()

        if not id_expediente or not nueva_descripcion:
            QMessageBox.warning(self, "Error", "Debe proporcionar el ID del expediente y la nueva descripción.")
            return

        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            conn = self.conectar_bd()
            if conn is None:
                return

            cursor = conn.cursor()

            # Insertar un nuevo ingreso en la tabla fechasingreso
            query_ingreso = """
            INSERT INTO fechasingreso (id_expediente, fecha_ingreso, descripcion)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query_ingreso, (id_expediente, fecha_actual, nueva_descripcion))

            # Actualizar la última fecha de actualización del expediente
            query_actualizar = """
            UPDATE Expedientes
            SET ultima_actualizacion = %s
            WHERE id_expediente = %s
            """
            cursor.execute(query_actualizar, (fecha_actual, id_expediente))

            # Consulta para obtener el expediente actualizado
            query_buscar = """
            SELECT id_expediente, id_mascota, descripcion, fecha_apertura, ultima_actualizacion
            FROM Expedientes
            WHERE id_expediente = %s
            """
            cursor.execute(query_buscar, (id_expediente,))
            expediente = cursor.fetchone()

            if expediente:
                QMessageBox.information(self, "Éxito", "Expediente actualizado exitosamente.")
                self.inicializarTabla(self.tblExpedientes_2)
            else:
                QMessageBox.warning(self, "Error", "No se encontró el expediente.")

            conn.commit()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el expediente.\n{e}")
    def abrir_menu(self):
        """Abre el menú principal."""
        self.menu = Menu(self.tipo_usuario)
        self.menu.show()
        self.close()
        
        
class Citas(QMainWindow):
    def __init__(self, tipo_usuario):
        super(Citas, self).__init__()
        arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Citas.ui")
        loadUi(arch, self)
        self.setWindowTitle('Citas')
        self.conn = self.connect_db()
        self.cursor = self.conn.cursor(buffered=True)
        self.tipo_usuario = tipo_usuario
    

        # Conectar botones a funciones
        self.btnAgregaU.clicked.connect(self.registrar_cita)  # Registrar
        self.btnAgregaU_2.clicked.connect(self.eliminar_cita)  # Eliminar
        self.pushButton_3.clicked.connect(self.consultar_citas)  # Consultar
        self.btnAgregaU_3.clicked.connect(self.cargar_datos_actualizar)  # Buscar cita para actualizar
        self.pushButton_2.clicked.connect(self.actualizar_cita)  # Guardar cambios en la cita
        self.btnRegresar.clicked.connect(self.abrir_menu)
        self.btnRegresar_2.clicked.connect(self.abrir_menu)
        self.btnRegresar_3.clicked.connect(self.abrir_menu)
        self.btnRegresar_4.clicked.connect(self.abrir_menu)
        

        # Escuchar eventos de selección en el calendario y tabla
        self.calendarWidget.selectionChanged.connect(self.update_datetime_bar)
        self.tableWidget_3.cellClicked.connect(self.update_datetime_bar)

        # Resaltar fechas ocupadas en el calendario
        self.highlight_occupied_dates()

        # Cargar citas en tablas
        self.load_all_citas(self.tableWidget_2)  # Tabla de eliminar
        self.load_all_citas(self.tableWidget_4)  # Tabla de consultar

        

    def connect_db(self):
        """Conexión a la base de datos MySQL"""
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",  # Cambiar si es necesario
                password="",  # Cambiar según tu configuración
                database="Veterinaria"  # Cambiar si el nombre de la base es diferente
            )
            
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error de conexión", f"No se pudo conectar a la base de datos: {e}")
            sys.exit()
            return None
    


    def registrar_cita(self):
        """Registrar una nueva cita en la base de datos"""
        id_mascota = self.lineEdit_11.text()
        id_veterinario = self.lineEdit_15.text()
        motivo = self.lineEdit_13.text()
        fecha_hora = self.lineEdit_12.text()  # Ahora toma el valor de la barra de texto

        if not id_mascota or not id_veterinario or not motivo or not fecha_hora:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Verificar si el horario ya está ocupado
        if self.is_datetime_occupied(fecha_hora):
            QMessageBox.warning(self, "Error", "El horario seleccionado ya está ocupado. Elija otro horario.")
            return

        try:
            query = """
            INSERT INTO citas (id_mascota, id_veterinario, fecha_hora, motivo)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (id_mascota, id_veterinario, fecha_hora, motivo))
            self.conn.commit()
            QMessageBox.information(self, "Éxito", "Cita registrada correctamente.")
            # Resaltar la fecha ocupada en el calendario
            selected_date = QDate.fromString(fecha_hora.split()[0], "yyyy-MM-dd")
            self.highlight_date(selected_date)
            # Actualizar tablas
            self.load_all_citas(self.tableWidget_2)
            self.load_all_citas(self.tableWidget_4)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo registrar la cita: {e}")
        finally:
            self.limpiar_campos()

    def update_datetime_bar(self):
        """Actualiza la barra de texto con la fecha y hora seleccionadas"""
        selected_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        selected_time = ""

        # Verificar si se seleccionó alguna celda en la tabla
        if self.tableWidget_3.currentRow() >= 0 and self.tableWidget_3.currentColumn() >= 0:
            selected_time = self.tableWidget_3.horizontalHeaderItem(self.tableWidget_3.currentColumn()).text()

        # Combinar la fecha y hora si ambas están seleccionadas
        if selected_date and selected_time:
            self.lineEdit_12.setText(f"{selected_date} {selected_time}")

    def is_datetime_occupied(self, fecha_hora):
        """Verifica si una fecha y hora están ocupadas"""
        try:
            query = "SELECT COUNT(*) FROM citas WHERE fecha_hora = %s"
            self.cursor.execute(query, (fecha_hora,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error al verificar disponibilidad: {e}")
            return False

    def highlight_occupied_dates(self):
        """Resalta todas las fechas ocupadas en el calendario"""
        try:
            query = "SELECT DISTINCT DATE(fecha_hora) FROM citas"
            self.cursor.execute(query)
            fechas_ocupadas = self.cursor.fetchall()

            for fecha in fechas_ocupadas:
                self.highlight_date(fecha[0])
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar las fechas ocupadas: {e}")

    def highlight_date(self, date):
        """Resalta una fecha específica en el calendario"""
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("red"))
        self.calendarWidget.setDateTextFormat(date, fmt)

    def load_all_citas(self, table_widget):
        """Carga todas las citas en una tabla"""
        try:
            query = "SELECT id, id_mascota, id_veterinario, fecha_hora, motivo FROM citas"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            if resultados:
                self.populate_table(table_widget, resultados)
            else:
                table_widget.setRowCount(0)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar las citas: {e}")

    def populate_table(self, table_widget, data):
        """Llena una tabla con datos"""
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(5)
        table_widget.setHorizontalHeaderLabels(["ID", "ID Mascota", "ID Veterinario", "Fecha y Hora", "Motivo"])

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def actualizar_cita(self):
        """Actualizar los datos de una cita existente"""
        id_cita = self.lineEdit_6.text()
        id_mascota = self.lineEdit_12.text()
        id_veterinario = self.lineEdit_14.text()
        fecha_hora = self.dateTimeEdit_2.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        motivo = self.lineEdit_13.text()

        if not id_cita or not id_mascota or not id_veterinario or not motivo:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            query = """
            UPDATE citas
            SET id_mascota = %s, id_veterinario = %s, fecha_hora = %s, motivo = %s
            WHERE id = %s
            """
            self.cursor.execute(query, (id_mascota, id_veterinario, fecha_hora, motivo, id_cita))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                QMessageBox.information(self, "Éxito", f"Cita con ID {id_cita} actualizada correctamente.")
                # Actualizar tablas
                self.load_all_citas(self.tableWidget_2)
                self.load_all_citas(self.tableWidget_4)
            else:
                QMessageBox.warning(self, "Error", f"No se encontró una cita con ID {id_cita}.")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar la cita: {e}")

    def eliminar_cita(self):
        """Eliminar una cita de la base de datos"""
        id_cita = self.lineEdit_3.text()

        if not id_cita:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la cita a eliminar.")
            return

        try:
            query = "DELETE FROM citas WHERE id = %s"
            self.cursor.execute(query, (id_cita,))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                QMessageBox.information(self, "Éxito", f"Cita con ID {id_cita} eliminada correctamente.")
                # Actualizar tablas
                self.load_all_citas(self.tableWidget_2)
                self.load_all_citas(self.tableWidget_4)
            else:
                QMessageBox.warning(self, "Error", f"No se encontró una cita con ID {id_cita}.")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar la cita: {e}")

    def consultar_citas(self):
        """Consultar citas en la base de datos"""
        id_cita = self.lineEdit_8.text()

        try:
            if id_cita:
                query = "SELECT id, id_mascota, id_veterinario, fecha_hora, motivo FROM citas WHERE id = %s"
                self.cursor.execute(query, (id_cita,))
                resultados = self.cursor.fetchall()

                if not resultados:
                    QMessageBox.information(self, "Sin resultados", f"No se encontró ninguna cita con ID {id_cita}.")
                    return

                self.populate_table(self.tableWidget_4, resultados)
            else:
                self.load_all_citas(self.tableWidget_4)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron consultar las citas: {e}")

    def cargar_datos_actualizar(self):
        """Cargar los datos de una cita en los campos para actualizar"""
        id_cita = self.lineEdit_6.text()

        if not id_cita:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el ID de la cita a buscar.")
            return

        try:
            query = "SELECT id_mascota, id_veterinario, fecha_hora, motivo FROM citas WHERE id = %s"
            self.cursor.execute(query, (id_cita,))
            resultado = self.cursor.fetchone()

            if resultado:
                self.lineEdit_12.setText(resultado[0])  # ID Mascota
                self.lineEdit_14.setText(resultado[1])  # ID Veterinario
                self.dateTimeEdit_2.setDateTime(resultado[2])  # Fecha y Hora
                self.lineEdit_13.setText(resultado[3])  # Motivo
            else:
                QMessageBox.warning(self, "Error", f"No se encontró una cita con ID {id_cita}.")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los datos: {e}")

    def load_all_citas(self, table_widget):
        """Cargar todas las citas en una tabla"""
        try:
            query = "SELECT id, id_mascota, id_veterinario, fecha_hora, motivo FROM citas"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            if resultados:
                self.populate_table(table_widget, resultados)
            else:
                table_widget.setRowCount(0)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar las citas: {e}")

    def populate_table(self, table_widget, data):
        """Llenar una tabla con datos"""
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(5)
        table_widget.setHorizontalHeaderLabels(["ID", "ID Mascota", "ID Veterinario", "Fecha y Hora", "Motivo"])

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def limpiar_campos(self):
        """Limpia los campos después de registrar"""
        self.lineEdit_11.clear()
        self.lineEdit_15.clear()
        self.lineEdit_13.clear()
        self.dateTimeEdit.setDateTime(self.dateTimeEdit.minimumDateTime())

    def closeEvent(self, event):
        """Cierra la conexión al salir"""
        self.cursor.close()
        self.conn.close()
        event.accept()

    def limpiar_campos(self):
        """Limpia los campos después de registrar"""
        self.lineEdit_11.clear()
        self.lineEdit_15.clear()
        self.lineEdit_13.clear()
        self.lineEdit_12.clear()
        self.dateTimeEdit.setDateTime(self.dateTimeEdit.minimumDateTime())

    def closeEvent(self, event):
        """Cierra la conexión al salir"""
        self.cursor.close()
        self.conn.close()
        event.accept()

    def abrir_menu(self):
        """Abre el menú principal."""
        self.menu = Menu(self.tipo_usuario)
        self.menu.show()
        self.close()
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Login()
    form.show()
    sys.exit(app.exec())
