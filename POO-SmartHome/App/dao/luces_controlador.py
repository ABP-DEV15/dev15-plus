from conn.base_de_datos import BaseDeDatos

class LucesControlador(BaseDeDatos):
    def __init__(self):
        super().__init__()
        self._luces = []  # Lista de Luces
        self._ids = {}    # Diccionario: {id_luz: objeto_luz}
    
    def cambiar_nombre(self, id_luz, nuevo_nombre):
      
        if id_luz in self._ids:
            luz = self._ids[id_luz]
            luz._nombre = nuevo_nombre
            return True
        return False
    
    def agregar_luz(self, luz, nombre):
         self._luces.append(luz)
         self._ids[nombre] = luz

    
    def listar_luces(self):
        """Devuelve todas las luces """
        return self._luces
    
    def obtener_luz_por_id(self, id_luz):
        """Método auxiliar para obtener una luz por su ID"""
        return self._ids.get(id_luz)