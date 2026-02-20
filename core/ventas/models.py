from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import models

from core.clientes.models import Cliente
from core.comerciales.models import Comercial
from core.productos.models import Producto


class Venta(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='ventas',
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='ventas',
    )
    comercial = models.ForeignKey(
        Comercial,
        on_delete=models.PROTECT,
        related_name='ventas',
    )
    fecha = models.DateField()
    unidades = models.PositiveIntegerField()
    articulo = models.CharField(max_length=255)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    neto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    coste = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha', '-id']

    def __str__(self):
        return f'Venta #{self.id} - {self.producto.referencia}'

    def clean(self):
        if self.descuento < 0 or self.descuento > 100:
            raise ValidationError({'descuento': 'El descuento debe estar entre 0 y 100.'})

    @classmethod
    def actualizar_stock_producto(cls, producto_id: int):
        from django.db.models import Sum

        from core.compras.models import Compra

        total_compras = Compra.objects.filter(producto_id=producto_id).aggregate(
            total=Sum('cantidad')
        )['total'] or 0
        total_ventas = cls.objects.filter(producto_id=producto_id).aggregate(
            total=Sum('unidades')
        )['total'] or 0
        stock_actual = max(total_compras - total_ventas, 0)
        Producto.objects.filter(pk=producto_id).update(stock_actual=stock_actual)

    def save(self, *args, **kwargs):
        venta_anterior = None
        if self.pk:
            venta_anterior = type(self).objects.filter(pk=self.pk).values('producto_id').first()

        self.full_clean()

        self.articulo = f'{self.producto.referencia} - {self.producto.descripcion}'

        subtotal = (self.pvp * Decimal(self.unidades)).quantize(Decimal('0.01'))
        factor_descuento = (Decimal('100.00') - self.descuento) / Decimal('100.00')
        self.neto = (subtotal * factor_descuento).quantize(Decimal('0.01'))
        self.coste = (self.producto.coste * Decimal(self.unidades)).quantize(Decimal('0.01'))

        super().save(*args, **kwargs)

        type(self).actualizar_stock_producto(self.producto_id)

        if venta_anterior and venta_anterior['producto_id'] != self.producto_id:
            type(self).actualizar_stock_producto(venta_anterior['producto_id'])

    def delete(self, *args, **kwargs):
        producto_id = self.producto_id
        super().delete(*args, **kwargs)
        type(self).actualizar_stock_producto(producto_id)
