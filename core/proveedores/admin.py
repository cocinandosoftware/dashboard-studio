from django.contrib import admin

from core.proveedores.models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'activo')
    list_filter = ('activo',)
    search_fields = ('codigo', 'nombre')
