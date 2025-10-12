class Luces(Dispositivo):
    def __init__(self, nombre, intensidad=0):
        super().__init__(nombre)
        self._intensidad = intensidad

    @property
    def intensidad(self):
        return self._intensidad

    @intensidad.setter
    def intensidad(self, valor):
        if 0 <= valor <= 10:
            self._intensidad = valor
        else:
            raise ValueError("La intensidad debe estar entre 0 y 10.")



       
            
     