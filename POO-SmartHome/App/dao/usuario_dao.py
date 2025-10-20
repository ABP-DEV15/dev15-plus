import mysql.connector
from conn.dbconn import DBConn
from interface.data_access_dao import DataAccessDAO
from dominio.clases_base.usuarios import Usuario

class UsuarioDAO(DataAccessDAO):
    def __init__(self, dbconn: DBConn):
        self.dbconn = dbconn.conectar_a_mysql()
        self.database = dbconn.obtener_base_de_datos()

    def get(self, id):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT usuario, contrasena, dni, rol FROM {self.database}.usuarios WHERE usuario = %s"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    conn.close()
                    return Usuario(row[0], row[1], row[2], row[3])
                return None
            except mysql.connector.Error as err:
                raise err

    def get_all_data(self):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT usuario, contrasena, dni, rol FROM {self.database}.usuarios"
                cursor.execute(query, )
                rows = cursor.fetchall()
                usuarios = [Usuario(row[0], row[1], row[2], row[3]) for row in rows]
                return usuarios
            except mysql.connector.Error as err:
                raise err

    def create(self, usuario: Usuario):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"INSERT INTO {self.database}.usuarios (usuario, contrasena, dni, rol) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (usuario.usuario,
                usuario.contraseña, usuario.dni, usuario.rol))
                conn.commit()
            except mysql.connector.Error as err:
                raise err

    def update(self, usuario: Usuario):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"UPDATE {self.database}.usuarios SET usuario = %s, contrasena = %s, dni = %s, rol = %s WHERE dni = %s"
                cursor.execute(query, (usuario.usuario,
                usuario.contraseña, usuario.dni, usuario.rol, usuario.dni))
                conn.commit()
            except mysql.connector.Error as err:
                raise err
            
    def delete(self, id):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"DELETE FROM {self.database}.usuarios WHERE dni = %s"
                cursor.execute(query, (id,))
                conn.commit()
            except mysql.connector.Error as err:
                raise err

    def validar_contraseña(self, usuario, contraseña):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT contrasena FROM {self.database}.usuarios WHERE usuario = %s"
                cursor.execute(query, (usuario,))
                row = cursor.fetchone()
                if row and row[0] == contraseña:
                    return True
                return False
            except mysql.connector.Error as err:
                raise err
            
    def get_id_by_username(self, username):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT id_usuario FROM {self.database}.usuarios WHERE usuario = %s"
                cursor.execute(query, (username,))
                row = cursor.fetchone()
                
                if row:
                    return row[0]
                return None
            except mysql.connector.Error as err:
                raise err
            
    def check_duplicate(self, usuario):
        with self.dbconn as conn:
            try:
                cursor = conn.cursor()
                query = f"select usuario from {self.database}.usuarios where usuario = %s"       
                cursor.execute(query,(usuario,))
                row = cursor.fetchone()
                if row:
                    print(row)
                    return True
                return False
            except mysql.connector.Error as err:
                raise err