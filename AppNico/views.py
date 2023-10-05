from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Login, Register, Curso
from .forms import Formulario, FormularioRegister, FormularioCurso


def inicio(request):
    return render(request,"AppNico/index.html")

def curso(request):
    if request.method == "POST":
        
        mi_formulario2 = FormularioCurso(request.POST)
        print(mi_formulario2)
        
        if mi_formulario2.is_valid():
            informacion = mi_formulario2.cleaned_data
            nombre = informacion.get("nombre", "")       
            camada = informacion.get("camada", "")
            info_curso= Curso(nombre=informacion["nombre"],camada=informacion["camada"] ) #tuve problemas en esta parte y era porque no coincidian los nombres con los modelos de la base de datos
            info_curso.save()
            print("VOLVIO AL INDEX")
            return render(request,"AppNico/index.html")
    else:
        print("Se ejecuto el bucle else \n\n")
        mi_formulario2 = FormularioCurso()
        print("\n\n\nSe ejecuto el formulario")
        
    return render(request,"AppNico/curso.html",{"mi_formulario2":mi_formulario2})


def estudiantes(request):
    return render(request,"AppNico/estudiantes.html")

def register(request):
    return render(request,"AppNico/register.html")

def login(request):
    return render(request,"AppNico/login.html")

#def formulario(request):
    if request.method == 'POST':
        
        inicio_sesion = Login(request.POST['login'])
        
        inicio_sesion.save()
        
        return render(request,"AppNico/index.html")
    
    return render(request,"AppNico/formulario.html")

def appform(request):
    if request.method == "POST":
        
        mi_formulario = Formulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario = informacion.get("usuario", "")       
            contrasena = informacion.get("contrasena", "")
            usuario_contra= Login(usuario=informacion["usuario"],contrasena=informacion["contrasena"] ) #tuve problemas en esta parte y era porque no coincidian los nombres con los modelos de la base de datos
            usuario_contra.save()
            print("VOLVIO AL INDEX")
            return render(request,"AppNico/index.html")
    else:
        print("Se ejecuto el bucle else \n\n")
        mi_formulario = Formulario()
        print("\n\n\nSe ejecuto el formulario")
        
    return render(request,"AppNico/formulario.html",{"mi_formulario":mi_formulario})


def appformRegister(request):
    
    if request.method == "POST":
        
        register_form = FormularioRegister(request.POST)
        
        if register_form.is_valid():
            info = register_form.cleaned_data
            nombre=info.get("nombre","")
            apellido=info.get("apellido","")
            email=info.get("email","")
            contrasena = info.get("contrasena","")
            
            datos = Register(nombre=info["nombre"],apellido=info["apellido"],email=info["email"],contrasena=info["contrasena"])
            datos.save()
            return render(request,"AppNico/index.html")
    else:
        register_form = FormularioRegister()
    
    return render(request,"AppNico/formulario_register.html",{"register_form":register_form})


def busqueda(request):
    if request.GET["nombre"]:
        nombre= request.GET['nombre']
        
    
    return render(request,"AppNico/busqueda_register.html")
    
    
def busquedaR(request):
    
    nombre= f"Buscando register {request.GET['nombre']}"
    apellido = f"Buscando apellido {request.GET['apellido']}"
    email = f"buscando email {request.GET['email']}"
    contrasena = f"buscando contrasena {request.GET['contrasena']}"
    
    return HttpResponse(nombre,apellido,email,contrasena)
    

