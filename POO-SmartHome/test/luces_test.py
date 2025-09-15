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
        return Luces()
        luces_fixture.encender()
        luces_fixture.apagar()
        assert luces_fixture.estado() == "apagadas"
