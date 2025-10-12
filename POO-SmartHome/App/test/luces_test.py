import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dominio.luces import Luces
import pytest

def test_luces_inician_apagadas():
        luces = Luces("Luz Sala")
        assert luces._encendida is False

def test_luces_pueden_encenderse():
        luces = Luces("Luz Sala")
        luces.encender()
        assert luces.estado() == "encendido"

def test_luces_pueden_apagarse():
        luces = Luces("Luz Sala")
        luces.apagar()
        assert luces.estado() == "apagado"

def test_intensidad_se_ajusta_al_usuario():
        luces = Luces("Luz Sala")
        luces.intensidad = 5
        assert luces._intensidad == 5
