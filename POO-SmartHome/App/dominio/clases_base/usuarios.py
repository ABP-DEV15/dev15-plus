class Usuario:
    def __init__(self, usuario, contraseña, dni, rol):
        self._usuario = usuario
        self._contraseña = contraseña
        self._dni = dni
        self._rol = rol

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
            raise ValueError ("La contraseña debe tener al menos 8 caracteres.")
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
