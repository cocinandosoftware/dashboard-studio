from django.contrib import admin

from core.leads.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellidos', 'empresa', 'estado', 'cliente_convertido', 'activo')
    list_filter = ('estado', 'activo')
    search_fields = ('nombre', 'apellidos', 'email', 'telefono', 'empresa', 'origen')
