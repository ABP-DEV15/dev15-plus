class Usuarios:
    def __init__(self, usuario, contraseña, dni, rol, luces):
        self._usuario = usuario
        self._contraseña = contraseña
        self._dni = dni
        self._rol = rol
        self._luces = luces

    def _mostrar_datos_personales(self):
        return f"Usuario: {self._usuario}, DNI: {self._dni}, Rol: {self._rol}"
    
    def listar_dispositivos(self):
        for luz in self._luces:
            print(luz)
        