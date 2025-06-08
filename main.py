from src.services.luces import cargar_luces
from src.services.gestion_dispositivos import listar_luces, buscar_luz, agregar_luz, eliminar_luz
from src.services.gestion_dispositivos import automatizacion_por_horario

luces = cargar_luces()
def menu():
    print("**********Bienvenido a SmartHome**********")
    print("**********MENU PRINCIPAL**********")
    print("1. Listar luces ")
    print("2. Buscar luz por nombre")
    print("3. Agregar luz")
    print("4. Eliminar luz")
    print("5. Ejecutar Modo de ahorro de energia")
    print("6. Salir")

while True:
    menu()
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        listar_luces(luces)

    elif opcion == "2":
        luz_nombre = input("Ingrese el nombre de la luz a buscar: ")
        buscar_luz(luces, luz_nombre)


    elif opcion == "3":
        nueva_luz = input("Ingrese el nombre de la nueva luz: ")
        agregar_luz(luces, nueva_luz)

    elif opcion == "4":
         luz_eliminar = input("Ingrese el nombre de la luz a eliminar: ")
         luces = eliminar_luz(luces, luz_eliminar)


    elif opcion == "5":
        automatizacion_por_horario(luces)
        print("Modo de ahorro de energia ejecutado.")
        
    elif opcion == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opcion no valida, elije una opcion del 1 al 6.")