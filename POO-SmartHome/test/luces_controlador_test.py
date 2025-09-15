import pytest
import sys
import os

# Agregar el path para importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from luces_controlador import LucesControlador
from luces import Luces

@pytest.fixture
def controlador():
    """Fixture que crea una instancia de LucesControlador para cada test"""
    return LucesControlador()

@pytest.fixture
def luz_ejemplo():
    """Fixture que crea una luz de ejemplo"""
    luz = Luces()
    luz._nombre = "Luz_Sala"  # Asignamos nombre manualmente
    return luz

def test_agregar_luz(controlador, luz_ejemplo):
    """Test que verifica que se puede agregar una luz al controlador"""
    controlador.agregar_luz(luz_ejemplo, "L1")
    
    assert len(controlador.listar_luces()) == 1
    assert luz_ejemplo in controlador.listar_luces()

def test_cambiar_nombre_existente(controlador, luz_ejemplo):
    """Test que verifica que se puede cambiar el nombre de una luz existente"""
    # Configuración
    controlador.agregar_luz(luz_ejemplo, "L1")
    nombre_original = luz_ejemplo._nombre
    
    # Acción
    resultado = controlador.cambiar_nombre("L1", "Luz_Sala_Principal")
    
    # Verificación
    assert resultado == True
    assert luz_ejemplo._nombre == "Luz_Sala_Principal"
    assert luz_ejemplo._nombre != nombre_original

def test_cambiar_nombre_multiples_luces(controlador):
    """Test que verifica que cambia solo la luz correcta entre múltiples luces"""
    # Crear múltiples luces
    luz1 = Luces()
    luz1._nombre = "Luz_Cocina"
    luz2 = Luces()
    luz2._nombre = "Luz_Habitacion"
    luz3 = Luces()
    luz3._nombre = "Luz_Baño"
    
    # Agregar luces al controlador
    controlador.agregar_luz(luz1, "L1")
    controlador.agregar_luz(luz2, "L2")
    controlador.agregar_luz(luz3, "L3")
    
    # Cambiar nombre solo de la luz 2
    resultado = controlador.cambiar_nombre("L2", "Luz_Dormitorio")
    
    # Verificaciones
    assert resultado == True
    assert luz1._nombre == "Luz_Cocina"  # No cambió
    assert luz2._nombre == "Luz_Dormitorio"  # Sí cambió
    assert luz3._nombre == "Luz_Baño"  # No cambió

def test_agregar_multiples_luces(controlador):
    """Test que verifica que se pueden agregar múltiples luces"""
    luz1 = Luces()
    luz1._nombre = "Luz1"
    luz2 = Luces()
    luz2._nombre = "Luz2"
    luz3 = Luces()
    luz3._nombre = "Luz3"
    
    controlador.agregar_luz(luz1, "L1")
    controlador.agregar_luz(luz2, "L2")
    controlador.agregar_luz(luz3, "L3")
    
    assert len(controlador.listar_luces()) == 3

def test_herencia_base_de_datos(controlador):
    # Verificar que tiene los métodos de BaseDeDatos
    assert hasattr(controlador, "conectar")
    assert hasattr(controlador, "desconectar")
    assert hasattr(controlador, "estado_conexion")
    
    # Verificar que los métodos funcionan
    assert controlador.conectar() == True
    assert controlador.estado_conexion == True
    assert controlador.desconectar() == False
    assert controlador.estado_conexion == False