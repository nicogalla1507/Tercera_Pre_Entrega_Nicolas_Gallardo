from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render(request,"AppNico/index.html")

def curso(request):
    return render(request,"AppNico/curso.html")

def estudiantes(request):
    return render(request,"AppNico/estudiantes.html")

def register(request):
    return render(request,"AppNico/register.html")

def login(request):
    return render(request,"AppNico/login.html")


