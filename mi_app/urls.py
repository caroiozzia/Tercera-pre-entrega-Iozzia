from django import views
from django.urls import path, include
from ProyectoEntrega.views import insertar_categoria, insertar_cliente, insertar_producto, buscar

urlpatterns = [path('insertar_categoria/', insertar_categoria, name='insertar_categoria'),
    path('insertar_producto/', insertar_producto, name='insertar_producto'),
    path('insertar_cliente/', insertar_cliente, name='insertar_cliente'),
    path('buscar/', buscar, name='buscar'),
]
