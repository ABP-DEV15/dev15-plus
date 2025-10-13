
# SmartHome- Luces Inteligentes

Sistema de Gestion de Luces inteligentes que permite administrar luces, usuarios y viviendas, aplicando los principios POO, arquitectura modular y acceso a base de datos mediante DAO.

## Objetivos
Registro de inicio de sesion de usuarios(Administradores y estandar)
Registrar, consultar y administrar Luces.
Conectar a una Base de datos MySQL para persistencia de datos.
Automatizacion inicial Modo ahorro de energia.
## Estructura de directorios

```
SmartHome/
│
├── BD-Evidencia-5/        # Scripts SQL (DDL y DML)
├── BD-Evidencia-6/        # Consultas multitabla y subconsultas
├── DC-Evidencia-5/        # Diagrama de clases y documentación POO
├── POO-SmartHome/         # Implementación POO + DAO + main.py
│   ├── App/
│   │   ├── conn/          # Conexión a BD
│   │   ├── dao/           # Clases DAO
│   │   ├── dominio/       # Clases de dominio (POO)
│   │   ├── interface/     # DAO Interface
│   │   ├── test/          # Pruebas unitarias
│   │   └── main.py        # Punto de entrada
│   └── config.ini         # Configuración BD
└── Programacion_Modular/  # Versión inicial modular (Evidencias 2-3)
```
## Tech Stack

- **Backend:** Python
- **Database:** SQL (DDL, DML, consultas multitabla)
- **Architecture:** POO, DAO Pattern, Programación Modular
- **Tools:** Diagramas de clases, Configuración INI
- **Testing:** Pruebas unitarias
## Authors

- [dev15-plus](https://github.com/ABP-DEV15/dev15-plus)

### **Desarrolladores:**
- **Fabricio Nicolas Rivarola**
- **Pablo Emiliano Gatica**
- **Maria Pia Pereyra Tauil**
- **Alejandro Lucas Cortez**
## Ejecutar localmente

Clonar el proyecto

```bash
  git clone https://github.com/ABP-DEV15/dev15-plus
```

Ir al directorio del proyecto

```bash
  cd POO-SmartHome/App
```

Ejecutar el programa

```bash
  python main.py
```


## Estado del Proyecto
Evidencias completadas: 2, 3, 5 y 6

Pruebas unitarias: todas en verde

Revisión ética y técnica: cumplida