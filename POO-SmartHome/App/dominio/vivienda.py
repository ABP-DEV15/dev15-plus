class Vivienda:
    def __init__(self, id_vivienda, ciudad, calle, altura, luces=[]):
        self.__id_vivienda = id_vivienda
        self.__ciudad = ciudad
        self.__calle = calle
        self.__altura = altura
        self.__luces = []
        

    @property
    def calle(self):
        return self.__calle
    @calle.setter
    def calle(self, nueva_calle):
        self.__calle = nueva_calle
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, nueva_altura):
        self.__altura = nueva_altura
    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, nueva_ciudad):
        self.__ciudad = nueva_ciudad
    @property
    def id_vivienda(self):
        return self.__id_vivienda
    @id_vivienda.setter
    def id_vivienda(self, nuevo_id):
        self.__id_vivienda = nuevo_id
    @property
    def luces(self):
        return self.__luces
    @luces.setter
    def luces(self, nuevas_luces):
        self.__luces = nuevas_luces    

    def _listar_luces(self):
        for luz in self.__luces:
            print(luz)       