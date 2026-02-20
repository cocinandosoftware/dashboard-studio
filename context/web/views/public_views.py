"""Vista pública de Hello World."""
from django.shortcuts import render


def hello_world_view(request):
    """
    Vista pública que muestra un mensaje de bienvenida Hello World.
    
    Args:
        request: Objeto HttpRequest de Django
    
    Returns:
        HttpResponse con el template renderizado
    """
    context = {
        'titulo': 'Dashboard Studio',
        'mensaje': 'Hello World',
        'descripcion': 'Bienvenido al Dashboard Studio - Tu primer contexto web público'
    }
    return render(request, 'hello_world.html', context)
