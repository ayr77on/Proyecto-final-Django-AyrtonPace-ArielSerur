from django.contrib import admin

# Register your models here.
from .models import Blog, Cliente, Producto

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Blog)