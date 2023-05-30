from django.db import models
from django.utils import timezone


class ProductoCategoria(models.Model):
    """Categorías de productos."""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto."""
        return self.nombre


class Producto(models.Model):
    """Productos que corresponden a una categoría. Cada vez que se actualiza el precio, se modifica la fecha de actualización."""

    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    unidad_de_medida = models.CharField(max_length=50)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    _fecha_actualizacion = models.DateTimeField(editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["categoria", "nombre"], name="cat_nom1"),
            models.UniqueConstraint(fields=["categoria", "nombre"], condition=models.Q(categoria=None), name="cat_nom2"),
        ]
        indexes = [models.Index(fields=["nombre"])]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio:.2f}"

    @property
    def fecha_actualización(self):
        self.ver_precio_actualizar_fecha()
        return self._fecha_actualizacion

    def ver_precio_actualizar_fecha(self):
        if self.pk:
            original_producto = Producto.objects.get(pk=self.pk)
            if original_producto != self.precio:
                self._fecha_actualizacion = timezone.now
