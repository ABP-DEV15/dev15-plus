from dominio.clases_base.usuarios import Usuario

class UsuarioAdministrador(Usuario):
    def __init__(self, usuario, contraseña, dni):
        super().__init__(usuario, contraseña, dni, rol='admin')
