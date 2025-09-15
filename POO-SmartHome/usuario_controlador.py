from base_de_datos import BaseDeDatos

class Usuario:
    def __init__(self, usuario: str, contraseña: str, dni: str):
        self.usuario = usuario
        self.contraseña = contraseña
        self.dni = dni
        self.luces = set()
        
class UsuarioControlador(BaseDeDatos):
    def __init__(self):
        super().__init__()
        self.lista_de_usuarios: list[Usuario] = []
    
    def insertar_usuario(self, usuario: str, contraseña: str, dni: str) -> Usuario:
        nuevo = self._crear_usuario(usuario, contraseña, dni)
        self.lista_de_usuarios.append(nuevo)
        return nuevo

    
    def obtener_usuario(self, dni: str) -> Usuario | None:
        for u in self.lista_de_usuarios:
            if u.dni == dni:
                return u
        return None
    
    def asignar_luz(self, usuario: Usuario, luz: str) -> None:
        usuario.luces.add(luz)
    
    def _editar_datos_personales(self, dato: str, nuevo_dato: str) -> None:
        pass

    def _listar_usuarios(self) -> None: 
        for u in self.lista_de_usuarios:
            print(f"{u.usuario} - {u.dni}") 
        
    def _crear_usuario(self, usuario: str, contraseña: str, dni: str) -> Usuario: return Usuario(usuario, contraseña, dni)