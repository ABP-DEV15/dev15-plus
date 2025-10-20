from dao.usuario_dao import UsuarioDAO
from dao.usuarios_vivienda_dao import UsuariosViviendaDAO
from dao.luces_dao import LucesDAO
from dao.vivienda_dao import ViviendaDAO
from dominio.clases_base.usuarios import Usuario
from dominio.usuario_administrador import UsuarioAdministrador
from dominio.usuario_estandar import UsuarioEstandar
from dominio.luces import Luces
from conn.dbconn import DBConn


class Main:

    def menu(self):
        print("1. Iniciar sesión")
        print("2. Crear usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion


    def inciar_sesion(self):
        usuario_dao = UsuarioDAO(DBConn('config.ini'))
        input_usuario = input("Ingrese su usuario: ")
        input_contraseña = input("Ingrese su contraseña: ")
        usuario = usuario_dao.validar_contraseña(input_usuario, input_contraseña)
        if not usuario:
            print("Usuario o contraseña incorrectos.")
            return
        usuario_dao = UsuarioDAO(DBConn('config.ini'))
        usuario = usuario_dao.get(input_usuario)
        return usuario

    def menu_estandar(self, usuario: Usuario):
        estandar = UsuarioEstandar(usuario.usuario, usuario.contraseña, usuario.dni)
        print(f"Bienvenido, {estandar.usuario}!")
        print("1. Consultar datos")
        print("2. Cerrar sesión")
        input_opcion = input("Seleccione una opción: ")
        if input_opcion == "1":
            print(estandar.llamar_datos())
            self.menu_estandar(usuario)
        if input_opcion == "2":
            self.menu()

    def obtener_viviendas_usuario(self, id_usuario):
        usuarios_vivienda_dao = UsuariosViviendaDAO(DBConn('config.ini'))
        id_vivienda = usuarios_vivienda_dao.get(id_usuario)
        viviendadao = ViviendaDAO(DBConn('config.ini'))
        vivienda = viviendadao.get(id_vivienda)
        luces_vivienda = LucesDAO(DBConn('config.ini'))
        luces = luces_vivienda.get_all_data(vivienda.id_vivienda)
        vivienda.luces = luces
        return vivienda

#Estamos aqui
    def menu_admin(self, usuario: Usuario):
        admin = UsuarioAdministrador(usuario.usuario, usuario.contraseña, usuario.dni)
        print(f"Bienvenido, {admin.usuario}!")
        usuario_dao = UsuarioDAO(DBConn('config.ini'))
        id_usuario = usuario_dao.get_id_by_username(admin.usuario)
        vivienda = self.obtener_viviendas_usuario(id_usuario)
        print(f"Usted tiene acceso a la vivienda en {vivienda.calle} {vivienda.altura}, {vivienda.ciudad}")
        print("1. Gestionar dispositivos")
        print("2. Modificar Rol de usuario")
        print("3. Salir")
        input_opcion = input("Seleccione una opción: ")
        if input_opcion == "1":
            luces_dao = LucesDAO(DBConn('config.ini'))
            print("Que desea hacer?")
            print("1. Obtener luz")
            print("2. Ver todas las luces")
            print("3. Crear luz")
            print("4. Actualizar luz")
            print("5. Eliminar luz")
            input_opcion = input("Seleccione una opción: ")
            if input_opcion == "1":
                nombre_luz = input("Ingrese el id de la luz: ")
                luz = luces_dao.get(nombre_luz, vivienda.id_vivienda)
                if luz:
                    print(f"Luz: {luz.nombre}, Intensidad: {luz.intensidad}")
                else:
                    print("Luz no encontrada.")
                self.menu_admin(usuario)
            if input_opcion == "2":
                for luz in vivienda.luces:
                    print(f"Luz: {luz.nombre}, Intensidad: {luz.intensidad}")
                self.menu_admin(usuario)
            if input_opcion == "3":
                nombre_luz = input("Ingrese el nombre de la luz: ")
                intensidad = input("Ingrese la intensidad de la luz: ")
                nueva_luz = Luces(nombre=nombre_luz, intensidad=intensidad)
                luces_dao.create(nueva_luz, vivienda.id_vivienda)
                print("Luz creada exitosamente.")
                self.menu_admin(usuario)
            if input_opcion == "4":
                luces_dao = LucesDAO(DBConn('config.ini'))
                nombre_luz = input("Ingrese el id de la luz a actualizar: ")
                luz = luces_dao.get(nombre_luz, vivienda.id_vivienda)
                print(luz.nombre)
                if luz:
                    luces_dao = LucesDAO(DBConn('config.ini'))
                    viejo_nombre = luz.nombre
                    nuevo_nombre = input("Ingrese el nuevo nombre de la luz: ")
                    nueva_intensidad = input("Ingrese la nueva intensidad de la luz: ")
                    luz.nombre = nuevo_nombre
                    luz.intensidad = nueva_intensidad
                    luces_dao.update(luz, viejo_nombre)
                    print("Luz actualizada exitosamente.")
                else:
                    print("Luz no encontrada.")
                self.menu_admin(usuario)
            if input_opcion == "5":
                nombre_luz = input("Ingrese el id de la luz a eliminar: ")
                luz = luces_dao.get(nombre_luz, vivienda.id_vivienda)
                if luz:
                    luces_dao = LucesDAO(DBConn('config.ini'))
                    luces_dao.delete(nombre_luz)
                    print("Luz eliminada exitosamente.")
                else:
                    print("Luz no encontrada.")
                self.menu_admin(usuario)
        if input_opcion == "2":
            usuario_dao = UsuarioDAO(DBConn('config.ini'))
            usuario_a_modificar = input("Ingrese el nombre de usuario al que desea modificar el rol: ")
            usuario_mod = usuario_dao.get(usuario_a_modificar)
            if usuario_mod:
                print(f"El rol actual de {usuario_mod.usuario} es {usuario_mod.rol}")
                nuevo_rol = input("Ingrese el nuevo rol (estandar/admin): ")
                if nuevo_rol in ['estandar', 'admin']:
                    usuario_dao = UsuarioDAO(DBConn('config.ini'))
                    usuario_mod.rol = nuevo_rol
                    usuario_dao.update(usuario_mod)
                    print("Rol actualizado exitosamente.")
                    self.menu_admin(usuario)
                else:
                    print("Rol inválido. Debe ser 'estandar' o 'admin'.")
                    self.menu_admin(usuario)
            else:
                print("Usuario no encontrado.")
        if input_opcion == "3":
            print("Saliendo...")
            return

    def manejar_login(self, opcion):
        match opcion:
            case "1":
                inicio = self.inciar_sesion()
                if inicio.rol == 'estandar':
                    self.menu_estandar(inicio)
                self.menu_admin(inicio)
            case "2":
                usuario_dao = UsuarioDAO(DBConn('config.ini'))
                nuevo_usuario = input("Ingrese el nombre de usuario: ")
                
                if usuario_dao.check_duplicate(nuevo_usuario):
                    print("El usuario ya existe ingrese otro")
                    self.manejar_login(self.menu())
                
                nueva_contraseña = input("Ingrese la contraseña: ")
                nuevo_dni = input("Ingrese el DNI: ")
                if len(nuevo_dni) > 8:
                    print("El Dni es demasiado largo")
                    self.manejar_login(self.menu())

                usuario = Usuario(nuevo_usuario, nueva_contraseña, nuevo_dni, 'estandar')
                usuario_dao = UsuarioDAO(DBConn('config.ini'))
                usuario_dao.create(usuario)
                self.manejar_login(self.menu())
            case "3":
                print("Saliendo...")
                return
view = Main()

view.manejar_login(view.menu())
