import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from luces import Luces
import pytest
@pytest.fixture

def luces_fixture():
        return Luces()

def test_luces_inician_apagadas(luces_fixture):
        return Luces ()
        assert luces_fixture.estado() == "apagadas"

def test_luces_pueden_encenderse(luces_fixture):
        return Luces()
        assert luces_fixture.estado() == "encendidas"

def test_luces_pueden_apagarse(luces_fixture):
        luces_fixture.encender()
        luces_fixture.apagar()
        assert luces_fixture.estado() == "apagadas"

def test_intensidad_se_ajusta_al_usuario(luces_fixture):
        luces_fixture.intensidad = 5
        assert luces_fixture._intensidad == 5
# la intensidad de luz se adapta a preferencia del usuario.
        luces_fixture.intensidad = 20
        assert luces_fixture._intensidad == 20
# no deberia haberse modificado a ese valor.