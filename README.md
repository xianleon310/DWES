# Proyecto Web con PHP, Python y Django

## Descripción

Este proyecto es una aplicación web híbrida que combina la potencia de Django como framework principal, con componentes en PHP para funcionalidades legacy y scripts de Python para procesamiento de datos.

## Tecnologías Utilizadas

- **Django 5.0+** - Framework web principal (Python)
- **PHP 8.2+** - Módulos legacy y servicios auxiliares
- **Python 3.11+** - Scripts de procesamiento y backend
- **MySQL/PostgreSQL** - Base de datos
- **Nginx/Apache** - Servidor web
- **Redis** - Cache y gestión de sesiones

## Estructura del Proyecto
```
proyecto/
├── django_app/              # Aplicación Django principal
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   ├── apps/
│   │   ├── usuarios/
│   │   ├── productos/
│   │   └── api/
│   └── templates/
├── php_modules/             # Módulos PHP
│   ├── legacy/
│   ├── api/
│   └── config.php
├── python_scripts/          # Scripts Python auxiliares
│   ├── data_processing/
│   ├── migrations/
│   └── utils/
├── static/                  # Archivos estáticos
├── media/                   # Archivos multimedia
├── requirements.txt         # Dependencias Python
├── composer.json           # Dependencias PHP
└── README.md
```

## Instalación

### Requisitos Previos

- Python 3.11 o superior
- PHP 8.2 o superior
- Composer
- pip y virtualenv
- MySQL/PostgreSQL
- Nginx o Apache

### Configurar Entorno Virtual de Python
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Instalar Dependencias PHP
```bash
cd php_modules
composer install
cd ..
```

### Configurar Base de Datos
```bash
# Crear base de datos
mysql -u root -p
CREATE DATABASE nombre_proyecto CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Ejecutar migraciones Django
python django_app/manage.py migrate
```

### Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:
```env
# Django
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de datos
DB_NAME=nombre_proyecto
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=3306

# PHP
PHP_API_KEY=tu-api-key-php
PHP_BASE_URL=http://localhost:8080

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
```

### Crear Superusuario Django
```bash
python django_app/manage.py createsuperuser
```

## Ejecución

### Desarrollo

**Servidor Django:**
```bash
python django_app/manage.py runserver
```

**Servidor PHP (usando el servidor integrado):**
```bash
cd php_modules
php -S localhost:8080
```

**Scripts Python:**
```bash
python python_scripts/nombre_script.py
```

### Producción

Para producción, se recomienda usar:
- **Gunicorn** o **uWSGI** para Django
- **PHP-FPM** con Nginx/Apache para PHP
- **Supervisor** para gestionar procesos
```bash
# Ejemplo con Gunicorn
gunicorn --bind 0.0.0.0:8000 django_app.wsgi:application
```

## Configuración

### Django Settings

Editar `django_app/settings.py` para configurar:
- Base de datos
- Aplicaciones instaladas
- Middleware
- Archivos estáticos

### PHP Configuration

Editar `php_modules/config.php` para:
- Conexiones a base de datos
- APIs externas
- Configuración de sesiones

## Arquitectura

### Flujo de Datos
```
Usuario → Nginx → Django (Frontend/API)
                    ↓
                  Python Scripts (Procesamiento)
                    ↓
                  PHP Modules (Legacy/Servicios)
                    ↓
                  Base de Datos
```

### Integración Django-PHP

La comunicación entre Django y PHP se realiza mediante:
- **API REST**: PHP expone endpoints consumidos por Django
- **Archivos compartidos**: Sistema de archivos común
- **Base de datos compartida**: Acceso a las mismas tablas

## Testing

### Tests Django
```bash
python django_app/manage.py test
```

### Tests PHP
```bash
cd php_modules
./vendor/bin/phpunit tests/
```

### Tests Python Scripts
```bash
pytest python_scripts/tests/
```

## API Documentation

### Endpoints Django

- `GET /api/usuarios/` - Listar usuarios
- `POST /api/usuarios/` - Crear usuario
- `GET /api/productos/` - Listar productos

### Endpoints PHP

- `GET /api/legacy/datos` - Obtener datos legacy
- `POST /api/legacy/procesar` - Procesar información

## Seguridad

- Las contraseñas se almacenan hasheadas con bcrypt
- CSRF protection habilitado en Django
- Validación de entrada en todos los endpoints
- HTTPS obligatorio en producción
- Rate limiting implementado

## Contribución

### Guía de Estilo

- **Python**: Seguir PEP 8
- **PHP**: Seguir PSR-12
- **JavaScript**: Usar ESLint

## Licencia

Este proyecto está bajo la Licencia MIT.
