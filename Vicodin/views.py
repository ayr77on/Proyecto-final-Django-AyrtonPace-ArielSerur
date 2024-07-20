from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "Vicodin/index.html")

def nosotros(request):
    return render(request, "Vicodin/nosotros.html")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")