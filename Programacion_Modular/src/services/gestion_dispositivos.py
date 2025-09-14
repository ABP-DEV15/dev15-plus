import uuid
from src.services.luces import cargar_luces, guardar_luces
import datetime

luces = cargar_luces()


def listar_luces(luces):
    if not luces:
        print("No hay luces registradas.")
        return
    print("Luces registradas:")
    for luz in luces:
        print(f"{luz['nombre']} - Estado: {'Encendida' if luz['estado'] else 'Apagada'}")
def buscar_luz(luces, nombre):
    for luz in luces:
        if luz['nombre'].lower() == nombre.lower():
            print(f"Luz encontrada: {luz['nombre']} - Estado: {'Encendida' if luz['estado'] else 'Apagada'}")
            return luz
    print(f"Luz '{nombre}' no encontrada.")
    return None

def agregar_luz(luces, nombre, estado=False):
    if any(l['nombre'].lower() == nombre.lower() for l in luces):
        print(f"La luz '{nombre}' ya existe.")
    else:
        nueva_luz = {
            "id": str(uuid.uuid4()),
            "nombre": nombre,
            "estado": estado
        }
        luces.append(nueva_luz)
        guardar_luces(luces)
        print(f"Luz '{nombre}' agregada.")

def eliminar_luz(luces, nombre):
    luces_filtradas = [l for l in luces if l['nombre'].lower() != nombre.lower()]
    if len(luces_filtradas) == len(luces):
        print(f"Luz '{nombre}' no encontrada.")
        return luces
    else:
        guardar_luces(luces_filtradas)
    return luces_filtradas

def cambiar_estado(nombre, nuevo_estado):
    for luz in luces:
        if luz['nombre'].lower() == nombre.lower():
            luz['estado'] = nuevo_estado
            guardar_luces(luces)
            print(f"Estado de la luz '{nombre}' cambiado a {'Encendida' if nuevo_estado else 'Apagada'}.")
            return
    print(f"Luz '{nombre}' no encontrada.")

def automatizacion_por_horario(luces):
    ahora = datetime.datetime.now().time()

     # Prender luz del frente a las 19:00Hs
    if ahora.hour == 19 and ahora.minute == 0:
        for luz in luces:
            if luz['nombre'].lower() == 'frente':
                if not luz['estado']:
                    luz['estado'] = True
                    print("Luz 'Frente' encendida automáticamente al anochecer (19:00).")
        guardar_luces(luces)
    
     # Apaga todas las luces a las 23:00 excepto la del frente
    if ahora.hour == 23 and ahora.minute == 0:
        cambio = False
    for luz in luces:
        if luz['estado'] and luz['nombre'].lower() != 'frente':
            luz['estado'] = False
            cambio = True
            if cambio:
                print("Todas las luces (excepto la del frente') fueron apagadas automáticamente a las 23:00.")
                guardar_luces(luces)

   
