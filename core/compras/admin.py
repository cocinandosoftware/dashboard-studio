from django.contrib import admin

from core.compras.models import Compra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'producto', 'proveedor', 'cantidad', 'coste_unitario')
    list_filter = ('fecha', 'proveedor', 'producto')
    search_fields = ('producto__referencia', 'producto__descripcion', 'proveedor__codigo', 'proveedor__nombre')
