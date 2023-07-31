from django.shortcuts import render

# Create your views here.
from mi_app.forms import CategoriaForm, ProductoForm, ClienteForm
from mi_app.models import Categoria, Producto, Cliente
from django.contrib import messages

def insertar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'mi_app/insertar_categoria.html', {'form': form})

def insertar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'mi_app/insertar_producto.html', {'form': form})

def insertar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'mi_app/insertar_cliente.html', {'form': form})

def buscar(request):
    # Lógica para buscar datos en la base de datos
    return render(request, 'mi_app/buscar.html')

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response
