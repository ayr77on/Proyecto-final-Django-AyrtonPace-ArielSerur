from django.shortcuts import render
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Vicodin.models import Blog, Comentario, Producto
from .forms import BlogForm, BuscarProductoForm, ClienteForm, ComentarioForm, ProductoForm

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

def about(request):
    return render(request, "Vicodin/nosotros.html")


# VISTAS BASADAS EN CLASES - Productos
class ProductoListView(ListView):
    model = Producto
    template_name = "Vicodin/vbc/producto_list.html"
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "Vicodin/vbc/producto_detail.html"
    def get_login_url(self):
        return self.login_url


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "Vicodin/vbc/producto_create.html"
    fields = ["name", "price", "description",'image']
    success_url = reverse_lazy("ProductoList")


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    success_url = reverse_lazy("ProductoList")
    login_url = '/accounts/login/'
    fields = ["name", "price", "description",'image']
    template_name = "Vicodin/vbc/producto_update.html"


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("ProductoList")
    login_url = '/accounts/login/' 
    template_name = 'Vicodin/vbc/producto_delete.html'


# --------------------------------------------------------------------------------

# VISTAS BASADAS EN CLASES - Blog
class PublicacionListView(LoginRequiredMixin,ListView):
    model = Blog
    template_name = "Vicodin/vbc/publicacion_list.html"
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PublicacionDetailView(FormMixin, DetailView):
    model = Blog
    template_name = "Vicodin/vbc/publicacion_detail.html"
    form_class = ComentarioForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(blog=self.get_object())
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse('PublicacionDetail', kwargs={'pk': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return self.handle_no_permission()

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comentario = form.save(commit=False)
        comentario.user = self.request.user
        comentario.blog = self.get_object()
        comentario.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "Vicodin/vbc/publicacion_create.html"
    login_url = '/accounts/login/'
    fields = ["name", "date", "description",'body','image']
    success_url = reverse_lazy("PublicacionList")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy("PublicacionList")
    login_url = '/accounts/login/'
    fields = ["name", "date", "description"]
    template_name = "Vicodin/vbc/publicacion_update.html"


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("PublicacionList")
    login_url = '/accounts/login/'
    template_name = 'Vicodin/vbc/publicacion_delete.html'