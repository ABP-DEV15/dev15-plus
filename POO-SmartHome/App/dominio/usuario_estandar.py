from clases_base.usuarios import Usuario

class UsuarioEstandar(Usuario):
    def __init__(self, usuario, contraseña, dni):
        super().__init__(usuario, contraseña, dni, rol='estandar')

    def consultar_datos(self):
        return f"Usuario: {self.usuario}, DNI: {self.dni}, Rol: {self.rol}"