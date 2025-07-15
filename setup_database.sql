-- Script para configurar la base de datos del Minimarket La Favorita
-- Ejecutar este script en SQL Server Management Studio

-- Crear la base de datos
CREATE DATABASE MinimartLaFavorita;
GO

-- Usar la base de datos
USE MinimartLaFavorita;
GO

-- Crear la tabla Ventas
CREATE TABLE Ventas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente NVARCHAR(100) NOT NULL,
    prenda NVARCHAR(50) NOT NULL,
    talla NVARCHAR(10) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    fecha DATETIME DEFAULT GETDATE()
);
GO

-- Insertar algunos datos de ejemplo
INSERT INTO Ventas (cliente, prenda, talla, cantidad, precio) VALUES
('María González', 'Vestido', 'M', 1, 45.50),
('Carlos Ruiz', 'Camisa', 'L', 2, 35.00),
('Ana López', 'Pantalón', 'S', 1, 55.75),
('José Martínez', 'Camiseta', 'XL', 3, 25.00),
('Lucía Fernández', 'Falda', 'M', 1, 40.00),
('Roberto Silva', 'Chaqueta', 'L', 1, 85.99),
('Patricia Morales', 'Blusa', 'S', 2, 32.50),
('Miguel Torres', 'Zapatos', '42', 1, 120.00);
GO

-- Verificar que los datos se insertaron correctamente
SELECT * FROM Ventas;
GO

-- Crear vista para estadísticas
CREATE VIEW VentasEstadisticas AS
SELECT 
    COUNT(*) as TotalVentas,
    SUM(cantidad * precio) as IngresoTotal,
    AVG(precio) as PrecioPromedio,
    prenda,
    COUNT(*) as VentasPorPrenda
FROM Ventas
GROUP BY prenda;
GO

-- Consultar estadísticas
SELECT * FROM VentasEstadisticas;
GO
