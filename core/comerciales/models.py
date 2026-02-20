from django.contrib.auth.models import User
from django.db import models

from core.perfiles.models import Perfil


class Comercial(models.Model):
    nombre = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=150, blank=True)
    codigo_comercial = models.CharField(max_length=30, unique=True)
    usuario = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='comercial',
    )
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        related_name='comerciales',
    )
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comercial'
        verbose_name_plural = 'Comerciales'
        ordering = ['nombre', 'apellidos']

    def __str__(self):
        return f'{self.codigo_comercial} - {self.nombre} {self.apellidos}'.strip()
