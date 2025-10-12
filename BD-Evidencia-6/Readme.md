# SmartHome Luces Inteligentes- Base de Datos

## Scripts de Base de Datos

Este repositorio contiene los scripts SQL para la base de datos del sistema SmartHome Luces Inteligentes.

###  Estructura de archivos
- `SmartHome_DLL.sql` - Script DDL utilizado en la evidencia 5
- `SmartHome_DML.sql` - Script DML 

## Ejecución en OneCompiler (MySQL)

### Pasos para ejecutar:
1.  Abrir directamente OneCompiler con el dml y dll ya cargado:
    [https://onecompiler.com/mysql/43zfcv9he]
# =============================================

1. ** O Abrir OneCompiler MySQL**
   Ve a: [https://onecompiler.com/mysql/](https://onecompiler.com/mysql/)

2. **Ejecutar script DDL (Estructura)**
   ```sql
   -- Copia y pega todo el contenido de SmartHome_DLL.sql
   -- en el editor de OneCompiler y haz clic en "Run"

3. **Ejecutar script DML (Datos)**
    ```sql
    -- Copia y pega todo el contenido de SmartHome_DML.sql
    -- en el editor de OneCompiler y haz clic en "Run"

4. **Verificar la ejecución**

    Deberías ver mensajes de éxito para cada comando

    Las consultas SELECT al final mostrarán los datos insertados

5. **Consultas incluidas en el DML**
# =============================================
# CONSULTAS SIMPLES
# =================

# Ver todos los usuarios
SELECT * FROM usuarios;

# Ver todas las viviendas
SELECT * FROM viviendas;

# Ver todas las luces
SELECT * FROM luces;

# Ver la relacion usuarios_viviendas
SELECT * FROM usuarios_viviendas;


# CONSULTAS MULTITABLAS
# =====================

# 1 Consulta Multitabla: Usuarios con acceso a viviendas

# 2 Consulta Multitabla: Inventario de luces por vivienda

# 3 Consulta Multitabla: Consumo energético por vivienda

# 4 Consulta Multitabla: Estado de luces por ciudad

# SUBCONSULTAS
# =============

# 1 SubConsulta: Viviendas con más luces que el promedio

# 2 SubConsulta: Usuarios con acceso a múltiples ciudades  


5. **Estructura de Base de Datos**

    A- usuarios - Usuarios del sistema (admin y estándar)

    B- viviendas - Direcciones de las viviendas

    C- luces - Dispositivos de iluminación

    D- usuarios_viviendas - Relación muchos-a-muchos entre usuarios y viviendas

6. **DBMS utilizado: MySQL 8.0 ( compatible con OneCompiler)**