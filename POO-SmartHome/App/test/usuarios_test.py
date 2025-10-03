import pytest
from usuarios import Usuario


class TestUsuario:
    def test_crear_usuario(self):
        usuario = Usuario("juan", "contraseña123", "12345678", "admin")
        assert usuario.usuario == "juan"
        assert usuario.contraseña == "contraseña123"
        assert usuario.dni == "12345678"
        assert usuario.rol == "admin"

    def test_modificar_usuario(self):
        usuario = Usuario("juan", "contraseña123", "12345678", "admin")
        usuario.usuario = "pedro"
        assert usuario.usuario == "pedro"

    def test_modificar_contraseña_valida(self):
        usuario = Usuario("juan", "contraseña123", "12345678", "admin")
        usuario.contraseña = "nuevaPass123"
        assert usuario.contraseña == "nuevaPass123"

    def test_modificar_contraseña_invalida(self):
        usuario = Usuario("juan", "contraseña123", "12345678", "admin")
        with pytest.raises(ValueError) as excinfo:
            usuario.contraseña = "short"
        assert str(excinfo.value) == "La contraseña debe tener al menos 8 caracteres."