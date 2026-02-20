from django.db import models


class Producto(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    coste = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['referencia']

    def __str__(self):
        return f'{self.referencia} - {self.descripcion}'
