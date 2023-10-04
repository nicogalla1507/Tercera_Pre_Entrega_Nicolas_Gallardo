from django import forms

class Formulario(forms.Form):
    
    usuario = forms.CharField()
    contrasena =forms.CharField()
    