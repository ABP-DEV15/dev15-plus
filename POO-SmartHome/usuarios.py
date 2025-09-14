class Usuarios:
    def __init__(self, usuario, contraseña, dni, rol, luces):
        self._usuario = usuario
        self._contraseña = contraseña
        self._dni = dni
        self._rol = rol
        self._luces = luces

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario

    @property
    def contraseña(self):
        return self._contraseña
    
    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) < 8:
            return "La contraseña debe tener al menos 8 caracteres."
        self._contraseña = nueva_contraseña

    @property
    def dni(self):
        return self._dni
    
    @dni.setter 
    def dni(self, nuevo_dni):
        if len(nuevo_dni) != 8 or len(nuevo_dni) != 7:
            return "El DNI debe tener al menos 7 caracteres y no mas de 8."
        self._dni = nuevo_dni

    @property
    def rol(self):
        return self._rol    

    @rol.setter
    def rol(self, nuevo_rol):
        self._rol = nuevo_rol

    def _mostrar_datos_personales(self):
        return f"Usuario: {self._usuario}, DNI: {self._dni}, Rol: {self._rol}"
    
    def listar_dispositivos(self):
        for luz in self._luces:
            print(luz)
        