from base_de_datos import BaseDeDatos

class Usuario:
    def __init__(self, usuario: str, contraseña: str, dni: str):
        self._usuario = usuario
        self._contraseña = contraseña
        self._dni = dni
        self._luces = set()
    
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, valor):
        self._usuario = valor
         
    @property
    def contraseña(self):
        return self._contraseña
    
    @contraseña.setter
    def contraseña(self, valor):
        if len(valor) < 8:
            raise ValueError("La contraseña debe tener minimo 8 caracteres")
        self._contraseña = valor
    
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if len(valor) not in (7, 8):
            raise ValueError("El DNI debe tener entre 7 y 8 caracteres")
        self._dni = valor
    
    @property
    def luces(self):
        return self._luces
    

class UsuarioControlador(BaseDeDatos):
    def __init__(self):
        super().__init__()
        self.lista_de_usuario: list[Usuario] = []
    
    def insertar_usuario(self, usuario: str, contraseña: str, dni: str) -> Usuario:
        nuevo = self._crear_usuario(usuario, contraseña, dni)
        self.lista_de_usuario.append(nuevo)
        return nuevo  
    def obtener_usuario(self, dni: str) -> Usuario | None:
        for u in self.lista_de_usuario:
            if u.dni == dni:
                return u
            return None
    def asignar_luz(self, usuario: Usuario, luz: str) -> None:
        usuario.luces.add(luz)
    def _crear_usuario(self, usuario: str, contraseña: str, dni:str) -> Usuario:
        return Usuario(usuario, contraseña, dni)