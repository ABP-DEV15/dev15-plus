INSERT INTO usuarios (usuario, contrasena, dni, rol) VALUES
('admin', '4dmin$$F', '12345678', 'admin'),
('maria_soledad', 'HolaMari$', '23456789', 'estandar'),
('juan_p', '$HelloJuan$', '34567890', 'estandar'),
('laura_otta', '$Pass$$Hola', '45678901', 'estandar'),
('carlos_martinez', 'K4rl0s$$', '56789012', 'estandar'),
('ana_garcia', 'AnaG2024$', '67890123', 'estandar'),
('pedro_lopez', 'P3dr0$$L', '78901234', 'estandar'),
('lucia_fernandez', 'Luc1aF$', '89012345', 'estandar'),
('miguel_torres', 'M1gu3lT$$', '90123456', 'estandar'),
('elena_ruiz', '3l3n4R$', '01234567', 'estandar');

# Insertar 10 viviendas
INSERT INTO viviendas (calle, altura, ciudad) VALUES
('Rogelio', 123, 'Cordoba'),
('Avenida Libertador', 456, 'Buenos Aires'),
('Ruta 22', 789, 'Rio Negro'),
('Calle Sol', 321, 'Laberiso'),
('Avenida Cabildo', 742, 'Buenos Aires'),
('Pasaje Carlucci', 654, 'Cordoba'),
('Calle Florida', 100, 'Buenos Aires'),
('Avenida Siempre Viva', 742, 'Springfield'),
('Calle Principal', 50, 'Mendoza'),
('Rivadavia', 1500, 'Buenos Aires');

# Insertar relaciones usuarios_viviendas
INSERT INTO usuarios_viviendas (id_usuario, id_vivienda) VALUES
(1, 1), (2, 1), (2, 2), (3, 2), (3, 3),
(4, 4), (5, 5), (5, 6), (6, 7), (7, 8),
(8, 9), (9, 10), (10, 1), (10, 3);

# Insertar luces de viviendas 
INSERT INTO luces (nombre, encendida, intensidad, id_vivienda) VALUES
# Vivienda 1
('Luz Sala', 1, 80, 1),
('Luz Cocina', 0, 0, 1),
('Luz Dormitorio', 1, 50, 1),
# Vivienda 2
('Luz Living', 1, 75, 2),
('Luz Comedor', 0, 0, 2),
('Luz Jardín', 1, 30, 2),
# Vivienda 3
('Luz Entrada', 1, 100, 3),
('Luz Garaje', 0, 0, 3),
# Vivienda 4
('Luz Sala Estar', 1, 60, 4),
('Luz Cocina', 1, 40, 4),
# Vivienda 5
('Luz Patio', 1, 20, 5),
# Vivienda 6
('Luz Estudio', 1, 90, 6);

# =============================================
# CONSULTAS SIMPLES
# =============================================

# Ver todos los usuarios
SELECT * FROM usuarios;

# Ver todas las viviendas
SELECT * FROM viviendas;

# Ver todas las luces
SELECT * FROM luces;

# Ver la relacion usuarios_viviendas
SELECT * FROM usuarios_viviendas;


# CONSULTAS MULTITABLAS
# =============================================

# 1 Consulta Multitabla: Usuarios con acceso a viviendas
# Justificacion: Permite verificar qué usuarios pueden acceder a que viviendas
SELECT 
    u.id_usuario AS 'ID Usuario',
    u.usuario AS 'Usuario',
    u.rol AS 'Rol',
    v.id_vivienda AS 'ID Vivienda',
    CONCAT(v.calle, ' ', v.altura, ', ', v.ciudad) AS 'Dirección Completa'
FROM usuarios u
JOIN usuarios_viviendas uv ON u.id_usuario = uv.id_usuario
JOIN viviendas v ON uv.id_vivienda = v.id_vivienda
ORDER BY u.usuario, v.id_vivienda;

# 2 Consulta Multitabla: Inventario de luces por vivienda
# Justificacion: Proporciona un inventario de luces por vivienda
SELECT 
    l.id_luz AS 'ID Luz',
    l.nombre AS 'Nombre Luz',
    CASE 
        WHEN l.encendida = 1 THEN 'ENCENDIDA'
        ELSE 'APAGADA'
    END AS 'Estado',
    l.intensidad AS 'Intensidad',
    v.id_vivienda AS 'ID Vivienda',
    CONCAT(v.calle, ' ', v.altura, ', ', v.ciudad) AS 'Dirección Completa'
FROM luces l
JOIN viviendas v ON l.id_vivienda = v.id_vivienda
ORDER BY v.id_vivienda, l.nombre;

# 3 Consulta Multitabla: Consumo energético por vivienda
# Justificacion: Calcula el consumo energético por vivienda
SELECT 
    v.id_vivienda,
    v.calle,
    v.altura,
    v.ciudad,
    COUNT(l.id_luz) AS 'Total Luces',
    SUM(l.intensidad) AS 'Consumo Total',
    AVG(l.intensidad) AS 'Intensidad Promedio'
FROM viviendas v
LEFT JOIN luces l ON v.id_vivienda = l.id_vivienda AND l.encendida = 1
GROUP BY v.id_vivienda, v.calle, v.altura, v.ciudad
ORDER BY SUM(l.intensidad) DESC;

# 4 Consulta Multitabla: Estado de luces por ciudad
# Justificacion: Resumen rapido del estado de las luces agrupado por ciudad
SELECT 
    v.ciudad AS 'Ciudad',
    COUNT(l.id_luz) AS 'Total Luces',
    SUM(CASE WHEN l.encendida = 1 THEN 1 ELSE 0 END) AS 'Luces Encendidas',
    SUM(CASE WHEN l.encendida = 0 THEN 1 ELSE 0 END) AS 'Luces Apagadas',
    ROUND((SUM(CASE WHEN l.encendida = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(l.id_luz)), 1) AS '% Encendidas'
FROM viviendas v
JOIN luces l ON v.id_vivienda = l.id_vivienda
GROUP BY v.ciudad
ORDER BY COUNT(l.id_luz) DESC;

# SUBCONSULTAS
# =============

# 1 SubConsulta: Viviendas con más luces que el promedio
# Justificacion: Identifica viviendas con mayor cantidad de dispositivos para mantenimiento
SELECT 
    v.id_vivienda,
    v.calle,
    v.altura,
    v.ciudad,
    COUNT(l.id_luz) AS 'Cantidad de Luces'
FROM viviendas v
JOIN luces l ON v.id_vivienda = l.id_vivienda
GROUP BY v.id_vivienda, v.calle, v.altura, v.ciudad
HAVING COUNT(l.id_luz) > (
    SELECT AVG(conteo_luces) 
    FROM (
        SELECT COUNT(id_luz) AS conteo_luces 
        FROM luces 
        GROUP BY id_vivienda
    ) AS promedios
)
ORDER BY COUNT(l.id_luz) DESC;

# 2 SubConsulta: Usuarios con acceso a múltiples ciudades  
# Justificacion: Ayuda a la gestion de permisos identificando usuarios con acceso a viviendas para posibles ajustes
SELECT 
    u.usuario,
    u.dni,
    u.rol,
    COUNT(DISTINCT v.ciudad) AS 'Ciudades Diferentes'
FROM usuarios u
JOIN usuarios_viviendas uv ON u.id_usuario = uv.id_usuario
JOIN viviendas v ON uv.id_vivienda = v.id_vivienda
GROUP BY u.id_usuario, u.usuario, u.dni, u.rol
HAVING COUNT(DISTINCT v.ciudad) > 1
ORDER BY COUNT(DISTINCT v.ciudad) DESC;
