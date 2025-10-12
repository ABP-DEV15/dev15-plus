import mysql.connector
from conn.dbconn import DBConn
from interface.data_access_dao import DataAccessDAO


class UsuariosViviendaDAO(DataAccessDAO):
    def __init__(self, dbconn: DBConn):
        self.dbconn = dbconn.conectar_a_mysql()
        self.database = dbconn.obtener_base_de_datos()

    def get(self, id):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT id_usuario, id_vivienda FROM {self.database}.usuarios_viviendas WHERE id_usuario = %s"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return row[1]
                return None
            except mysql.connector.Error as err:
                raise err

    def get_all_data(self):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT id_usuario, id_vivienda FROM {self.database}.usuarios_viviendas"
                cursor.execute(query, )
                rows = cursor.fetchall()
                usuarios_viviendas = [(row[0], row[1]) for row in rows]
                return usuarios_viviendas
            except mysql.connector.Error as err:
                raise err

    def create(self, id_usuario, id_vivienda):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"INSERT INTO {self.database}.usuarios_viviendas (id_usuario, id_vivienda) VALUES (%s, %s)"
                values = (id_usuario, id_vivienda)
                cursor.execute(query, values)
                conn.commit()
            except mysql.connector.Error as err:
                raise err

    def update(self, id_usuario, id_vivienda, new_id_vivienda):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"UPDATE {self.database}.usuarios_viviendas SET id_vivienda = %s WHERE id_usuario = %s and id_vivienda = %s"
                values = (new_id_vivienda, id_usuario, id_vivienda)
                cursor.execute(query, values)
                conn.commit()
            except mysql.connector.Error as err:
                raise err

    def delete(self, id_usuario, id_vivienda):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"DELETE FROM {self.database}.usuarios_viviendas WHERE id_usuario = %s and id_vivienda = %s"
                cursor.execute(query, (id_usuario, id_vivienda))
                conn.commit()
            except mysql.connector.Error as err:
                raise err