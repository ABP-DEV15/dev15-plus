class BaseDeDatos:
    def __init__(self):
        self.estado_conexion = False

    def conectar(self) -> bool:
        self.estado_conexion = True
        return self.estado_conexion

    def desconectar(self) -> bool:
        self.estado_conexion = False
        return self.estado_conexion
