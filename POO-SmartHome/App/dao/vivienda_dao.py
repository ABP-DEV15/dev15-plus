import mysql.connector
from conn.dbconn import DBConn
from interface.data_access_dao import DataAccessDAO
from dominio.vivienda import Vivienda

class ViviendaDAO(DataAccessDAO):
    def __init__(self, dbconn: DBConn):
        self.dbconn = dbconn.conectar_a_mysql()
        self.database = dbconn.obtener_base_de_datos()

    def get(self, id):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT id_vivienda, ciudad, calle, altura FROM {self.database}.viviendas WHERE id_vivienda = %s"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return Vivienda(row[0], row[1], row[2], row[3], row[4])
                return None
            except mysql.connector.Error as err:
                raise err
            
    def get_all_data(self):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT id_vivienda, ciudad, calle, altura FROM {self.database}.viviendas"
                cursor.execute(query, )
                rows = cursor.fetchall()
                viviendas = [Vivienda(row[0], row[1], row[2], row[3], row[4]) for row in rows]
                return viviendas
            except mysql.connector.Error as err:
                raise err

    def create(self, vivienda: Vivienda):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"INSERT INTO {self.database}.viviendas (id_vivienda, ciudad, calle, altura) VALUES (%s, %s, %s, %s)"
                values = (vivienda.id_vivienda, vivienda.ciudad, vivienda.calle, vivienda.altura)
                cursor.execute(query, values)
                conn.commit()
            except mysql.connector.Error as err:
                raise err
    
    def update(self, vivienda: Vivienda):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"UPDATE {self.database}.viviendas SET ciudad = %s, calle = %s, altura = %s WHERE id_vivienda = %s"
                values = (vivienda.ciudad, vivienda.calle, vivienda.altura, vivienda.id_vivienda)
                cursor.execute(query, values)
                conn.commit()
            except mysql.connector.Error as err:
                raise err

    def delete(self, id):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"DELETE FROM {self.database}.viviendas WHERE id_vivienda = %s"
                cursor.execute(query, (id,))
                conn.commit()
            except mysql.connector.Error as err:
                raise err
            