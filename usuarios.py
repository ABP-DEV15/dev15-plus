from datausers import *

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
        print('usuario regular')
    else:
        hacer = input('Que desea hacer?: ' \
        '1 consultar automatizaciones, ' \
        '2 Automatizar dispositivo, ' \
        '3 modificar rol de usuario')
        match hacer:
            case '3':
                data = input('Cual es el nombre del usuario que desea modificar: ')
                user['usuario'] = data
                modificar_usuario(user)

def main():
    option = input("Bievenido, en caso de tener un usuario escriba 1, en caso de necesitar registrarse escriba 2:")
    match option:
        case '1':
            ingreso = inicio_sesion()
            if ingreso[0]:
                view_main(ingreso[1])
            else:
                print(ingreso[1])
                ingreso = inicio_sesion()
        case '2':
            registro()
        case _:
            print('Por favor, ingrese una opcion valida')    

main()

