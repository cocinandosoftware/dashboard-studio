"""Configuración de URLs para contextos públicos."""
from django.urls import path
from context.web.views.public_views import hello_world_view

app_name = 'public'

urlpatterns = [
    path('', hello_world_view, name='hello_world'),
]
