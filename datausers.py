import os
import json

USUARIOS = os.path.join(os.path.dirname(__file__), "data/users.json")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def insertar_usuarios(data, dir):
    if os.path.exists(dir) and os.path.getsize(dir) != 2:
        with open(dir, "r") as file:
            datos = json.load(file)
        new = data
        new['rol'] = 'regular'
        datos.append(new)
        with open(dir, 'w') as file:
            json.dump(datos, file, indent=4)
    else:
        datos = [ {
            'usuario' : data['usuario'],
            'password': data['password'],
            'rol': 'admin',
            'dni': '00'
            }
        ]
        with open(dir, 'w') as file:
            json.dump(datos, file, indent=4)

def buscar_usuario(user):
    with open(USUARIOS, 'r') as file:
        data = json.load(file)
        usuario = next((item for item in data if item.get("usuario") == user['usuario']), None)    
    if usuario:
        password = next((item for item in data if item.get("password") == user['password']), None)    
        if password:
            return True, usuario['rol']
        else:
            return False, 'No ingresa'
    else:
        return False, 'No ingresa'
        
            
def modificar_usuario(user):
    with open(USUARIOS, 'r') as file:
        data = json.load(file)
        usuario = next((item for item in data if item.get("usuario") == user['usuario']), None)
        if usuario:
            usuario['rol'] = 'admi'

    with open(USUARIOS, 'w') as file:
        json.dump(data, file, indent=4)
user = {
    'usuario': 'prueba',
    'password': '1234'
}

#insertar_usuarios(user, USUARIOS)

#buscar_usuario(user)

#modificar_usuario({'usuario': 'caray'})

