# SmartHome - Sistema de Gestión de Luces Inteligentes 💡

Este proyecto es una aplicación escrita en Python para gestionar un sistema de luces inteligentes.  
Permite listar, buscar, agregar y eliminar luces, además de activar un modo de ahorro de energía.

## 🗂️ Estructura del Proyecto

```
dev15-plus/
├── main.py                          # Programa principal
└── src/
    ├── data/
    │   └── luces.json              # JSON que actúa como base de datos
    └── services/
        ├── luces.py               # Funciones para cargar y guardar luces
        └── gestion_dispositivos.py # Funciones para operar sobre las luces
```

## Funcionalidades

- Listar todas las luces registradas  
- Buscar una luz por nombre  
- Agregar una nueva luz  
- Eliminar una luz existente  
- Activar el modo de ahorro de energía  

## Cómo ejecutar

1. Cloná este repositorio:
   ```bash
   git clone https://[https://github.com/ABP-DEV15/dev15-plus/]  
2. Ejecutar con Python:
   main.py
