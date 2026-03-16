from django.db import models

# Modelo que representa los productos de la tienda
class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    # las imágenes se guardan en la carpeta media/productos
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    # categoría básica para los productos
    categoria = models.CharField(max_length=50, null=True, blank=True)

    # permite activar o desactivar productos
    activo = models.BooleanField(default=True)

    # fecha de creación automática
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre