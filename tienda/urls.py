from django.urls import path #importamos la función path para definir las rutas de la app
from . import views #importamos las vistas de la app

urlpatterns = [ #definimos la ruta para el catálogo de productos
    path('', views.catalogo, name='catalogo'),
]