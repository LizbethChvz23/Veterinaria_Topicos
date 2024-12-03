import mysql.connector
from PyQt5.QtWidgets import QMessageBox

class registro_datos:
    
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
    """
    
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = "localhost",
            database ="veterinaria",
            user = "root",
            password = ""
        )
    
    def buscaUsuario(self, nombre_usuario):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM USUARIOS WHERE NOMBRE_USUARIO = {}".format(nombre_usuario)
        cur.execute(sql)
        nom_users = cur.fetchall()
        cur.close()
        return nom_users
    
    def buscaContra(self, contrasenia):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM USUARIOS WHERE contrasenia = {}".format(contrasenia)
        cur.execute(sql)
        contra = cur.fetchall()
        cur.close()
        return contra"""