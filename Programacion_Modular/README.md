# SmartHome - Sistema de Gestión de Luces Inteligentes 💡

Este proyecto es una aplicación escrita en Python para gestionar un sistema de luces inteligentes.  
Permite listar, buscar, agregar y eliminar luces, además de activar un modo de ahorro de energía.

## 🗂️ Estructura del Proyecto

```
   dev15-plus/
   ├── src/                      # código fuente (Ev2 y Ev3)
   │     ├── data/  
   │     │      ├── luces_data.py
   │     │      ├── user.py
   │     ├── services/
   │            ├── gestion_dispositivos.py
   │           
   ├── main.py
   ├── menu_luces.py 
   │
   ├── docs/   # toda la documentación (Ev2 y Ev3)
   │   ├── ev2y3/   # documentos de la Evidencia 3
   │   │   ├── ev2_automatizacion.pdf
   │   │   ├── Diagrama_entidad_relacion.sgv
   │   │   ├── ev3_modelo_relacional.pdf
   │   │   ├── ev3_informe_eticaymanual_etico.pdf
   │       
   └── README.md
```

## Funcionalidades Menu_luces.py (Menu Principal)

- Listar todas las luces registradas  
- Buscar una luz por nombre  
- Agregar una nueva luz  
- Eliminar una luz existente  
- Activar el modo de ahorro de energía(Apaga todas las luces excepto la del frente)
- Modificar estado de una Luz (Encendido apagado)

## Funcionalidades Main.py (Gestion de usuarios)
- Creacion de nuevos usuarios
- Modificacion de perfiles de usuarios
- Informacion de Usuarios
- Acciones con usuarios administradores y usuarios regular.

## Cómo ejecutar

1. Cloná este repositorio:
   ```bash
   git clone https://[https://github.com/ABP-DEV15/dev15-plus/]  
2. Ejecutar con Python: el main.py si quiere ingresar con usuarios ya precargados, modificarlos o agregar nuevos o ver informacion de los usuarios.
3. Ejecutar menu_luces.py si quieres administrar el sistema de luces inteligentes. 
