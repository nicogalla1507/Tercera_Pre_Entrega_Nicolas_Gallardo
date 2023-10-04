from django.shortcuts import render
from .models import Login
from .forms import Formulario

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

def formulario(request):
    if request.method == 'POST':
        
        inicio_sesion = Login(request.POST['login'])
        
        inicio_sesion.save()
        
        return render(request,"AppNico/index.html")
    
    return render(request,"AppNico/formulario.html")

def appform(request):
    if request.method == 'POST':
        
        mi_formulario = Formulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario_contra= Login(usuario=informacion["usuario"],contrasena=informacion["contrasena"] )
            usuario_contra.save()
            
            return render(request,"AppNico/index.html")
    else:
        mi_formulario = Formulario()
            
    return render(request,"AppNico/formulario.html",{"mi_formulario":mi_formulario})
    
    