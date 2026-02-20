from django.contrib import admin

from core.cartera_comercial.models import CarteraComercial


@admin.register(CarteraComercial)
class CarteraComercialAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'comercial', 'fecha_asignacion', 'activo')
    list_filter = ('activo', 'fecha_asignacion', 'comercial')
    search_fields = (
        'cliente__nombre',
        'cliente__apellidos',
        'comercial__codigo_comercial',
        'comercial__nombre',
        'comercial__apellidos',
    )
