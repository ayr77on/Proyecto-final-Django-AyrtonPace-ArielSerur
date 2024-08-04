from django.urls import path
from Vicodin import views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('crear-producto/', views.crear_producto, name='CrearProducto'),
    path('crear-cliente/', views.crear_cliente, name='CrearCliente'),
    path('crear-publicacion/', views.crear_blog, name='CrearBlog'),
    path('buscar-producto/', views.buscar_producto, name="BuscarProducto"),
]


# Productos
urlpatterns += [
    path('producto-list/', views.ProductoListView.as_view(), name="ProductoList"),
    path('producto-detail/<int:pk>/', views.ProductoDetailView.as_view(), name="ProductoDetail"),
    path('producto-create/', views.ProductoCreateView.as_view(), name="ProductoCreate"),
    path('producto-update/<int:pk>/', views.ProductoUpdateView.as_view(), name="ProductoUpdate"),
    path('producto-delete/<int:pk>/', views.ProductoDeleteView.as_view(), name="ProductoDelete"),
]

# Publicaciones
urlpatterns += [
    path('publicacion-list/', views.PublicacionListView.as_view(), name="PublicacionList"),
    path('publicacion-detail/<int:pk>/', views.PublicacionDetailView.as_view(), name="PublicacionDetail"),
    path('publicacion-create/', views.PublicacionCreateView.as_view(), name="PublicacionCreate"),
    path('publicacion-update/<int:pk>/', views.PublicacionUpdateView.as_view(), name="PublicacionUpdate"),
    path('publicacion-delete/<int:pk>/', views.PublicacionDeleteView.as_view(), name="PublicacionDelete"),
]
