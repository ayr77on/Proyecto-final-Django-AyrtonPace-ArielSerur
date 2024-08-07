from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from users.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "Vicodin/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"Vicodin/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()
    return render(request,"users/register.html" ,  {"form":form, "msg_register": msg_register})

# @login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            if miFormulario.cleaned_data.get('imagen'):
                usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.imagen.save()
            miFormulario.save()

            return render(request, "Vicodin/index.html")

    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "users/edit_user.html", {"form": miFormulario, "usuario": usuario})


# Test123!
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/change_pass.html"
    success_url = reverse_lazy("EditarPerfil")