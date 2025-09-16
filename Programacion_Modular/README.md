# SmartHome - Sistema de Gestión de Luces Inteligentes 💡

Este proyecto es una aplicación escrita en Python para gestionar un sistema de luces inteligentes.  
Permite listar, buscar, agregar y eliminar luces, además de activar un modo de ahorro de energía.

## 🗂️ Estructura del Proyecto

```
   dev15-plus/
   ├── src/                      # código fuente (Ev2 y Ev3)
   │     ├── data/  
   │     │      ├── luces.json
   │     │      ├── user.json
   │     ├── services/
   │     │      ├── gestion_dispositivos.py
   │     │      ├── luces.py
   ├── datauser.py
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

## Funcionalidades

- Listar todas las luces registradas  
- Buscar una luz por nombre  
- Agregar una nueva luz  
- Eliminar una luz existente  
- Activar el modo de ahorro de energía(Apaga todas las luces excepto la del frente)

## Cómo ejecutar

1. Cloná este repositorio:
   ```bash
   git clone https://[https://github.com/ABP-DEV15/dev15-plus/]  
2. Ejecutar con Python:
   main.py
