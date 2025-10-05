import pathlib
import configparser
import mysql.connector
from mysql.connector import errorcode

class DBCconn:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        if self.config_file != "":
            config = configparser.ConfigParser()
            config_path = pathlib.Path(__file__).parent.parent / self.config_file
            config.read(config_path)
            self.db_config = config['database']

    def get_config_path(self):
        return self.config_file

    def obtener_base_de_datos(self):
        return self.db_config.get('database')

    def conectar_a_mysql(self):
        try:
            conexion = mysql.connector.connect(
                host=self.db_config.get('host'),
                user=self.db_config.get('user'),
                password=self.db_config.get('password'),
                database=self.db_config.get('database')
            )
            return conexion
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de autenticación: Verifica el usuario y la contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)
            return None
