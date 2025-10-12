import mysql.connector
from conn.dbconn import DBConn
from interface.data_access_dao import DataAccessDAO
from dominio.luces import Luces

class LucesDAO(DataAccessDAO):
    def __init__(self, dbconn: DBConn):
        self.dbconn = dbconn.conectar_a_mysql()
        self.database = dbconn.obtener_base_de_datos()

    def get(self, id_luz, id_vivienda):
        with self.dbconn as conn:
            cursor = conn.cursor()
            query = f"SELECT id_luz, nombre, intensidad, id_vivienda FROM {self.database}.luces WHERE id_luz = %s and id_vivienda = %s"
            cursor.execute(query, (id_luz, id_vivienda))
            row = cursor.fetchone()
            if row:
                return Luces(nombre=row[1], intensidad=row[2])
            return None

    def get_all_data(self, id_vivienda):
        with self.dbconn as conn:
            cursor = conn.cursor()
            query = f"SELECT id_luz, nombre, intensidad, id_vivienda FROM {self.database}.luces where id_vivienda = %s"
            cursor.execute(query, (id_vivienda,))
            rows = cursor.fetchall()
            luces = [Luces(nombre=row[1], intensidad=row[2]) for row in rows]
            return luces

    def create(self, luz: Luces, id_vivienda):
        with self.dbconn as conn:
            cursor = conn.cursor()
            query = f"INSERT INTO {self.database}.luces (nombre, intensidad, id_vivienda) VALUES (%s, %s, %s)"
            values = (luz.nombre, luz.intensidad, id_vivienda)
            cursor.execute(query, values)
            conn.commit()

    def update(self, luz: Luces, nombre):
        with self.dbconn as conn:
            cursor = conn.cursor()
            query = f"UPDATE {self.database}.luces SET nombre = %s, intensidad = %s WHERE nombre = %s"
            values = (luz.nombre, luz.intensidad, nombre)
            cursor.execute(query, values)
            conn.commit()

    def delete(self, nombre):
        with self.dbconn as conn:
            cursor = conn.cursor()
            query = f"DELETE FROM {self.database}.luces WHERE id_luz = %s"
            cursor.execute(query, (nombre,))
            conn.commit()
