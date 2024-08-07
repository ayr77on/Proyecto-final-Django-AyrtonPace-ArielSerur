from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.name
