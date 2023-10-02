from django.shortcuts import render


def inicio(request):
    return render(request,"AppNico/inicio.html")

def estudiantes(request):
    return render(request, "")
