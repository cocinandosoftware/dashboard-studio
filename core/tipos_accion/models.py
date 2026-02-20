from django.db import models


class TipoAccion(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tipo de acción'
        verbose_name_plural = 'Tipos de acción'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
