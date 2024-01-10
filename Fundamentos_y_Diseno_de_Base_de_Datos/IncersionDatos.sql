use DBCineplanet
INSERT INTO Empleado VALUES
('E001', 'C001', 'Juan', 'Perez', '12345678', '955123456', 'juan@email.com', 'A', '09:00:00', '17:00:00'),
('E002', 'C002', 'Maria', 'Lopez', '23456789', '956987654', 'maria@email.com', 'A', '10:00:00', '18:00:00'),
('E003', 'C003', 'Pedro', 'Gonzalez', '34567890', '957234567', 'pedro@email.com', 'A', '08:30:00', '16:30:00'),
('E004', 'C001', 'Laura', 'Ramirez', '45678901', '958345678', 'laura@email.com', 'A', '11:00:00', '19:00:00'),
('E005', 'C002', 'Carlos', 'Fernandez', '56789012', '959456789', 'carlos@email.com', 'A', '12:30:00', '20:30:00'),
('E006', 'C003', 'Isabel', 'Gutierrez', '67890123', '951567890', 'isabel@email.com', 'A', '13:45:00', '21:45:00'),
('E007', 'C001', 'Alejandro', 'Martinez', '78901234', '952678901', 'alejandro@email.com', 'A', '14:15:00', '22:15:00'),
('E008', 'C002', 'Sofia', 'Lopez', '89012345', '953789012', 'sofia@email.com', 'A', '15:30:00', '23:30:00'),
('E009', 'C003', 'Fernando', 'Hernandez', '90123456', '954890123', 'fernando@email.com', 'A', '16:45:00', '00:45:00'),
('E010', 'C001', 'Ana', 'Gomez', '98765432', '955901234', 'ana@email.com', 'A', '17:00:00', '01:00:00');

INSERT INTO Caja VALUES
('C001'),
('C002'),
('C003'),
('C004'),
('C005'),
('C006'),
('C007'),
('C008'),
('C009'),
('C010');


INSERT INTO Cliente VALUES
('CL001', 'Carlos', 'Gomez', '87654321', 'carlos@email.com', '955123456'),
('CL002', 'Ana', 'Martinez', '76543210', 'ana@email.com', '956987654'),
('CL003', 'Luis', 'Rodriguez', '65432109', 'luis@email.com', '957345678'),
('CL004', 'Elena', 'Fernandez', '54321098', 'elena@email.com', '958456789'),
('CL005', 'Juan', 'Hernandez', '43210987', 'juan@email.com', '959567890'),
('CL006', 'Isabel', 'Lopez', '32109876', 'isabel@email.com', '951678901'),
('CL007', 'Miguel', 'Ramirez', '21098765', 'miguel@email.com', '952789012'),
('CL008', 'Sofia', 'Gutierrez', '10987654', 'sofia@email.com', '953890123'),
('CL009', 'Diego', 'Fernandez', '98765432', 'diego@email.com', '954901234'),
('CL010', 'Laura', 'Gomez', '87654321', 'laura@email.com', '955012345');


INSERT INTO Producto VALUES
('P001', 'Palomitas', 5.00, 100, 'Dulceria'),
('P002', 'Refresco', 3.50, 50, 'Dulceria'),
('P003', 'Nachos', 6.50, 30, 'Dulceria'),
('P004', 'Chocolate', 2.00, 80, 'Dulceria'),
('P005', 'Gaseosa', 4.00, 60, 'Dulceria'),
('P006', 'Agua', 1.50, 40, 'Dulceria'),
('P007', 'Hot Dog', 7.00, 20, 'Dulceria'),
('P008', 'Caramelos', 1.00, 100, 'Dulceria'),
('P009', 'Chicles', 0.50, 120, 'Dulceria'),
('P010', 'Papas Fritas', 4.50, 50, 'Dulceria');

-- Insertar datos en la tabla Pelicula
INSERT INTO Pelicula VALUES
('PEL001', 'Titanic', 'Romance', '02:45:00', 'A', 'Historia de amor en un barco donde dos jóvenes se enamoran en medio de un trágico desastre.'),
('PEL002', 'Inception', 'Sci-Fi', '02:30:00', 'PG-13', 'Un ladrón de sueños realiza atracos corporativos al entrar en los sueños de otras personas.'),
('PEL003', 'The Shawshank Redemption', 'Drama', '02:22:00', 'R', 'Un hombre es condenado a cadena perpetua por un crimen que no cometió y encuentra la redención en Shawshank.'),
('PEL004', 'The Godfather', 'Crime', '02:55:00', 'R', 'El patriarca de una familia criminal intenta traspasar el negocio a su hijo, pero las tensiones y traiciones amenazan la estabilidad.'),
('PEL005', 'Forrest Gump', 'Drama', '02:22:00', 'PG-13', 'La vida extraordinaria de Forrest Gump, un hombre con discapacidades mentales, que participa en eventos clave de la historia.'),
('PEL006', 'The Dark Knight', 'Action', '02:32:00', 'PG-13', 'Batman se enfrenta al Joker, un criminal maestro que desata el caos en Gotham City.'),
('PEL007', 'Pulp Fiction', 'Crime', '02:34:00', 'R', 'Historias interconectadas de criminales, boxeadores, gánsteres y otros personajes en Los Ángeles.'),
('PEL008', 'The Matrix', 'Sci-Fi', '02:16:00', 'R', 'Un programador descubre la verdad detrás de la realidad simulada y lidera una rebelión contra las máquinas.'),
('PEL009', 'Schindler List', 'Biography', '03:15:00', 'R', 'La historia real de Oskar Schindler, un empresario alemán que salva a más de mil judíos durante el Holocausto.'),
('PEL010', 'Casablanca', 'Drama', '01:42:00', 'PG', 'En la Segunda Guerra Mundial, un dueño de un club nocturno en Casablanca se ve atrapado en un dilema moral y político.');


INSERT INTO Sala VALUES
('S001', 100, 'Normal', 'Disponible'),
('S002', 80, 'VIP', 'Ocupada'),
('S003', 120, 'Normal', 'Disponible'),
('S004', 90, 'VIP', 'Disponible'),
('S005', 150, 'Normal', 'Ocupada'),
('S006', 70, 'VIP', 'Disponible'),
('S007', 110, 'Normal', 'Ocupada'),
('S008', 60, 'VIP', 'Disponible'),
('S009', 130, 'Normal', 'Disponible'),
('S010', 85, 'VIP', 'Disponible');

INSERT INTO Butaca VALUES
('B001', 'S001', 'A1', 'Disponible'),
('B002', 'S001', 'A2', 'Disponible'),
('B003', 'S002', 'B1', 'Ocupada'),
('B004', 'S002', 'B2', 'Disponible'),
('B005', 'S003', 'C1', 'Ocupada'),
('B006', 'S003', 'C2', 'Disponible'),
('B007', 'S004', 'D1', 'Disponible'),
('B008', 'S004', 'D2', 'Disponible'),
('B009', 'S005', 'E1', 'Ocupada'),
('B010', 'S005', 'E2', 'Disponible');

INSERT INTO Horario VALUES
('H001', 'S001', '12:00:00', '14:30:00'),
('H002', 'S001', '15:00:00', '17:30:00'),
('H003', 'S002', '18:00:00', '20:30:00'),
('H004', 'S002', '21:00:00', '23:30:00'),
('H005', 'S003', '13:30:00', '16:00:00'),
('H006', 'S003', '16:30:00', '19:00:00'),
('H007', 'S004', '19:30:00', '22:00:00'),
('H008', 'S004', '22:30:00', '01:00:00'),
('H009', 'S005', '14:00:00', '16:30:00'),
('H010', 'S005', '17:00:00', '19:30:00');

INSERT INTO Funcion VALUES
('F001', 'PEL001', 'H001'),
('F002', 'PEL002', 'H002'),
('F003', 'PEL003', 'H003'),
('F004', 'PEL004', 'H004'),
('F005', 'PEL005', 'H005'),
('F006', 'PEL006', 'H006'),
('F007', 'PEL007', 'H007'),
('F008', 'PEL008', 'H008'),
('F009', 'PEL009', 'H009'),
('F010', 'PEL010', 'H010');

INSERT INTO Comprobante_Pago VALUES
('CP001', 'Efectivo', '001', '12345'),
('CP002', 'Tarjeta', '002', '54321'),
('CP003', 'Efectivo', '003', '67890'),
('CP004', 'Tarjeta', '004', '98765'),
('CP005', 'Efectivo', '005', '43210'),
('CP006', 'Tarjeta', '006', '56789'),
('CP007', 'Efectivo', '007', '87654'),
('CP008', 'Tarjeta', '008', '98701'),
('CP009', 'Efectivo', '009', '10987'),
('CP010', 'Tarjeta', '010', '21098');

INSERT INTO Venta VALUES
('V001', 'CL001', 'C001', 'E001', 'CP001', '2024-01-04', '18:30:00'),
('V002', 'CL002', 'C002', 'E002', 'CP002', '2024-01-05', '19:15:00'),
('V003', 'CL003', 'C003', 'E003', 'CP003', '2024-01-06', '20:00:00'),
('V004', 'CL004', 'C004', 'E004', 'CP004', '2024-01-07', '21:30:00'),
('V005', 'CL005', 'C005', 'E005', 'CP005', '2024-01-08', '22:45:00'),
('V006', 'CL006', 'C006', 'E006', 'CP006', '2024-01-09', '23:15:00'),
('V007', 'CL007', 'C007', 'E007', 'CP007', '2024-01-10', '15:45:00'),
('V008', 'CL008', 'C008', 'E008', 'CP008', '2024-01-11', '16:30:00'),
('V009', 'CL009', 'C009', 'E009', 'CP009', '2024-01-12', '17:00:00'),
('V010', 'CL010', 'C010', 'E010', 'CP010', '2024-01-13', '18:00:00');

INSERT INTO Detalle_Venta VALUES
('DV001', 'V001', 'P001', 2, 10.00, 20.00),
('DV002', 'V001', 'P002', 1, 3.50, 3.50),
('DV003', 'V002', 'P003', 3, 19.50, 19.50),
('DV004', 'V002', 'P004', 1, 2.00, 2.00),
('DV005', 'V003', 'P005', 2, 8.00, 16.00),
('DV006', 'V003', 'P006', 1, 1.50, 1.50),
('DV007', 'V004', 'P007', 2, 14.00, 28.00),
('DV008', 'V004', 'P008', 1, 1.00, 1.00),
('DV009', 'V005', 'P009', 3, 1.50, 4.50),
('DV010', 'V005', 'P010', 2, 9.00, 18.00);

INSERT INTO Boleto VALUES
('B001', 'F001', 'S001', 8.00, '2024-01-04', '14:30:00', 8.00),
('B002', 'F002', 'S002', 10.00, '2024-01-05', '14:45:00', 10.00),
('B003', 'F003', 'S003', 12.00, '2024-01-06', '15:30:00', 12.00),
('B004', 'F004', 'S004', 9.00, '2024-01-07', '16:15:00', 9.00),
('B005', 'F005', 'S005', 15.00, '2024-01-08', '17:00:00', 15.00),
('B006', 'F006', 'S006', 7.50, '2024-01-09', '18:30:00', 7.50),
('B007', 'F007', 'S007', 11.00, '2024-01-10', '19:45:00', 11.00),
('B008', 'F008', 'S008', 6.00, '2024-01-11', '20:15:00', 6.00),
('B009', 'F009', 'S009', 13.50, '2024-01-12', '21:00:00', 13.50),
('B010', 'F010', 'S010', 8.50, '2024-01-13', '22:00:00', 8.50);