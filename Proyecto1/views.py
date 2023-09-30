from datetime import datetime as dt
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader


def saludo(request):
    return HttpResponse("Hola django-Nico")

def segunda(request):
    return HttpResponse("<br><br> Ya entendi")

def hora(request):
    hoy = dt.now()
    
    return HttpResponse(f"hola, la hora de hoy es {hoy}")

def probando_template1(request):
    
    diccionario = {
        "first_name": "Nicolas",
        "last_name": "Gallardo",
        "notas":[5,6,7,10]
    }
    miHtml = open('./templates/template1.html') #abrimos el archivo html
    
    plantilla = Template(miHtml.read()) #creamos el template con el uso de la clase Template
    
    miHtml.close()  #cerramos el archivo previamente abierto ya que lo tenemos en la carpeta plantilla
    
    mi_contexto= Context(diccionario)   #creamos un contexto 
    
    documento = plantilla.render(mi_contexto) #construimos el template renderizandolo con el contexto 
    
    return HttpResponse(documento)

