import json
import os

LUCES_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "luces.json")

# Cargar luces
def cargar_luces(archivo=LUCES_PATH):
    if not os.path.exists(archivo):
        print(f"El archivo {archivo} no existe")
        return []
    
    try:
        with open(archivo, 'r', encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, TypeError) as error:
        print(f"Error al cargar las luces: {error}")
        return []

# Guardar luces
def guardar_luces(luces, archivo=LUCES_PATH):
    try:
        with open(archivo, 'w', encoding="utf-8") as f:
            json.dump(luces, f, indent=2)
    except (json.JSONDecodeError, TypeError) as error:
        print(f"Error al guardar las luces: {error}")