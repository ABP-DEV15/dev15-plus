from dominio.clases_base.usuarios import Usuario

class UsuarioEstandar(Usuario):
    def __init__(self, usuario, contraseña, dni):
        super().__init__(usuario, contraseña, dni, rol='estandar')

    def __consultar_datos(self):
        return f"Usuario: {self.usuario}, DNI: {self.dni}, Rol: {self.rol}"
    
    def llamar_datos(self):
        return self.__consultar_datos()