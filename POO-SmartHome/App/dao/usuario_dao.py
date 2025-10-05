from conn.dbconn import DBCconn
from interface.data_access_dao import DataAccessDAO

class UsuarioDAO(DataAccessDAO):
    def __init__(self, dbconn: DBCconn):
        self.dbconn = dbconn.conectar_a_mysql()
        self.database = dbconn.obtener_base_de_datos()
