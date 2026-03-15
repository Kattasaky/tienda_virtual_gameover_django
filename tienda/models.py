from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
#las imagenes vana en la carpeta media
imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

#categoría básica para los productos
categoria = models.CharField(max_length=50, null=True, blank=True)

#fecha de creación del producto automáticamente al crear un nuevo producto
creado = models.DateTimeField(auto_now_add=True) #fecha de actualización del producto automáticamente al guardar cambios

def __str__(self):
    return self.nombre 
#esta función devuelve el nombre del producto cuando se imprime el objeto Producto, lo que facilita
#la identificación de los productos en el panel de administración de Django.