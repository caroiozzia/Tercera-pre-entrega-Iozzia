from django.shortcuts import render

# Create your views here.

from .forms import CategoriaForm, ProductoForm, ClienteForm
from .models import Categoria, Producto, Cliente

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

