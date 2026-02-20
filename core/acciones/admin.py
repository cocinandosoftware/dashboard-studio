from django.contrib import admin

from core.acciones.models import Accion


@admin.register(Accion)
class AccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'tipo_accion', 'comercial', 'cliente', 'lead')
    list_filter = ('fecha', 'tipo_accion', 'comercial')
    search_fields = (
        'detalle',
        'cliente__nombre',
        'cliente__apellidos',
        'lead__nombre',
        'lead__apellidos',
        'comercial__codigo_comercial',
        'comercial__nombre',
        'comercial__apellidos',
    )
