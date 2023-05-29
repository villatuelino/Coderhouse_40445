from django.db import models
from django.utils import timezone


class ProductoCategoria(models.Model):
    """Modelo de Django para representar categorías de productos."""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto."""
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    unidad_de_medida = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        models.UniqueConstraint(fields=["categoría", "nombre"], name="categoria_producto")
        indexes = [models.Index(fields=["nombre"])]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio:.2f}"


class Iventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.FloatField()
    fecha_compra = models.DateTimeField(default=timezone.now)
