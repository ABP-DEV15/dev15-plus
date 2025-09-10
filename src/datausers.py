import os
import json

USUARIOS = os.path.join(os.path.dirname(__file__), "src/data/users.json")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def insertar_usuarios(data, dir):
    if os.path.exists(dir) and os.path.getsize(dir) > 2:
        with open(dir, "r") as file:
            datos = json.load(file)
        if any(u["usuario"] == data["usuario"] for u in datos):
            print("El usuario ya existe.")
            return
        data["rol"] = "regular"
        datos.append(data)
    else:
        print("Primer usuario registrado, asignado como admin.")
        datos = [{
            'usuario': data['usuario'],
            'password': data['password'],
            'rol': 'admin',
            'dni': data.get('dni', '00')
        }]
    with open(dir, 'w') as file:
        json.dump(datos, file, indent=4)
    print("Usuario insertado correctamente.")

def buscar_usuario(user):
    with open(USUARIOS, 'r') as file:
        data = json.load(file)
        usuario = next(
            (item for item in data if item.get("usuario") == user['usuario'] and item.get("password") == user['password']),
            None
        )
    if usuario:
        return True, usuario
    else:
        return False, 'Usuario o contraseña incorrectos'
        
            
def modificar_usuario(user):
    with open(USUARIOS, 'r') as file:
        data = json.load(file)
        usuario = next((item for item in data if item.get("usuario") == user['usuario']), None)
        if usuario:
            nuevo_rol = input(f"Ingrese nuevo rol para '{user['usuario']}' (admin/regular): ").strip().lower()
            if nuevo_rol in ['admin', 'regular']:
                usuario['rol'] = nuevo_rol
                print(f"Rol del usuario '{user['usuario']}' actualizado a '{nuevo_rol}'.")
            else:
                print("Rol no válido. Debe ser 'admin' o 'regular'.")
        else:
            print("Usuario no encontrado.")

    with open(USUARIOS, 'w') as file:
        json.dump(data, file, indent=4)
user = {
    'usuario': 'prueba',
    'password': '1234'
}

def mostrar_datos_personales(usuario_actual):
    with open(USUARIOS, 'r') as file:
        data = json.load(file)
        usuario = next((item for item in data if item.get("usuario") == usuario_actual['usuario']), None)
        if usuario:
            print("\n--- DATOS PERSONALES ---")
            print(f"Usuario: {usuario['usuario']}")
            print(f"DNI: {usuario['dni']}")
            print(f"Rol: {usuario['rol']}")
        else:
            print("Usuario no encontrado.")

