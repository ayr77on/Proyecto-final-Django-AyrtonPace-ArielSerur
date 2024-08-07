from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='Login'),
     path('registro/',views.register, name='Register'),
     path('logout/', auth_views.LogoutView.as_view(template_name='Vicodin/logout.html'), name="Logout"),
     path('edit/', views.editar_perfil, name="EditarPerfil"),
     path('cambiar_pass/', views.CambiarContrasenia.as_view(), name="CambiarPass")
]