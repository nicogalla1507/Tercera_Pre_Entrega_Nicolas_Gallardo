from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render(request,"AppNico/index.html")

def curso(request):
    return HttpResponse("Bienvenido al curso de python")

def estudiantes(request):
    return HttpResponse("Hola Estudiantes!")

def profesores(request):
    return("Hola Profesores!")


