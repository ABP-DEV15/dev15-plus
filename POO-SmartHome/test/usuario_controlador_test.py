import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from usuario_controlador import UsuarioControlador, Usuario
import pytest
@pytest.fixture
def controlador():
    return UsuarioControlador()

def test_insertar_usuario(controlador):
    usuario = controlador.insertar_usuario("pablo", "12345678", "12345678")
    
    assert isinstance(usuario, Usuario)
    assert usuario.usuario == "pablo"
    assert usuario.contraseña == "12345678"
    assert usuario.dni == "12345678"
    assert usuario in controlador.lista_de_usuario

def test_obtener_usuario(controlador):
    controlador.insertar_usuario("ana", "abcdefgh", "87654321")
    
    usuario = controlador.obtener_usuario("87654321")
    assert usuario is not None
    assert usuario.usuario == "ana"
    usuario_none = controlador.obtener_usuario("00000000")
    assert usuario_none is None

def test_asignar_luz(controlador):
    usuario = controlador.insertar_usuario("luis", "abcdefgh", "11223344")
    controlador.asignar_luz(usuario, "Luz1")
    assert "Luz1" in usuario.luces
    assert len(usuario.luces) == 1
