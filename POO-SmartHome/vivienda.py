class Vivienda:
    def __init__(self, calle, altura, ciudad, id_vivienda):
        self._calle = calle
        self._altura = altura
        self._ciudad = ciudad
        self._id_vivienda = id_vivienda

    @property
    def calle(self):
        return self._calle
    @calle.setter
    def calle(self, nueva_calle):
        self._calle = nueva_calle
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, nueva_altura):
        self._altura = nueva_altura
    @property
    def ciudad(self):
        return self._ciudad
    @ciudad.setter
    def ciudad(self, nueva_ciudad):
        self._ciudad = nueva_ciudad
    @property
    def id_vivienda(self):
        return self._id_vivienda
    @id_vivienda.setter
    def id_vivienda(self, nuevo_id):
        self._id_vivienda = nuevo_id    