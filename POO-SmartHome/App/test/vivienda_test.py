import pytest
from dominio.vivienda import Vivienda

class TestVivienda:
    def test_crear_vivienda(self):
        luces = ["Luz1", "Luz2"]
        vivienda = Vivienda( "VIV001", "Springfield", "Calle Falsa", 123, luces)
        assert vivienda.calle == "Calle Falsa"
        assert vivienda.altura == 123
        assert vivienda.ciudad == "Springfield"
        assert vivienda.id_vivienda == "VIV001"

                 