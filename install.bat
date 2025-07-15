@echo off
echo ===============================================
echo    BOTICA UNAJMA - SCRIPT DE INSTALACION
echo ===============================================
echo.

echo 1. Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado o no esta en PATH
    echo Por favor instala Python 3.13+ desde https://python.org
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

echo 2. Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo [OK] Dependencias instaladas
echo.

echo 3. Verificando SQL Server...
sqlcmd -L >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] SQL Server no encontrado o no accesible
    echo Por favor asegurate de que SQL Server Express este instalado e iniciado
    echo.
)

echo 4. Configurando base de datos...
echo Por favor ejecuta manualmente:
echo sqlcmd -S "TU_SERVIDOR\SQLEXPRESS" -E -i setup_database.sql
echo.

echo 5. Configuracion del servidor...
echo Edita app.py y cambia el SERVER por el nombre de tu servidor SQL
echo.

echo ===============================================
echo    INSTALACION COMPLETADA
echo ===============================================
echo.
echo Para ejecutar la aplicacion:
echo   python app.py
echo.
echo Luego ve a: http://127.0.0.1:5000
echo Usuario: admin  |  Contraseña: 1234
echo.
pause
