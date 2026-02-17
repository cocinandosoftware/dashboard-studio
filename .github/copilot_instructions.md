# Instrucciones de Desarrollo - Dashboard Studio

## 🎯 Principios Fundamentales

- **NUNCA** actualices el README.md cuando proporciones ayuda o implementes cambios
- Sigue estrictamente la arquitectura de tres capas definida: Core → Library → Context
- Mantén la separación de responsabilidades en todo momento
- Escribe código limpio, idiomático y bien documentado en español
- NO queremos utilizar formularios de Django

## 📁 Arquitectura del Proyecto

### Estructura de Carpetas

```
dashboard_studio/
├── core/                    # Capa de datos y lógica de negocio
│   ├── models/             # Modelos de Django (un archivo por modelo)
│   ├── admin/              # Configuración del admin de Django
│   └── migrations/         # Migraciones de base de datos
├── library/                # Capa de comunicación y utilidades
│   ├── services/           # Servicios de negocio
│   ├── serializers/        # Serialización de datos
│   ├── validators/         # Validadores personalizados
│   └── utils/              # Funciones auxiliares
├── context/                # Capa de presentación (contextos separados)
│   ├── web/               # Contexto web público
│   │   ├── views/         # Vistas del contexto web
│   │   └── urls/          # URLs del contexto web
│   ├── admin/             # Contexto administrativo (ejemplo)
│   │   ├── views/
│   │   └── urls/
│   └── api/               # Contexto API REST (ejemplo)
│       ├── views/
│       └── urls/
├── templates/              # Templates HTML (raíz del proyecto)
│   ├── web/               # Templates del contexto web
│   ├── admin/             # Templates del contexto admin
│   └── shared/            # Templates compartidos entre contextos
└── static/                # Archivos estáticos (CSS, JS, imágenes)
    ├── web/               # Assets específicos del contexto web
    ├── admin/             # Assets específicos del contexto admin
    └── shared/            # Assets compartidos
```

## 🏗️ Descripción de Capas

### 1. **Core** - Capa de Datos
- **Propósito**: Definir modelos de base de datos y configuración del admin
- **Contenido**:
  - `models/`: Un archivo por modelo (ej: `user.py`, `dashboard.py`)
  - `admin/`: Configuración del panel de administración
- **Reglas**:
  - Los modelos NO deben importar nada de `context`
  - Pueden usar funciones de `library` si es necesario
  - Incluir docstrings en español para cada modelo y campo importante
  - Usar `related_name` descriptivos en relaciones

### 2. **Library** - Capa de Comunicación
- **Propósito**: Funciones intermediarias entre Core y Context
- **Contenido**:
  - `services/`: Lógica de negocio compleja (ej: `dashboard_service.py`)
  - `serializers/`: Transformación de datos (si usas DRF)
  - `validators/`: Validaciones personalizadas
  - `utils/`: Funciones auxiliares reutilizables
- **Reglas**:
  - Puede importar de `core`
  - NO debe importar de `context`
  - Funciones puras cuando sea posible
  - Manejo de errores consistente

### 3. **Context** - Capa de Presentación
- **Propósito**: Manejar peticiones HTTP y renderizar respuestas
- **Organización**: Cada contexto en su propia carpeta (web, admin, api, etc.)
- **Contenido de cada contexto**:
  - `views/`: Vistas basadas en clases o funciones del contexto
  - `urls/`: Configuración de rutas del contexto
- **Templates**: Se almacenan en `templates/` en la raíz del proyecto
  - Organizados por contexto: `templates/web/`, `templates/admin/`, etc.
  - Templates compartidos en `templates/shared/`
- **Reglas**:
  - Cada contexto es independiente (web pública, administración, API, etc.)
  - Puede importar de `core` y `library`
  - Las vistas deben ser delgadas, la lógica va en `library`
  - Un archivo de URLs por contexto
  - **NO usamos formularios de Django** (manejo manual de datos)
  - Los templates se referencian con el nombre del contexto: `'web/pagina.html'`

## �️ Organización de Contextos

### ¿Qué es un Contexto?
Un **contexto** representa un área funcional completa y separada de la aplicación. Cada contexto debe ser independiente y tener su propio propósito claro.

### Ejemplos de Contextos:
- **`web`**: Sitio web público para usuarios finales
- **`admin`**: Panel de administración interno
- **`api`**: API REST para aplicaciones móviles o terceros
- **`dashboard`**: Dashboard interactivo para usuarios registrados
- **`auth`**: Sistema de autenticación y registro

### Estructura de un Contexto:
```
context/
└── nombre_contexto/
    ├── __init__.py
    ├── views/              # Solo vistas de este contexto
    │   ├── __init__.py
    │   ├── home_views.py
    │   └── detail_views.py
    └── urls/               # Solo URLs de este contexto
        ├── __init__.py
        └── main_urls.py

templates/
└── nombre_contexto/        # Templates específicos del contexto
    ├── base.html          # Base template del contexto
    ├── home.html
    └── detail.html

static/
└── nombre_contexto/        # Assets específicos del contexto
    ├── css/
    │   └── styles.css
    └── js/
        └── app.js
```

### Reglas para Contextos:
1. **Un contexto = Una carpeta** dentro de `context/`
2. **Solo `views/` y `urls/`** dentro de cada contexto
3. **Templates en la raíz** del proyecto dentro de `templates/contexto/`
4. **Sin dependencias entre contextos**: Un contexto NO debe importar de otro contexto
5. **Compartir mediante Library**: Si dos contextos necesitan la misma lógica, va en `library/`
6. **Nombres descriptivos**: Usa nombres que indiquen claramente el propósito del contexto

### Registrar un Contexto:
```python
# dashboard_studio/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('context.web.urls.main_urls')),        # Web pública en /
    path('panel/', include('context.admin.urls.main_urls')), # Admin en /panel/
    path('api/', include('context.api.urls.main_urls')),     # API en /api/
]
```

## �📝 Convenciones de Código

### Nomenclatura
- **Archivos**: snake_case (ej: `dashboard_view.py`)
- **Clases**: PascalCase (ej: `DashboardModel`)
- **Funciones/Variables**: snake_case (ej: `get_user_dashboards`)
- **Constantes**: UPPER_SNAKE_CASE (ej: `MAX_DASHBOARDS`)

### Organización de Imports
```python
# 1. Librerías estándar de Python
import os
from datetime import datetime

# 2. Librerías de terceros
from django.db import models
from django.shortcuts import render

# 3. Imports del proyecto (Core → Library → Context)
from core.models.user import User
from core.models.dashboard import Dashboard
from library.services.dashboard_service import DashboardService
from library.utils.date_helpers import format_date

# ❌ NUNCA importar entre contextos
# from context.admin.views.admin_views import some_function  # ¡MAL!
```

### Documentación
- Docstrings en español para clases y funciones públicas
- Comentarios inline solo cuando la lógica no sea obvia
- Type hints en funciones cuando sea apropiado

## 🔄 Flujo de Trabajo

### Para implementar una nueva funcionalidad:

1. **Core**: Define el modelo si es necesario
   ```python
   # core/models/dashboard.py
   from django.db import models
   
   class Dashboard(models.Model):
       """Modelo para representar un dashboard del usuario."""
       nombre = models.CharField(max_length=200)
       # ... más campos
   ```

2. **Library**: Crea la lógica de negocio
   ```python
   # library/services/dashboard_service.py
   def crear_dashboard(usuario, datos):
       """Crea un nuevo dashboard para el usuario especificado."""
       # Lógica de creación
   ```

3. **Context**: Implementa la vista en el contexto apropiado
   ```python
   # context/web/views/dashboard_views.py
   from library.services.dashboard_service import crear_dashboard
   
   def crear_dashboard_view(request):
       """Vista para crear un dashboard."""
       context = {'titulo': 'Crear Dashboard'}
       return render(request, 'web/dashboard_form.html', context)
   ```

4. **URLs**: Configura las rutas del contexto
   ```python
   # context/web/urls/dashboard_urls.py
   from django.urls import path
   from context.web.views.dashboard_views import crear_dashboard_view
   
   urlpatterns = [
       path('crear/', crear_dashboard_view, name='crear_dashboard'),
   ]
   ```

5. **Template**: Crea el template en la carpeta del contexto
   ```html
   <!-- templates/web/dashboard_form.html -->
   <!DOCTYPE html>
   <html>
   <head><title>{{ titulo }}</title></head>
   <body>
       <!-- Contenido del formulario -->
   </body>
   </html>
   ```

### Para crear un nuevo contexto:

1. Crear la carpeta del contexto: `context/nombre_contexto/`
2. Crear subcarpetas: `views/` y `urls/`
3. Crear archivos `__init__.py` en cada carpeta
4. Crear carpeta para templates: `templates/nombre_contexto/`
5. Registrar las URLs en el archivo principal `dashboard_studio/urls.py`

**Ejemplo - Nuevo contexto "admin":**
```
context/
└── admin/
    ├── __init__.py
    ├── views/
    │   ├── __init__.py
    │   └── admin_views.py
    └── urls/
        ├── __init__.py
        └── admin_urls.py

templates/
└── admin/
    └── dashboard.html
```

## ⚠️ Restricciones

### Prohibiciones Estrictas:
- **🚫 NO** actualices README.md automáticamente
- **🚫 NO** uses formularios de Django (manejo manual de request.POST)
- **🚫 NO** mezcles lógica de negocio en las vistas
- **🚫 NO** pongas imports circulares entre capas
- **🚫 NO** importes de un contexto a otro (context/web → context/admin ❌)
- **🚫 NO** uses imports relativos entre diferentes capas
- **🚫 NO** pongas templates dentro de las carpetas de contexto (van en `templates/`)
- **🚫 NO** mezcles código de diferentes contextos en el mismo archivo

### Buenas Prácticas Obligatorias:
- **✅ SÍ** mantén funciones pequeñas y enfocadas
- **✅ SÍ** cada contexto es completamente independiente
- **✅ SÍ** usa Library para compartir lógica entre contextos
- **✅ SÍ** escribe tests para servicios críticos
- **✅ SÍ** maneja excepciones apropiadamente
- **✅ SÍ** usa nombres descriptivos para contextos y archivos
- **✅ SÍ** organiza templates por contexto en `templates/nombre_contexto/`
- **✅ SÍ** organiza static files por contexto en `static/nombre_contexto/`

## 🧪 Testing

- Tests unitarios en `tests/` dentro de cada capa
- Nombrar archivos de test: `test_*.py`
- Usar fixtures para datos de prueba reutilizables

## 🚀 Mejores Prácticas

### Por Capa:

1. **Modelos (Core)**: 
   - Usa `__str__()` descriptivos
   - Añade `Meta` con `ordering` y `verbose_name`
   - Incluye docstrings en español
   - Usa `related_name` claros y descriptivos

2. **Servicios (Library)**: 
   - Una función = una responsabilidad
   - Funciones puras cuando sea posible
   - Manejo explícito de errores con try/except
   - Documentar parámetros y returns

3. **Vistas (Context)**: 
   - Delega toda la lógica a servicios
   - Solo maneja HTTP (request/response)
   - Valida datos del request antes de procesarlos
   - Retorna contextos claros y mínimos

4. **Templates**: 
   - Un template base por contexto: `templates/contexto/base.html`
   - Hereda del base: `{% extends 'web/base.html' %}`
   - Usa nombres descriptivos: `dashboard_list.html`, no `list.html`
   - Templates compartidos en `templates/shared/`

5. **URLs**: 
   - Define `app_name` en cada archivo de URLs
   - Usa nombres descriptivos con namespaces: `{% url 'web:home' %}`
   - Agrupa rutas relacionadas en el mismo archivo
   - Un archivo `main_urls.py` por contexto como punto de entrada

### General:

6. **Configuración**: Usa variables de entorno para settings sensibles
7. **Seguridad**: Valida siempre los inputs del usuario
8. **Nomenclatura**: Consistente y en español
9. **Documentación**: Docstrings en español para todo código público
10. **Independencia**: Cada contexto debe poder funcionar sin los demás

## 📚 Ejemplos Prácticos

### Referenciar Templates desde Vistas

```python
# context/web/views/home_views.py
from django.shortcuts import render

def home_view(request):
    """Vista principal del contexto web."""
    context = {'titulo': 'Inicio'}
    # ✅ CORRECTO: Especificar contexto/archivo.html
    return render(request, 'web/home.html', context)
    
    # ❌ INCORRECTO: Sin especificar contexto
    # return render(request, 'home.html', context)
```

### Configuración de URLs por Contexto

```python
# context/web/urls/main_urls.py
from django.urls import path, include
from context.web.views.home_views import home_view

app_name = 'web'  # Namespace del contexto

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', include('context.web.urls.about_urls')),
]
```

```python
# dashboard_studio/urls.py (archivo principal)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('context.web.urls.main_urls')),  # Contexto web
    # path('panel/', include('context.admin.urls.main_urls')),  # Contexto admin
    # path('api/', include('context.api.urls.main_urls')),  # Contexto API
]
```

### Herencia de Templates

```html
<!-- templates/web/base.html - Template base del contexto web -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Dashboard Studio{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'web/css/styles.css' %}">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

```html
<!-- templates/web/home.html - Hereda del base del contexto -->
{% extends 'web/base.html' %}

{% block title %}{{ titulo }} - Dashboard Studio{% endblock %}

{% block content %}
    <h1>{{ titulo }}</h1>
    <p>Bienvenido al Dashboard Studio</p>
{% endblock %}
```

### Uso de Namespaces en Templates

```html
<!-- En cualquier template del contexto web -->
<nav>
    <a href="{% url 'web:home' %}">Inicio</a>
    <a href="{% url 'web:about' %}">Acerca de</a>
</nav>

<!-- ❌ INCORRECTO: Sin namespace -->
<!-- <a href="{% url 'home' %}">Inicio</a> -->
```

### Estructura Completa de un Contexto Real

```
context/
└── web/
    ├── __init__.py
    ├── views/
    │   ├── __init__.py
    │   ├── home_views.py       # Vistas de la página principal
    │   ├── about_views.py      # Vistas de "Acerca de"
    │   └── contact_views.py    # Vistas de contacto
    └── urls/
        ├── __init__.py
        ├── main_urls.py        # URLs principales del contexto
        ├── about_urls.py       # URLs de "Acerca de"
        └── contact_urls.py     # URLs de contacto

templates/
└── web/
    ├── base.html               # Template base del contexto
    ├── home.html               # Página principal
    ├── about.html              # Página "Acerca de"
    ├── contact.html            # Página de contacto
    └── partials/               # Componentes reutilizables
        ├── header.html
        └── footer.html

static/
└── web/
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── app.js
    └── images/
        └── logo.png
```

### Manejo de Datos sin Formularios Django

```python
# context/web/views/contact_views.py
from django.shortcuts import render, redirect
from library.services.contact_service import enviar_mensaje_contacto

def contact_view(request):
    """Vista para el formulario de contacto."""
    if request.method == 'POST':
        # ✅ CORRECTO: Manejo manual de request.POST
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()
        
        # Validar y procesar mediante servicio
        resultado = enviar_mensaje_contacto(nombre, email, mensaje)
        
        if resultado['exito']:
            return redirect('web:contact_success')
        else:
            context = {
                'error': resultado['error'],
                'nombre': nombre,
                'email': email,
            }
            return render(request, 'web/contact.html', context)
    
    # GET request
    return render(request, 'web/contact.html', {})
```

---

**Recuerda**: Sigue siempre esta arquitectura. La separación de contextos mantiene el código organizado, escalable y fácil de mantener.
