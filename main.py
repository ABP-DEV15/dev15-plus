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


def view_main(data):
    if data == 'regular':
        mostrar_datos_personales(data)
    else:
        hacer = input('Que desea hacer?: ' \
        '1. consultar automatizaciones, ' \
        '2. Automatizar dispositivo, ' \
        '3. modificar rol de usuario ' \
        '4. Salir ' \
        'Seleccione una opción: ')
        match hacer:
            case '1':
                    luces = cargar_luces()
                    listar_luces(luces)
            case '2':
                    luces = cargar_luces()
                    automatizacion_por_horario(luces)
            case '3':
                data = input('Cual es el nombre del usuario que desea modificar: ')
                user['usuario'] = data
                modificar_usuario(user)
            case '4':
                    print("Saliendo del menú de administrador.")
                    break
            case _:
                    print("Opción inválida.")

def main():
    opcion = input("Bienvenido. Si tiene usuario escriba 1. Para registrarse escriba 2: ")
    match opcion:
        case '1':
            exito, usuario = inicio_sesion()
            if exito:
                view_main(usuario)
            else:
                print(usuario) 
        case '2':
            exito, usuario = registro()
            if exito:
                view_main(usuario)
        case _:
            print('Por favor, ingrese una opción válida')

if __name__ == "__main__":
    main()
