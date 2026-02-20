"""Configuración de URLs para el contexto CRM."""
from django.urls import path
from context.crm.views.crm_views import access_view, register_view

app_name = 'crm'

urlpatterns = [
    path('acceso/', access_view, name='access'),
    path('registro/', register_view, name='register'),
]
