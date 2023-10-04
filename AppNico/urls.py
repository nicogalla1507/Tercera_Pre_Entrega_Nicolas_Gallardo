from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('curso/',curso, name="curso"),
    path('estudiantes/',estudiantes,name="estudiantes"),
    path('register/',register,name="register"),
    path('login/',login,name="login")
    ]

