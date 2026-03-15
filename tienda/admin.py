from django.contrib import admin

# Register your models here.
from .models import Producto
#registro del modelo para administración
admin.site.register(Producto)
