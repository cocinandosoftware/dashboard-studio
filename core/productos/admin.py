from django.contrib import admin

from core.productos.models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'referencia', 'descripcion', 'pvp', 'coste', 'stock_actual', 'activo')
    list_filter = ('activo',)
    search_fields = ('referencia', 'descripcion')
