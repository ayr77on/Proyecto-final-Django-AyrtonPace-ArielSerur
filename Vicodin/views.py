from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Vicodin.models import Producto
from .forms import BlogForm, BuscarProductoForm, ClienteForm, ProductoForm

def inicio(request):
    return render(request, "Vicodin/index.html")

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Vicodin/form_exito.html', {'form': "Cliente","texto_breadcrumb" : "Alta de cliente exitosa"})
    else:
        form = ClienteForm()
    return render(request, 'Vicodin/clientes.html', {'form': form,"texto_breadcrumb" : "Dar alta cliente"})

def crear_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Vicodin/form_exito.html', {'form': "Cliente","texto_breadcrumb" : "Alta de publicacion exitosa"})
    else:
        form = BlogForm()
    return render(request, 'Vicodin/publicaciones.html', {'form': form,"texto_breadcrumb" : "Dar alta publicación"})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Vicodin/form_exito.html', {'form': "Producto","texto_breadcrumb" : "Alta de producto exitosa"})
    else:
        form = ProductoForm()
    return render(request, 'Vicodin/productos.html', {'form': form,"texto_breadcrumb" : "Dar alta producto"})

def buscar_producto(request):
    if request.method == "POST":
        mi_formulario = BuscarProductoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            productos = Producto.objects.filter(name__icontains=informacion["producto"])

            return render(request, "Vicodin/productos_busqueda_resultados.html", {"productos": productos,"texto_breadcrumb" : "Resultado Busqueda"})
    else:
        mi_formulario = BuscarProductoForm()

    return render(request, "Vicodin/productos_busqueda.html", {"mi_formulario": mi_formulario,"texto_breadcrumb" : "Buscar productos"})