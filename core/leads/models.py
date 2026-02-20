from django.db import models

from core.clientes.models import Cliente


class Lead(models.Model):
    class Estado(models.TextChoices):
        NUEVO = 'NUEVO', 'Nuevo'
        CONTACTADO = 'CONTACTADO', 'Contactado'
        CONVERTIDO = 'CONVERTIDO', 'Convertido'
        DESCARTADO = 'DESCARTADO', 'Descartado'

    nombre = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    empresa = models.CharField(max_length=150, blank=True)
    origen = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.NUEVO)
    cliente_convertido = models.OneToOneField(
        Cliente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lead_origen',
    )
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-created_at', 'nombre', 'apellidos']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'.strip()

    def save(self, *args, **kwargs):
        if self.cliente_convertido and self.estado != self.Estado.CONVERTIDO:
            self.estado = self.Estado.CONVERTIDO
        super().save(*args, **kwargs)
