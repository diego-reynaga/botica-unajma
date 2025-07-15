# 🏥 Botica UNAJMA - Sistema de Gestión de Pedidos

Un sistema web desarrollado en Flask para la gestión de pedidos de una botica/farmacia, diseñado para la Universidad Nacional José María Arguedas (UNAJMA).

## 📋 Descripción

Este proyecto es una aplicación web que permite:
- 🔐 Sistema de autenticación (login/logout)
- 📝 Registro de pedidos de productos farmacéuticos
- 👀 Visualización de todos los pedidos
- ✏️ Edición de pedidos existentes
- 🗑️ Eliminación de pedidos
- 📊 Interfaz intuitiva y responsive

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.13+ con Flask
- **Base de datos:** SQL Server (SQL Server Express)
- **Frontend:** HTML5, CSS3, JavaScript
- **Conexión BD:** pyodbc
- **Autenticación:** Flask Sessions

## 📁 Estructura del Proyecto

```
BOTICA/
├── app.py                 # Aplicación principal Flask
├── setup_database.sql     # Script para crear la base de datos
├── README.md             # Documentación del proyecto
├── Templates/            # Plantillas HTML
│   ├── Formulario.html   # Página principal con formulario
│   └── login.html        # Página de login
└── static/              # Archivos estáticos
    └── img/             # Imágenes del proyecto
        ├── FondodeBotica.jpg
        ├── LogoBotica.png
        ├── LOGOEPIS.png
        └── LogoUnajma.png
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
       'DATABASE=BoticaVentas;'
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

### Tabla: `Pedidos`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INT IDENTITY | Clave primaria (auto-incremento) |
| `nombre_cliente` | NVARCHAR(100) | Nombre del cliente |
| `producto` | NVARCHAR(100) | Nombre del producto |
| `cantidad` | INT | Cantidad del producto |
| `precio` | DECIMAL(10,2) | Precio unitario |
| `fecha` | DATETIME | Fecha de registro (automática) |

## 🎯 Funcionalidades

### 1. **Sistema de Autenticación**
- Login seguro con sesiones
- Redirección automática si no está autenticado
- Logout con limpieza de sesión

### 2. **Gestión de Pedidos**
- ✅ **Crear:** Formulario para nuevos pedidos
- 📖 **Leer:** Lista completa de pedidos
- ✏️ **Actualizar:** Editar pedidos existentes
- 🗑️ **Eliminar:** Borrar pedidos

### 3. **Interfaz de Usuario**
- Diseño responsive
- Mensajes de confirmación
- Interfaz intuitiva

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
- Formulario de registro de pedidos
- Lista de pedidos con opciones de edición/eliminación
- Diseño responsive

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
- Juan Pérez - Paracetamol (2 unidades - S/ 5.50)
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

⭐ **¡Si te gusta este proyecto, dale una estrella!** ⭐
