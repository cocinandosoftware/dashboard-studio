# Dashboard Studio

Proyecto Django vacío listo para empezar a desarrollar.

## Estructura del Proyecto

```
dashboard-studio/
├── dashboard_studio/     # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py      # Configuración del proyecto
│   ├── urls.py          # Rutas principales
│   └── wsgi.py
├── dashboard_venv/       # Entorno virtual (no incluido en git)
├── db.sqlite3           # Base de datos SQLite (no incluida en git)
├── manage.py            # Herramienta de línea de comandos de Django
└── requirements.txt     # Dependencias del proyecto
```

## Configuración Inicial

### 1. Activar el entorno virtual

```bash
source venv_dashboard/bin/activate
```

### 2. Instalar dependencias (si es necesario)

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en http://127.0.0.1:8000/

## Comandos Útiles

### Crear una nueva aplicación Django

```bash
python manage.py startapp nombre_app
```

### Crear migraciones

```bash
python manage.py makemigrations
```

### Aplicar migraciones

```bash
python manage.py migrate
```

### Cargar configuración inicial del CRM

```bash
python manage.py bootstrap_crm
```

### Crear un superusuario

```bash
python manage.py createsuperuser
```

### Acceder al panel de administración

Primero crea un superusuario y luego accede a http://127.0.0.1:8000/admin/

## Tecnologías

- Python 3
- Django 4.2.28

## Arranque rápido recomendado

```bash
source venv_dashboard/bin/activate
python manage.py migrate
python manage.py bootstrap_crm
python manage.py createsuperuser
python manage.py runserver 8080
```
