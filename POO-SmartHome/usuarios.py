class Usuarios:
    def __init__(self, usuario, contraseña, dni, rol, luces):
        self.usuario = usuario
        self.contraseña = contraseña
        self.dni = dni
        self.rol = rol
        self.luces = luces

    def mostrar_datos_personales(self):
        return f"Usuario: {self.usuario}, DNI: {self.dni}, Rol: {self.rol}"
    
    def listar_dispositivos(self):
        for luz in self.luces:
            print(luz)
        