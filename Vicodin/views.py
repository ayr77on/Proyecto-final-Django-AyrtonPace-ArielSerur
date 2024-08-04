from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Vicodin.models import Blog, Producto
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


# VISTAS BASADAS EN CLASES - Productos
class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "Vicodin/vbc/producto_list.html"
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "Vicodin/vbc/producto_detail.html"
    def get_login_url(self):
        return self.login_url


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "Vicodin/vbc/producto_create.html"
    fields = ["name", "price", "description"]
    success_url = reverse_lazy("ProductoList")


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    success_url = reverse_lazy("ProductoList")
    login_url = '/users/login/'
    fields = ["name", "price", "description"]
    template_name = "Vicodin/vbc/producto_update.html"


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("ProductoList")
    login_url = '/users/login/' 
    template_name = 'Vicodin/vbc/producto_delete.html'


# --------------------------------------------------------------------------------

# VISTAS BASADAS EN CLASES - Blog
class PublicacionListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "Vicodin/vbc/publicacion_list.html"
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PublicacionDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "Vicodin/vbc/publicacion_detail.html"
    def get_login_url(self):
        return self.login_url


class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "Vicodin/vbc/publicacion_create.html"
    login_url = '/users/login/'
    fields = ["name", "date", "description"]
    success_url = reverse_lazy("PublicacionList")


class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy("PublicacionList")
    login_url = '/users/login/'
    fields = ["name", "date", "description"]
    template_name = "Vicodin/vbc/publicacion_update.html"


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("PublicacionList")
    login_url = '/users/login/'
    template_name = 'Vicodin/vbc/publicacion_delete.html'