
```
    │──BD-EVIDENCIA-5  # Scripts SQL
    │    │   ├── Readme.md # Explicacion de como ejecutar los Scripts
    │    │   ├── smartHome_DLL.sql # DLL de las tablas Viviendas, Usuarios, Luces y Usuarios_Viviendas
    │    │   └── SmartHome_DML.sql # DML para insertar datos y realizar consultas.
    │
    │──DC-EVIDENCIA-5  # Diagrama de clases
    │    │   ├── Diagrama de Clases
    │    │   ├── fundamentos POO del diagrama de clases
    │
    │──POO-SmartHome/ # código POO + TDD (Ev5)
        ─App
           │   config.ini
           │   Poo.pdf
           │
           ├───conn
           │   │   
           │   └───dbconn.py
           │   
           │
           ├───dao
           │   │   luces_dao.py
           │   │   usuario_dao.py
           │   │   vivienda_dao.py
           │
           ├───dominio
           │   │   dispositivo.py
           │   │   luces.py
           │   │   usuarios.py
           │   │   vivienda.py
           │
           ├───interface
           │   │   data_access_dao.py
           │
           ├───test
              │   luces_controlador_test.py
              │   luces_test.py
              │   usuarios_test.py
              │   usuario_controlador_test.py
              │   vivienda_test.py
               └── README.md
    │
    │──Programacion_Modular # Evidencia-3
      │     ├── src/                      # código fuente (Ev2 y Ev3)
      │     ├── data/  
      │     │      ├── luces_data.py
      │     │      ├── user.py
      │     ├── services/
      │            ├── gestion_dispositivos.py
      │           
      ├── main.py  # Gestion de usuarios
      ├── menu_luces.py  # Gestion del Menu Principal de Luces
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
