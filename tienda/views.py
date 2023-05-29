from django.shortcuts import render
from .models import Producto, CategoriaProd

# Create your views here.

def tienda(request):

    productos = Producto.objects.all()

    return render(request, "tienda/tienda.html", {"productos": productos})

def categoriaProd(request, categoria_id):
    categoriaProd = CategoriaProd.objects.get(id=categoria_id)
    prodcutos = Producto.objects.filter(categorias=categoriaProd)
    return render(request, "tienda/categoriaProd.html", {"categoriaProd": categoriaProd, "productos": prodcutos})