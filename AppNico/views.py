from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render(request,"AppNico/index.html")

def curso(request):
    return render(request,"AppNico/curso.html")

def estudiantes(request):
    return HttpResponse("Hola Estudiantes!")

def profesores(request):
    return("Hola Profesores!")


