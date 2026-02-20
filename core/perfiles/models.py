from django.db import models


class Perfil(models.Model):
    class Tipo(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        GERENTE = 'GERENTE', 'Gerente'
        COMERCIAL = 'COMERCIAL', 'Comercial'

    nombre = models.CharField(max_length=80, unique=True)
    tipo = models.CharField(max_length=20, choices=Tipo.choices, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
