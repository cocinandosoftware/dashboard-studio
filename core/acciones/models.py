from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from core.clientes.models import Cliente
from core.comerciales.models import Comercial
from core.leads.models import Lead
from core.tipos_accion.models import TipoAccion


class Accion(models.Model):
    comercial = models.ForeignKey(
        Comercial,
        on_delete=models.PROTECT,
        related_name='acciones',
    )
    tipo_accion = models.ForeignKey(
        TipoAccion,
        on_delete=models.PROTECT,
        related_name='acciones',
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='acciones',
    )
    lead = models.ForeignKey(
        Lead,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='acciones',
    )
    fecha = models.DateTimeField(default=timezone.now)
    detalle = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Acción'
        verbose_name_plural = 'Acciones'
        ordering = ['-fecha', '-id']

    def __str__(self):
        destino = self.cliente or self.lead
        return f'{self.tipo_accion} - {destino}'

    def clean(self):
        tiene_cliente = bool(self.cliente_id)
        tiene_lead = bool(self.lead_id)
        if tiene_cliente == tiene_lead:
            raise ValidationError('La acción debe estar asociada a un cliente o a un lead (solo uno).')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
