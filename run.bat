@echo off
echo ===============================================
echo    MINIMARKET LA FAVORITA - INICIANDO SISTEMA
echo ===============================================
echo.

echo Verificando dependencias...
pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Flask no esta instalado
    echo Ejecuta primero: install.bat
    pause
    exit /b 1
)

echo [OK] Dependencias encontradas
echo.

echo Iniciando sistema de ventas...
echo.
echo ===============================================
echo    MINIMARKET LA FAVORITA - SISTEMA ACTIVO
echo ===============================================
echo.
echo URL: http://127.0.0.1:5000
echo Usuario: admin
echo Contraseña: 1234
echo.
echo Presiona Ctrl+C para detener el servidor
echo ===============================================
echo.

python app.py
