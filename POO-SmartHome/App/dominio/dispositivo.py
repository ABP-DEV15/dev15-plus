class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self._encendida = False

    def encender(self):
        self._encendida = True

    def apagar(self):
        self._encendida = False

    def estado(self):
        return "encendido" if self._encendida else "apagado"
