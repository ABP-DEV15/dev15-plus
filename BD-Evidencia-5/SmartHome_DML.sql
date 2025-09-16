INSERT INTO usuarios (usuario, contrasena, dni, rol) VALUES
('admin', '4dmin$$F', '12345678', 'admin'),
('maria_soledad', 'HolaMari$', '23456789', 'estandar'),
('juan_p', '$HelloJuan$', '34567890', 'estandar'),
('laura_otta', '$Pass$$Hola', '45678901', 'estandar'),
('carlos_martinez', 'K4rl0s$$', '56789012', 'estandar');

INSERT INTO viviendas (calle, altura, ciudad) VALUES
('Rogelio', 123, 'Cordoba'),
('Avenida Libertador', 456, 'Buenos Aires'),
('Ruta 22', 789, 'Rio Negro'),
('Calle Sol', 321, 'Laberiso'),
('Avenida Cabildo', 742, 'Buenos Aires'),
('Pasaje Carlucci', 654, 'Cordoba');

INSERT INTO usuarios_viviendas (id_usuario, id_vivienda) VALUES
(1, 1), -- admin tiene acceso a vivienda 1
(2, 1), -- maria_soledad tiene acceso a vivienda 1
(2, 2), -- maria_soledad tiene acceso a vivienda 2
(3, 2), -- juan_p tiene acceso a vivienda 2
(3, 3), -- juan_p tiene acceso a vivienda 3
(4, 4), -- laura_otta tiene acceso a vivienda 4
(5, 5), -- carlos_martinez tiene acceso a vivienda 5
(5, 6); -- carlos_martinez tiene acceso a vivienda 6

INSERT INTO luces (nombre, encendida, intensidad, id_vivienda) VALUES
-- Vivienda 1
('Luz Sala', 1, 80, 1),
('Luz Cocina', 0, 0, 1),
('Luz Dormitorio', 1, 50, 1),
-- Vivienda 2
('Luz Living', 1, 75, 2),
('Luz Comedor', 0, 0, 2),
('Luz Jard�n', 1, 30, 2),
-- Vivienda 3
('Luz Entrada', 1, 100, 3),
('Luz Garaje', 0, 0, 3),
-- Vivienda 4
('Luz Sala Estar', 1, 60, 4),
('Luz Cocina', 1, 40, 4),
-- Vivienda 5
('Luz Patio', 1, 20, 5),
-- Vivienda 6
('Luz Estudio', 1, 90, 6);

-- Ver todos los usuarios
SELECT * FROM usuarios;

-- Ver todas las viviendas
SELECT * FROM viviendas;

-- Ver todas las luces
SELECT * FROM luces;

-- Ver la relación usuarios_viviendas
SELECT * FROM usuarios_viviendas;


