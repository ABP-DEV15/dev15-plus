# SmartHome - Sistema de Gestión de Luces Inteligentes 💡

Este proyecto es una aplicación escrita en Python para gestionar un sistema de luces inteligentes.  
Permite listar, buscar, agregar y eliminar luces, además de activar un modo de ahorro de energía.

## 🗂️ Estructura del Proyecto

```
   dev15-plus/
   ├── src/                      # código fuente (principalmente Ev2 y Ev3)
   ├── docs/                     # toda la documentación
   │   ├── ev2/                  # documentos de la Evidencia 2
   │   │   ├── ev2_automatizacion.pdf
   │   │   ├── ev2_der_modelo.pdf
   │   │   └── ev2_politica_datos.pdf
   │   ├── ev3/                  # documentos de la Evidencia 3
   │   │   ├── ev3_modelo_relacional.pdf
   │   │   ├── ev3_informe_etica.pdf
   │   │   ├── ev3_manual_etico.pdf
   │   │   └── ev3_demo_link.txt   # o ponerlo también en README
   │   └── ev5/                  # (cuando llegues a esta etapa)
   │       ├── diagrama_clases.pdf
   │       └── justificacion_poo.pdf
   ├── POO-SmartHome/            # código POO + TDD (Ev5)
   ├── BD-Evidencia-5/           # scripts SQL (Ev5)
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
