USUARIOS = [
    {
        "usuario": "fabri",
        "password": "123",
        "rol": "admin",
        "dni": "00"
    },
    {
        "usuario": "Neri",
        "password": "1234",
        "dni": "42259310",
        "rol": "regular"
    },
    {
        "usuario": "amparo",
        "password": "123",
        "dni": "100000",
        "rol": "regular"
    },
    {
        "usuario": "calvo",
        "password": "1234",
        "dni": "200000",
        "rol": "regular"
    },
    {
        "usuario": "pgatica",
        "password": "123456",
        "dni": "36871744",
        "rol": "regular"
    }
]

def insertar_usuarios(data, lista_usuarios):
    # Verificar si el usuario ya existe
    for usuario in lista_usuarios:
        if usuario['usuario'] == data['usuario']:
            print("El usuario ya existe")
            return False
    
    # Asignar rol - si es el primer usuario sera admin, sino regular
    if not lista_usuarios:
        print("Primer usuario registrado, asignado como admin.")
        data["rol"] = "admin"
    else:
        data["rol"] = "regular"
    
    # Agregar a la lista
    lista_usuarios.append(data)
    print(f"Usuario {data['usuario']} registrado exitosamente")
    return True

def buscar_usuario(user):
    usuario = next(
        (item for item in USUARIOS if item.get("usuario") == user['usuario'] and item.get("password") == user['password']),
        None
    )
    if usuario:
        return True, usuario
    else:
        return False, 'Usuario o contraseña incorrectos'
        
def modificar_usuario(datos):
    usuario_a_modificar = datos['usuario']
    nuevo_rol = datos['rol']
    
    for usuario in USUARIOS:
        if usuario['usuario'] == usuario_a_modificar:
            usuario['rol'] = nuevo_rol
            print(f"Rol modificado para {usuario_a_modificar}")
            return True
    
    print("Usuario no encontrado")
    return False

def mostrar_datos_personales(usuario_actual):
    usuario = next((item for item in USUARIOS if item.get("usuario") == usuario_actual['usuario']), None)
    if usuario:
        print("\n--- DATOS PERSONALES ---")
        print(f"Usuario: {usuario['usuario']}")
        print(f"DNI: {usuario['dni']}")
        print(f"Rol: {usuario['rol']}")
    else:
        print("Usuario no encontrado.")