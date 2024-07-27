from django.urls import path
from Vicodin import views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('crear-producto/', views.crear_producto, name='CrearProducto'),
    path('crear-cliente/', views.crear_cliente, name='CrearCliente'),
    path('crear-publicacion/', views.crear_blog, name='CrearBlog'),
    path('buscar-producto/', views.buscar_producto, name="BuscarProducto"),
]