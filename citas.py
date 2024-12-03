import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"C:\Users\AlejandroDamiánLopez\Documents\Topicos\Proyecto_v2\Proyecto_v2\Citas.ui", self)

        # Conexión a la base de datos
        self.conn = self.connect_db()
        self.cursor = self.conn.cursor()

        # Conectar botones a funciones
        self.btnAgregaU.clicked.connect(self.registrar_cita)  # Registrar
        self.btnAgregaU_2.clicked.connect(self.eliminar_cita)  # Eliminar
        self.pushButton_3.clicked.connect(self.consultar_citas)  # Consultar
        self.btnAgregaU_3.clicked.connect(self.cargar_datos_actualizar)  # Buscar cita para actualizar
        self.pushButton_2.clicked.connect(self.actualizar_cita)  # Guardar cambios en la cita

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
            conn = mysql.connector.connect(
                host="localhost",
                user="aled",
                password="aled",
                database="veterinaria"
            )
            return conn
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error de conexión", f"No se pudo conectar a la base de datos: {e}")
            sys.exit()

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
        
def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.btnRegresar.setText(_translate("MainWindow", "Volver al Menú"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
