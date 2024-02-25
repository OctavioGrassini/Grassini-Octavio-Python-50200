from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#class ClienteForm(forms.Form):
#    nombre = forms.CharField(max_length = 25, required = True)
#    apellido = forms.CharField(max_length = 25, required = True)
#    email = forms.EmailField(required = True)
#
#class EditorialForm(forms.Form):
#    nombre = forms.CharField(max_length = 25, required = True)
#    email = forms.EmailField(required = True)
#
#class LibroForm(forms.Form):
#    nombre = forms.CharField(max_length = 50, required = True)
#    autor = forms.CharField(max_length = 50, required = True)
#    anio = forms.IntegerField(required = True)
#
#    class Meta:
#        fields = [ 'nombre', 'autor', 'año' ]

class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length = 25, required = True)
    email = forms.EmailField(required = True)
    password1 = forms.CharField(max_length = 30, label = "Contraseña", required = True, widget = forms.PasswordInput)
    password2 = forms.CharField(max_length = 30, label = "Confirmar Contraseña", required = True, widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']