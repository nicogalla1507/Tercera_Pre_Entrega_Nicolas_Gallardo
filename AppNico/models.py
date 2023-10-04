from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.CharField(max_length=50)
    
class Register(models.Model):
    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    
class Login(models.Model):
    email= models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)