from django.shortcuts import render

# Create your views here.
from .models import Producto

def catalogo(request):
    productos = Producto.objects.filter(activo=True) # solo mostrar productos activos
    
    return render(request, 'tienda/catalogo.html', {
        'productos': productos
    })    

def detalle_producto(request, id):
    producto = Producto.objects.get(id=id)

    return render(request, 'tienda/detalle_producto.html', {
        'producto': producto
    })