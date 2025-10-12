import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data.users import USUARIOS, buscar_usuario, insertar_usuarios, modificar_usuario, mostrar_datos_personales
from data.luces_data import cargar_luces
from services.gestion_dispositivos import listar_luces, automatizacion_por_horario


def inicio_sesion():
    data = {}
    usuario = input('Ingrese su usuario: ')
    data['usuario'] = usuario
    password = input('Ingrese su contraseña de acceso: ')
    data['password'] = password
    return buscar_usuario(data)

def registro():
    data = {}
    usuario = input('Ingrese su nombre de usuario: ')
    data['usuario'] = usuario
    password = input('Ingrese su contraseña: ')
    data['password'] = password
    dni = input('Ingrese su DNI: ')
    data['dni'] = dni
    
    if insertar_usuarios(data, USUARIOS):
        print('Usuario creado. Use sus credenciales para ingresar.')
        return buscar_usuario(data)
    else:
        return False, "Error al registrar usuario"

def view_main(usuario):
    if usuario['rol'] == 'regular':
        mostrar_datos_personales(usuario)

    elif usuario['rol'] == 'admin':
        while True:
            hacer = input(
                "\n¿Qué desea hacer?:\n"
                "1. Consultar estado de luces\n"
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
                    usuario_modificar = input('Ingrese usuario a modificar: ')
                    nuevo_rol = input('Nuevo rol (admin/regular): ')
                    
                    resultado = modificar_usuario({
                        'usuario': usuario_modificar,
                        'rol': nuevo_rol
                    })
                    
                    if resultado:
                        print(f"Rol de {usuario_modificar} cambiado a {nuevo_rol}")
                    else:
                        print("Error al modificar el usuario")

                case '4':
                    break

                case _:
                    print("Opción inválida.")
    else:
        print("Rol no reconocido.")

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