import pytest
from vivienda import Vivienda

class TestVivienda:
    def test_crear_vivienda(self):
        luces = ["Luz1", "Luz2"]
        vivienda = Vivienda("Calle Falsa", 123, "Springfield", "VIV001", luces)
        assert vivienda.calle == "Calle Falsa"
        assert vivienda.altura == 123
        assert vivienda.ciudad == "Springfield"
        assert vivienda.id_vivienda == "VIV001"
        assert vivienda._luces == luces

    def test_listar_luces(self, capsys):
        luces = ["Luz1", "Luz2"]
        vivienda = Vivienda("Calle Falsa", 123, "Springfield", "VIV001", luces)
        vivienda._listar_luces()
        captured = capsys.readouterr()
        assert captured.out == "Luz1\nLuz2\n"                   