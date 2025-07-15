# 👗 Minimarket La Favorita - Sistema de Ventas

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v3.1.1-green.svg)
![SQL Server](https://img.shields.io/badge/sql%20server-express-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📖 Descripción

**Minimarket La Favorita** es un sistema de gestión de ventas desarrollado en Python Flask para tiendas de ropa. Permite registrar ventas, gestionar inventario básico y generar reportes de ventas de manera sencilla e intuitiva.

## ✨ Características

- 🛍️ **Registro de Ventas**: Registra ventas con cliente, prenda, talla, cantidad y precio
- 📊 **Dashboard de Ventas**: Visualiza todas las ventas registradas
- ✏️ **Edición de Ventas**: Modifica ventas existentes
- 🗑️ **Eliminación de Ventas**: Elimina ventas con confirmación
- � **Estadísticas Básicas**: Muestra total de ventas e ingresos
- 🔐 **Sistema de Login**: Acceso seguro con usuario y contraseña
- � **Diseño Responsive**: Funciona en desktop y móvil

## 📋 Catálogo de Productos

El sistema incluye las siguientes prendas:
- 👔 Camisas
- 👖 Pantalones
- � Vestidos y Faldas
- 👚 Blusas y Camisetas
- 🧥 Chaquetas
- 👠 Zapatos y Zapatillas
- 👜 Carteras y Accesorios

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.13+ con Flask
- **Base de datos:** SQL Server (SQL Server Express)
- **Frontend:** HTML5, CSS3, JavaScript
- **Conexión BD:** pyodbc
- **Autenticación:** Flask Sessions

## 📁 Estructura del Proyecto

```
minimarket-la-favorita/
├── app.py                 # Aplicación principal Flask
├── setup_database.sql     # Script para crear la base de datos
├── README.md             # Documentación del proyecto
├── Templates/            # Plantillas HTML
│   ├── Formulario.html   # Página principal con formulario
│   └── login.html        # Página de login
└── static/              # Archivos estáticos
    └── img/             # Imágenes del proyecto
        └── logo-minimarket.svg
```

## 🚀 Instalación y Configuración

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:
- 🐍 **Python 3.13+**
- 💾 **SQL Server** (SQL Server Express recomendado)
- 📦 **pip** (gestor de paquetes de Python)

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/diego-reynaga/botica-unajma.git
cd botica-unajma
```

### Paso 2: Instalar dependencias

```bash
# Instalar Flask y pyodbc
pip install flask pyodbc

# O usar el archivo requirements.txt (si lo tienes)
pip install -r requirements.txt
```

### Paso 3: Configurar SQL Server

1. **Iniciar SQL Server:**
   - Asegúrate de que SQL Server Express esté ejecutándose
   - Verifica con: `Get-Service -Name "*SQL*"`

2. **Crear la base de datos:**
   ```bash
   # Ejecutar el script SQL
   sqlcmd -S "TU_SERVIDOR\SQLEXPRESS" -E -i setup_database.sql
   ```

3. **Configurar la conexión:**
   - Abre `app.py`
   - Modifica la línea de conexión con tu nombre de servidor:
   ```python
   conn = pyodbc.connect(
       'DRIVER={ODBC Driver 17 for SQL Server};'
       'SERVER=TU_SERVIDOR\\SQLEXPRESS;'  # Cambia por tu servidor
       'DATABASE=MinimartLaFavorita;'
       'Trusted_Connection=yes;'
   )
   ```

### Paso 4: Obtener el nombre de tu servidor

```bash
# En Windows PowerShell
sqlcmd -L

# Busca algo como: DESKTOP-XXXXX\SQLEXPRESS
```

### Paso 5: Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: **http://127.0.0.1:5000**

## 🔐 Credenciales de Acceso

- **Usuario:** `admin`
- **Contraseña:** `1234`

## 🗄️ Estructura de la Base de Datos

### Tabla: `Ventas`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INT IDENTITY | Clave primaria (auto-incremento) |
| `cliente` | NVARCHAR(100) | Nombre del cliente |
| `prenda` | NVARCHAR(50) | Tipo de prenda |
| `talla` | NVARCHAR(10) | Talla de la prenda |
| `cantidad` | INT | Cantidad vendida |
| `precio` | DECIMAL(10,2) | Precio unitario |
| `fecha` | DATETIME | Fecha de venta (automática) |

## 🎯 Funcionalidades

### 1. **Sistema de Autenticación**
- Login seguro con sesiones
- Redirección automática si no está autenticado
- Logout con limpieza de sesión

### 2. **Gestión de Ventas**
- ✅ **Crear:** Formulario para nuevas ventas
- 📖 **Leer:** Lista completa de ventas
- ✏️ **Actualizar:** Editar ventas existentes
- 🗑️ **Eliminar:** Borrar ventas

### 3. **Interfaz de Usuario**
- Diseño responsive
- Mensajes de confirmación
- Interfaz intuitiva
- Estadísticas de ventas

## 🔧 Solución de Problemas

### Problema: "No se puede conectar a SQL Server"

**Solución:**
1. Verifica que SQL Server esté ejecutándose:
   ```bash
   Get-Service -Name "*SQL*"
   ```

2. Comprueba el nombre del servidor:
   ```bash
   sqlcmd -L
   ```

3. Actualiza la conexión en `app.py` con el nombre correcto

### Problema: "Base de datos no encontrada"

**Solución:**
1. Ejecuta el script de configuración:
   ```bash
   sqlcmd -S "TU_SERVIDOR\SQLEXPRESS" -E -i setup_database.sql
   ```

### Problema: "Módulo no encontrado"

**Solución:**
```bash
pip install flask pyodbc
```

## 📱 Capturas de Pantalla

### Login
- Pantalla de autenticación con diseño moderno
- Validación de credenciales

### Dashboard Principal
- Formulario de registro de ventas
- Lista de ventas con opciones de edición/eliminación
- Diseño responsive
- Estadísticas de ventas

## 🚀 Despliegue

### Desarrollo Local
```bash
python app.py
```

### Producción
Para producción, considera usar:
- **Gunicorn** como servidor WSGI
- **Nginx** como proxy reverso
- **Railway, Render, o Heroku** para hosting en la nube

## 📝 Datos de Ejemplo

El script `setup_database.sql` incluye datos de ejemplo:
- María González - Vestido M (1 unidad - S/ 45.50)
- Carlos Ruiz - Camisa L (2 unidades - S/ 35.00)
- María García - Ibuprofeno (1 unidad - S/ 12.00)
- Carlos López - Vitamina C (3 unidades - S/ 8.75)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Diego Reynaga**
- GitHub: [@diego-reynaga](https://github.com/diego-reynaga)
- Proyecto: [botica-unajma](https://github.com/diego-reynaga/botica-unajma)

## 🏥 Institución

**Universidad Nacional José María Arguedas (UNAJMA)**
- Escuela Profesional de Ingeniería de Sistemas

## 📞 Soporte

Si tienes problemas o preguntas:
1. Revisa la sección de **Solución de Problemas**
2. Abre un [Issue](https://github.com/diego-reynaga/botica-unajma/issues)
3. Contacta al autor

---

⭐ **¡Si te gusta este proyecto, dale una estrella en GitHub!**

⭐ **¡Si te gusta este proyecto, dale una estrella!** ⭐
