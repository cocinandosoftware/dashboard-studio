from django.db import models
from django.utils import timezone

from core.clientes.models import Cliente
from core.comerciales.models import Comercial


class CarteraComercial(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='carteras_comerciales',
    )
    comercial = models.ForeignKey(
        Comercial,
        on_delete=models.PROTECT,
        related_name='carteras_comerciales',
    )
    fecha_asignacion = models.DateField(default=timezone.now)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cartera comercial'
        verbose_name_plural = 'Carteras comerciales'
        ordering = ['cliente', 'comercial']
        constraints = [
            models.UniqueConstraint(
                fields=['cliente', 'comercial'],
                name='unique_cliente_comercial_asignado',
            )
        ]

    def __str__(self):
        return f'{self.cliente} ↔ {self.comercial}'
