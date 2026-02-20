from django.contrib import admin

from core.comerciales.models import Comercial


@admin.register(Comercial)
class ComercialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo_comercial',
        'nombre',
        'apellidos',
        'usuario',
        'perfil',
        'activo',
    )
    list_filter = ('activo', 'perfil')
    search_fields = (
        'codigo_comercial',
        'nombre',
        'apellidos',
        'usuario__username',
        'usuario__email',
        'perfil__nombre',
    )
