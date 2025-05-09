-- Crear la base de datos
CREATE DATABASE materias;

-- Usar la base de datos
USE materias;

-- Crear la tabla asignaturas
CREATE TABLE asignaturas (
    codigo INT PRIMARY KEY,
    nombre VARCHAR(100),
    creditos INT
);

-- Insertar los datos
INSERT INTO asignaturas (codigo, nombre, creditos) VALUES
(183224, 'Matemática', 6),
(224981, 'Química', 5),
(274192, 'Lógica de programación', 4),
(273914, 'Educación Física', 3),
(323253, 'Física', 5),
(394014, 'Biología', 4),
(604212, 'Marketing', 3),
(604213, 'Derecho Laboral', 3),
(683214, 'Teoría de bases de datos', 5),
(729312, 'Realidad Nacional', 3),
(903105, 'Ingeniería de montañas', 4),
(920418, 'Lenguaje', 4);
