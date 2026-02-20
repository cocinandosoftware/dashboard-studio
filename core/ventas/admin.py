from django.contrib import admin

from core.ventas.models import Venta


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha',
        'cliente',
        'producto',
        'comercial',
        'unidades',
        'pvp',
        'descuento',
        'neto',
        'coste',
    )
    list_filter = ('fecha', 'comercial', 'producto', 'cliente')
    readonly_fields = ('articulo', 'neto', 'coste')
    search_fields = (
        'articulo',
        'cliente__nombre',
        'cliente__apellidos',
        'producto__referencia',
        'producto__descripcion',
        'comercial__codigo_comercial',
        'comercial__nombre',
        'comercial__apellidos',
    )
