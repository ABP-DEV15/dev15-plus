import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data.luces_data import cargar_luces
from services.gestion_dispositivos import listar_luces, buscar_luz, agregar_luz, eliminar_luz, automatizacion_por_horario, cambiar_estado

def menu():
    print("**********Bienvenido a SmartHome**********")
    print("**********MENU PRINCIPAL**********")
    print("1. Listar luces ")
    print("2. Buscar luz por nombre")
    print("3. Agregar luz")
    print("4. Eliminar luz")
    print("5. Ejecutar Modo de ahorro de energia")
    print("6. Encender/apagar Luz")
    print("7. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        luces = cargar_luces()
        listar_luces(luces)
        menu()
    elif opcion == "2":
        luz_nombre = input("Ingrese el nombre de la luz a buscar: ")
        luces = cargar_luces()
        buscar_luz(luces, luz_nombre)
        menu()
    elif opcion == "3":
        nueva_luz = input("Ingrese el nombre de la nueva luz: ")
        luces = cargar_luces()
        agregar_luz(luces, nueva_luz)
        menu()
    elif opcion == "4":
        luz_eliminar = input("Ingrese el nombre de la luz a eliminar: ")
        luces = cargar_luces()
        luces = eliminar_luz(luces, luz_eliminar)
        menu()
    elif opcion == "5":
        luces = cargar_luces()
        automatizacion_por_horario(luces)
        print("Modo de ahorro de energia ejecutado.")
        menu()
    elif opcion == "6":
        luces = cargar_luces()
        listar_luces(luces)
        luz_nombre = input("Ingrese el nombre de la luz a modificar: ")
        estado_input = input("Ingrese el estado (1 para encender, 0 para apagar): ")
        nuevo_estado = estado_input == "1"
        cambiar_estado(luz_nombre, nuevo_estado)
        menu()            
    elif opcion == "7":
        print("Programa finalizado.")
    else:
        print("Opcion no valida, elije una opcion del 1 al 6.")

if __name__ == "__main__":
    menu()