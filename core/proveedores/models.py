from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=30, unique=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'
