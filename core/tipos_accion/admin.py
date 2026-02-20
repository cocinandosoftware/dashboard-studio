from django.contrib import admin

from core.tipos_accion.models import TipoAccion


@admin.register(TipoAccion)
class TipoAccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')
