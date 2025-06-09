from datausers import *
from luces import *

def inicio_sesion():
    data = {}
    usuario = input('Ingrese su usuario: ')
    data['usuario'] = usuario
    password = input('Ingrese su credencial de acceso: ')
    data['password'] = password
    return buscar_usuario(data)

def registro():
    data = {}
    usuario = input('Ingrese su nombre de usuario: ')
    data['usuario'] = usuario
    password = input('ingrese su contreña: ')
    data['password'] = password
    dni = input('Ingrese su DNI: ')
    data['dni'] = dni
    insertar_usuarios(data, USUARIOS)
    print('Use su nuevo usuario')
    inicio_sesion()


def view_main(usuario):
   if usuario['rol'] == 'regular':
        mostrar_datos_personales(usuario)
    elif usuario['rol'] == 'admin':
        while True:
            hacer = input(
                "\n¿Qué desea hacer?:\n"
                "1. Consultar automatizaciones\n"
                "2. Automatizar dispositivo (modo ahorro)\n"
                "3. Modificar rol de usuario\n"
                "4. Salir\n"
                "Seleccione una opción: "
            )
        match hacer:
            case '1':
                luces = cargar_luces()
                listar_luces(luces)
            case '2':
                luces = cargar_luces()
                automatizacion_por_horario(luces)
            case '3':
                email = input('Email del usuario a modificar: ')
                modificar_usuario(email)
            case '4':
                break
            case _:
                print("Opción inválida.")
    else:
        print("Rol no reconocido.")
        
def main():
    option = input("Bievenido, en caso de tener un usuario escriba 1, en caso de necesitar registrarse escriba 2:")
    match option:
        case '1':
            ingreso = inicio_sesion()
            if exito:
                view_main(usuario)
            else:
                print(usuario) 
        case '2':
            exito, usuario = registro()
            if exito:
                view_main(usuario)
        case _:
            print('Por favor, ingrese una opcion valida')    

if __name__ == "__main__":
    main()

