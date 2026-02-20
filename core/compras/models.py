from decimal import Decimal

from django.db import models
from django.db.models import DecimalField, ExpressionWrapper, F, Sum

from core.productos.models import Producto
from core.proveedores.models import Proveedor


class Compra(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='compras',
    )
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        related_name='compras',
    )
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    coste_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-fecha', '-id']

    def __str__(self):
        return f'Compra #{self.id} - {self.producto.referencia}'

    @classmethod
    def actualizar_coste_medio_producto(cls, producto_id: int):
        resumen = cls.objects.filter(producto_id=producto_id).aggregate(
            total_cantidad=Sum('cantidad'),
            total_coste=Sum(
                ExpressionWrapper(
                    F('cantidad') * F('coste_unitario'),
                    output_field=DecimalField(max_digits=14, decimal_places=2),
                )
            ),
        )

        total_cantidad = resumen['total_cantidad'] or 0
        total_coste = resumen['total_coste']

        if total_cantidad > 0 and total_coste is not None:
            coste_medio = (total_coste / Decimal(total_cantidad)).quantize(Decimal('0.01'))
        else:
            coste_medio = Decimal('0.00')

        Producto.objects.filter(pk=producto_id).update(coste=coste_medio)

    @classmethod
    def actualizar_stock_producto(cls, producto_id: int):
        from core.ventas.models import Venta

        total_compras = cls.objects.filter(producto_id=producto_id).aggregate(
            total_cantidad=Sum('cantidad')
        )['total_cantidad'] or 0
        total_ventas = Venta.objects.filter(producto_id=producto_id).aggregate(
            total_unidades=Sum('unidades')
        )['total_unidades'] or 0
        stock_actual = max(total_compras - total_ventas, 0)
        Producto.objects.filter(pk=producto_id).update(stock_actual=stock_actual)

    def save(self, *args, **kwargs):
        compra_anterior = None
        if self.pk:
            compra_anterior = type(self).objects.filter(pk=self.pk).values('producto_id').first()

        super().save(*args, **kwargs)

        type(self).actualizar_coste_medio_producto(self.producto_id)
        type(self).actualizar_stock_producto(self.producto_id)

        if compra_anterior and compra_anterior['producto_id'] != self.producto_id:
            type(self).actualizar_coste_medio_producto(compra_anterior['producto_id'])
            type(self).actualizar_stock_producto(compra_anterior['producto_id'])

    def delete(self, *args, **kwargs):
        producto_id = self.producto_id
        super().delete(*args, **kwargs)
        type(self).actualizar_coste_medio_producto(producto_id)
        type(self).actualizar_stock_producto(producto_id)
