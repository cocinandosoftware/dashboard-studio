from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=30, blank=True)
    empresa = models.CharField(max_length=150, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    provincia = models.CharField(max_length=100, blank=True)
    localidad = models.CharField(max_length=120, blank=True)
    codigo_postal = models.CharField(max_length=12, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre', 'apellidos']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'.strip()
