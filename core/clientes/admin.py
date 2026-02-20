from django.contrib import admin

from core.clientes.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellidos',
        'email',
        'telefono',
        'empresa',
        'localidad',
        'provincia',
        'codigo_postal',
        'activo',
    )
    list_filter = ('activo',)
    search_fields = (
        'nombre',
        'apellidos',
        'email',
        'telefono',
        'empresa',
        'direccion',
        'localidad',
        'provincia',
        'codigo_postal',
        'pais',
    )
