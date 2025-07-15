-- Script para configurar la base de datos de la Botica
-- Ejecutar este script en SQL Server Management Studio

-- Crear la base de datos
CREATE DATABASE BoticaVentas;
GO

-- Usar la base de datos
USE BoticaVentas;
GO

-- Crear la tabla Pedidos
CREATE TABLE Pedidos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre_cliente NVARCHAR(100) NOT NULL,
    producto NVARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    fecha DATETIME DEFAULT GETDATE()
);
GO

-- Insertar algunos datos de ejemplo
INSERT INTO Pedidos (nombre_cliente, producto, cantidad, precio) VALUES
('Juan Pérez', 'Paracetamol', 2, 5.50),
('María García', 'Ibuprofeno', 1, 12.00),
('Carlos López', 'Vitamina C', 3, 8.75);
GO

-- Verificar que los datos se insertaron correctamente
SELECT * FROM Pedidos;
GO
