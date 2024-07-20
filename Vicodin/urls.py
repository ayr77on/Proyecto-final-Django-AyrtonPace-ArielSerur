from django.urls import path
from Vicodin import views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('nosotros/', views.nosotros,name="Nosotros"),
]