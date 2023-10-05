from django import forms

class Formulario(forms.Form):
    usuario = forms.CharField()
    contrasena = forms.CharField()
    
class FormularioRegister(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    contrasena = forms.CharField()