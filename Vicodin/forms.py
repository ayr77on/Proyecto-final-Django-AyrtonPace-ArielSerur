from django import forms
from .models import Blog, Cliente, Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'description', 'price']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name', 'email', 'password']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description', 'date']

class BuscarProductoForm(forms.Form):
    producto = forms.CharField()