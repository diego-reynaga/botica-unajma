# Configuración de la aplicación Flask
import os

class Config:
    """Configuración base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_segura'
    
class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    # Configuración de SQL Server local
    DATABASE_CONFIG = {
        'DRIVER': '{ODBC Driver 17 for SQL Server}',
        'SERVER': 'localhost\\SQLEXPRESS',  # Cambiar por tu servidor
        'DATABASE': 'MinimartLaFavorita',
        'TRUSTED_CONNECTION': 'yes'
    }

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    # Configuración de base de datos en producción
    DATABASE_CONFIG = {
        'DRIVER': '{ODBC Driver 17 for SQL Server}',
        'SERVER': os.environ.get('DB_SERVER'),
        'DATABASE': os.environ.get('DB_NAME'),
        'UID': os.environ.get('DB_USER'),
        'PWD': os.environ.get('DB_PASSWORD')
    }

# Configuración por defecto
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
