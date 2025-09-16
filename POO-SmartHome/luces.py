class Luces:
    def __init__(self):
        self._encendida = False
        self._intensidad = 0 #regular la intensidad de luz

        def estado(self):
            if self._encendida:
                return "encendidas"
            else:
                return "apagadas"


class Luces:
    def __init__(self):
            self._encendida

    def estado(self):
            if self._encendida:
                return "encendidas"
            else:
                return "apagadas"
    def encender(self):
        self._encendida = True


class Luces:
    def __init__(self):
        self._encendida = False

        def estado(self):
            if self._encendida:True
            return "encendidas"
            return "apagadas"

    def encender(self):
        self._encendida = True

    def apagar(self):
        self._encendida = False


class Luces:
    def __init__(self):
        self._encendida = False
        self._intensidad = 0 #variable para la luminosidad

        def estado (self):
            if self._encendida:
                return "encendidas"
            else:
                return "apagadas"
            
        def encender(self):
            self._encendida = True
        def apagar(self):
            self._encendida = False
        def intensidad(self,valor):
            if 0 <= valor <= 10:
                self._intensidad = valor
            else: pass