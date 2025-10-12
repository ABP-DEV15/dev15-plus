from dominio.clases_base.dispositivo import Dispositivo

class Luces(Dispositivo):
    def __init__(self, nombre, intensidad=0):
        super().__init__(nombre)
        self._intensidad = intensidad

    @property
    def intensidad(self):
        return self._intensidad

    @intensidad.setter
    def intensidad(self, valor):
            self._intensidad = valor
